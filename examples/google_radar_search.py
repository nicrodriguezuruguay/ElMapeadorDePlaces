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
searchitems={"name": "Subway|McDonald's|Relate|Nooshin's|Quiznos|Ecotopiia|Ampool|Gamestop|Vons|Ralphs|Vons|Autozone|Target|Staples|Walmart|Baskin-Robbins|Chili's"};
key="AIzaSyAIedHRPPqW3-a2q5xq60Gg5RugUsYUHgE" # Insert your Google key here
service = GoogleRadarSearch(searchitems, key)
scanner.set_service(service)
scanner.start_scanning()
#searchitems={"name": "ica", "types": "grocery_or_supermarket"};

#places = ["Subway|7-Eleve|McDonald's|Relate|Nooshin's|Quiznos|Ecotopiia|Ampool|Gamestop|Vons|Ralphs|Vons|Autozone|Target|Staples|Walmart|Baskin-Robbins|Chili's"]


#scanner = Scanner()
#key="AIzaSyAIedHRPPqW3-a2q5xq60Gg5RugUsYUHgE" # Insert your Google key here
#for place in places:
  #searchitems = {"name":"Rite+Aid|Deluxe+T-Shirts|7-Eleve|AT&T+Store|Soulscape+Gift+and+Book+Store|Barnes+&+Noble|Buffalo+Wild+Wings|Bliss+101|Burger+King|Buy+Buy+Baby|Futon+Outlet|Pink+Peloton|ROXY+Restaurant+and+Ice+Cream|Barry+Robert+Mozlin|Artistic+Sewing|Encinitas+Television|Collector's+Cottage|San+Enchinitas|Mexico+Viejo|Webassist+com|California+Custom+Creations|Blue+Fin+Sushi+Bar|Ross+Stores|Super+Donut+1|Sacred+Silks|Foot+Solutions|Giant+New+York+Pizza+and+Pasta|Best+Buy|Anati+Baby|Rocky+Horror+Picture+Show|Flashbacks+Recycled+Fashion|Chronic+Tacos|Ampdraw+Hobbies|Mukunda+Gifts+and+Boutiques|Alberto's+Mexican+Food|Joseph+Alan+Galleries|Lil+Jungle+Java|Jamba+Juice|Lottery+Ticket+Sales|Peace+Pies|Lady+Rox|Patio+Source|Encinitas+Florist+Co.|Bailey's-That+Cat+Place|Fish+101|Juanita's+Taco+Shop|Acanthus+Antiques|Oggi's+Pizza+and+Brewing+Co.|Losts+At+Moonlight+Beach|D+and+E+Propagators|Shakarian+Jewelry|Flour+Power+Custom+Bakery|Coco's+Bakery|San+Dieguito+Heritage+Museum|Jamroc+101+Caribbean+Grill|Sunshine+Gardens|Alpha+Vision|Redbox|Sabor+de+Vida+Brazilian+Grill|O'Hurley's+Beach+Bar|Encinitas+Florist+Co.|Albertsons-Sav-O|+Food+Centers|Chipotle+Mexican+Grill|Pizza+Hut|Whole+Foods+Market|Carl's+Jr.|Dollar+Tree|99+Cents+Only+Stores|Big+Lots|CVS+Pharmacy|101+Diner|2Good2B+Bakery+and+Cafe|Pilates+and+Beyond|Aaron+Brothers+Art+and+Framing"};
	#service = GoogleRadarSearch(searchitems, key)
	#scanner.set_service(service)
	#scanner.start_scanning()