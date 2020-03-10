from app import db
import math

class airports(db.Model):
    __tablename__ = "airports"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    def __repr__(self):
        return "<airports: {}="">".format(self.name)

class sights(db.Model):
    __tablename__ = "sights"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    wikilink = db.Column(db.String)
    airport_id = db.Column(db.String, db.ForeignKey("airports.id"))


    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

class travelplan:
	def __init__(self, startairport, startlat, startlon, endairport, endlat, endlon): 
		self.startairport = startairport 
		self.startlat = startlat 
		self.startlon = startlon 
		self.endairport = endairport 
		self.endlat = endlat 
		self.endlon = endlon 
		self.distance = 0
		self.planeco2 = 0
		self.durationplane = 0 
		self.railco2 = 0
		self.durationrail = 0
		self.kerosininliter  = 0
		self.co2_emission_kg  = 0
		self.trees = 0
		self.fee = 0 

	def calculate_distance(self): 
		radius = 6371 #km 
		dlat = math.radians(self.endlat-self.startlat)  
		dlon = math.radians(self.endlon-self.startlon) 
		a = math.sin(dlat/2) ** 2  +  math.cos(math.radians(self.startlat)) * math.cos(math.radians(self.endlat))* math.sin(dlon/2)**2 
		c = math.asin(math.sqrt(a))*2
		self.distance = round(radius * c,2) #source: https://gist.github.com/rochacbruno/2883505
		self.durationplane = round(self.distance / 800,2)   #800 kmh pro Stunde

	def calculate_fuelemission(self): 
		C_kerosin_liter_per_passenger_per_100km = 6.3 
		C_tree_co2_filter_kg = 12.5 
		C_co2_fee_in_euro_per_ton = 130
		C_kerosin_in_co2_kg = 3.16 #atmosfair
		
		self.kerosininliter = round((self.distance / 100) * C_kerosin_liter_per_passenger_per_100km,2) 
		self.co2_emission_kg = round ((self.kerosininliter * 0.8) * C_kerosin_in_co2_kg,2) 
		self.trees = round(self.co2_emission_kg / C_tree_co2_filter_kg,0) 
		self.fee = round((self.co2_emission_kg / 1000) * C_co2_fee_in_euro_per_ton,2)
