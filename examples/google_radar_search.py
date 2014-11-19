import _bootstrap_

from classes.Scanner import *
from classes.services.GoogleRadarSearch import *

#
# In this example we will use the google radar search service
# to look for all groceries or supermarkets with the name "ICA".
# 
#
# For the full options for the Radar Search you can check the
# "Optional paremeters" here:
# https://developers.google.com/places/documentation/search#RadarSearchRequests
#

scanner = Scanner()
searchitems={"types": "restaurant"};
key="AIzaSyARitVLsV9jQ623B2OKb8YyT_b2BuYU77o" # Insert your Google key here
service = GoogleRadarSearch(searchitems, key)
scanner.set_service(service)
scanner.start_scanning()
