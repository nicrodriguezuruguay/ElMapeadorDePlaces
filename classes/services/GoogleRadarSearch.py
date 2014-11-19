from lib.google_places import *

import json
from lxml import etree
from time import sleep


# Makes a google radar search for each box
class GoogleRadarSearch():
   
   # SERVICE RULES
   service = {
      'authentication':{
         'REQUIRED'    : True
      },
      'request': {
         'COST_PER_REQUEST' : 5,
         'MAX_COST_DAY'     : 1000
      },
      'response': {
         'MAX_RESULTS' : 200
      },
      'box': {
         'MAX_X_DISTANCE' : 100000,  # 50km max radius
         'MAX_Y_DISTANCE' : 100000,  # 50km max radius
      }
   }
   
   searchItems = None
   key         = None
   resultsN    = 0

   def __init__(self, searchItems, key):
      self.searchItems=searchItems
      self.key = key

   def search(self, box, logger):

      # Make the radar search request and send it
      googleRequester=GoogleRequester(logger, self.key)
      location=str(box.center[0])+","+str(box.center[1])
      radius=max(box.xMeters, box.yMeters)/2  
      
      req= {'location': location,
            'radius': radius,
            'searchitems': self.searchItems}
      
      googleResponse = googleRequester.send_request(req, 0, 0)
      logger.log_scan(str(box.bounds())+" : "+googleResponse.status+" : "+str(googleResponse.resultsN)+" results")
   
      # Get the markers from the response
      markers=[]
      for result in googleResponse.results:
         details = G_details(result['reference'], False, self.key)

         self.root = etree.fromstring(details)
         self.status = self.root[0].text
         self.results = []

         for result1 in self.root.findall('result'):

            det = {}
            

            if len(result1.findall('name')) > 0:
               det['name']  = result1.findall('name')[0].text
            else:
               det['name']  = ''


            if len(result1.findall('formatted_address')) > 0:
               det['address']  = result1.findall('formatted_address')[0].text
            else:
               det['address']  = ''


            if len(result1.findall('international_phone_number')) > 0:
               det['tel']  = result1.findall('international_phone_number')[0].text
            else:
               det['tel']  = ''


            if len(result1.findall('website')) > 0:
               det['website']  = result1.findall('website')[0].text
            else:
               det['website']  = ''


            types = result1.findall('type')
            det['type'] = ''

            for i in range(0, len(types)):
               if types[i].text in ("cafe", "bakery", "grocery_or_supermarket", "restaurant"):
                  det['type'] = types[i].text


            address_component = result1.findall('address_component')
            det['postal_code'] = ''
            det['postal_code_suffix'] = ''
            for i in range(0, len(address_component)):
               if address_component[i].findall('type')[0].text == 'postal_code':
                  det['postal_code'] = address_component[i].findall('long_name')[0].text
               if address_component[i].findall('type')[0].text == 'postal_code_suffix':
                  det['postal_code_suffix'] = address_component[i].findall('long_name')[0].text


         self.resultsN+=1
         markers.append(result['location'])
         logger.log_result(str(self.resultsN) + " : " + str(det['name']) + " : " + str(det['address']) + " : " + str(result['location']) + " : " + str(det['tel']) + " : " + str(det['website']) + " : " + str(det['type']) + " : " + str(det['postal_code']) + " : " + str(det['postal_code_suffix']) )
   
      return markers


class GoogleResponse():
   
   # eTree
   root = None
   results = None
   
   # Parsed
   status = None
   
   # Stats
   resultsN = 0

   # Returns status of response
   def __init__(self, response):
      self.root = etree.fromstring(response)
      self.status = self.root[0].text
      self.results = []
      
      if (self.status=='OK'):
         for result in self.root.findall('result'):
            loc = result.findall('.//location')[0]
            newResult = {}
            newResult['location']  = (loc[0].text, loc[1].text)
            newResult['reference'] = result.findall('reference')[0].text
            newResult['id']        = result.findall('id')[0].text
            self.results.append(newResult)
            self.resultsN+=1
            #print(etree.tostring(result).decode("utf-8"))
            
            
class GoogleRequester():
   
   logger = None
   key = None

   # Returns status of response
   def __init__(self, logger, key):
      self.logger=logger
      self.key = key

   def send_request(self, request, maxRetries, retryInterval):
      logger=self.logger
      location    = request['location']
      radius      = request['radius']
      searchitems = request['searchitems']

      retries = -1
      googleResponse= None
      
      # Send the request
      while (retries!=maxRetries):
         resp=G_radarsearch(location, radius, searchitems, self.key)
         googleResponse=GoogleResponse(resp)
         status=googleResponse.status
         
         if (status == 'OK'):
            break
            
         elif (status == 'ZERO_RESULTS'):
            print("Zero results")
            break
            
         elif (status == 'OVER_QUERY_LIMIT'):
            if (retries == maxRetries):
               print("Query limit exceeded for today. Scanning stopped.")
               # EXIT PROGRAM HERE
            print("Query limit exceeded. Will wait a bit and retry.")
            sleep(config['scheduler']['ON_QUERY_LIMIT_WAIT'])
            retries+=1
            continue

         elif (status == 'INVALID_REQUEST'):
            print("Invalid request")
            # EXIT PROGRAM HERE
            
         elif (status == 'REQUEST_DENIED'):
            print("Request denied. Is the Google key correct?")
            # EXIT PROGRAM HERE
            
         else:
            logger.log_scan('scan', 'Unknown error in response from Google server')
            print("Unknown error in response from Google server")
            print("Page received from Google: \n", etree.tostring(googleResponse.root).decode("utf-8"))
            # EXIT PROGRAM HERE

      return googleResponse
