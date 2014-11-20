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

# scanner = Scanner()
# searchitems={"name": "Farrbetter+Sbirits+II"};
# key="AIzaSyCtxr0YD4-2kuDmo_xv-ALBJwtAn_a3J_s" # Insert your Google key here
# service = GoogleRadarSearch(searchitems, key)
# scanner.set_service(service)
# scanner.start_scanning()


places = ["Rite+Aid","Deluxe+T-Shirts","7-Eleven","7-Eleven","Subway","Subway","AT&T+Store","Soulscape+Gift+and+Book+Store","Barnes+&+Noble","Buffalo+Wild+Wings","Bliss+101","Burger+King","Buy+Buy+Baby","7-Eleven","Subway","McDonald's","7-Eleven","Burger+King","Futon+Outlet","Pink+Peloton","ROXY+Restaurant+and+Ice+Cream","Barry+Robert+Mozlin","Artistic+Sewing","Encinitas+Television","Collector's+Cottage","\"Intrepid+Shakespeare+Company+Presents+\"\"Hamlet\"","San+Enchinitas","Mexico+Viejo","Webassist+com","California+Custom+Creations","Blue+Fin+Sushi+Bar","Ross+Stores","Super+Donut+1","Relate","Sacred+Silks","Foot+Solutions","Giant+New+York+Pizza+and+Pasta","Nooshin's","Best+Buy","Anati+Baby","Rocky+Horror+Picture+Show","Flashbacks+Recycled+Fashion","Chronic+Tacos","Ampdraw+Hobbies","Mukunda+Gifts+and+Boutiques","Alberto's+Mexican+Food","Joseph+Alan+Galleries","Quiznos","Lil+Jungle+Java","Jamba+Juice","Lottery+Ticket+Sales","Peace+Pies","Lady+Rox","Patio+Source","Encinitas+Florist+Co.","Bailey's-That+Cat+Place","Fish+101","Juanita's+Taco+Shop","Acanthus+Antiques","Oggi's+Pizza+and+Brewing+Co.","Losts+At+Moonlight+Beach","Ecotopiia","D+and+E+Propagators","Shakarian+Jewelry","Flour+Power+Custom+Bakery","Coco's+Bakery","San+Dieguito+Heritage+Museum","Ampool","Jamroc+101+Caribbean+Grill","Sunshine+Gardens","Alpha+Vision","Redbox","Sabor+de+Vida+Brazilian+Grill","O'Hurley's+Beach+Bar","Encinitas+Florist+Co.","Albertsons-Sav-On,+Food+Centers","Chipotle+Mexican+Grill","Gamestop","Pizza+Hut","Whole+Foods+Market","Vons","Ralphs","Vons","Autozone","Subway","Subway","Subway","Subway","Carl's+Jr.","Target","Dollar+Tree","Staples","99+Cents+Only+Stores","Big+Lots","Walmart","CVS+Pharmacy","CVS+Pharmacy","101+Diner","2Good2B+Bakery+and+Cafe","7-Eleven","7-Eleven","7-Eleven","Pilates+and+Beyond","Aaron+Brothers+Art+and+Framing","Baskin-Robbins","Chili's","Jun,+Omar,+Tahlia+and+Gabe's+Super+Snack+Bar"]
types = ["bakery", "bank", "bar", "bicycle_store", "book_store", "cafe", "clothing_store", "convenience_store", "department_store", "electronics_store", "furniture_store", "gas_station", "grocery_or_supermarket", "hardware_store","home_goods_store", "jewelry_store", "liquor_store", "pet_store", "pharmacy", "restaurant", "shoe_store", "store"]

scanner = Scanner()
key="AIzaSyAst6maqQNSsSzidGCaRe954HebR4mw09o" # Insert your Google key here

for place in places:
	searchitems={"name": place};
	service = GoogleRadarSearch(searchitems, key)
	scanner.set_service(service)
	scanner.start_scanning()

bakery, bank, bar, bicycle_store, book_store, cafe, clothing_store, convenience_store, department_store, electronics_store, furniture_store, gas_station, grocery_or_supermarket, hardware_store,home_goods_store, jewelry_store, liquor_store, pet_store, pharmacy, restaurant, shoe_store, store