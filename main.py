# main.py
from app import app
from db_setup import init_db, db_session
from forms import AirportSearchForm
from flask import flash, render_template, request, redirect
from models import airports, sights, travelplan
from tables import Results

init_db()
startairport_db=''
endairport_db=''


@app.route('/', methods=['GET', 'POST'])
def index():
	search = AirportSearchForm(request.form)

	if request.method == 'POST':
		return search_results(search)

	return render_template('index.html', form=search)


@app.route('/results')

def search_results(search):
	results = []
	search_string_startairport = search.data['startairport']
	search_string_endairport = search.data['endairport']
	startairport_db=''
	endairport_db=''
	airportsfound = 0
	sights_db=''

	if search.data['startairport'] != '':
		startairport_db = airports.query.filter(airports.name.ilike(search_string_startairport)).first()
		airportsfound = airports.query.filter(airports.name.ilike(search_string_startairport)).count()

	if search.data['endairport'] != '':
		endairport_db = airports.query.filter(airports.name.ilike(search_string_endairport)).first()
		if airportsfound > 0:
			airportsfound = airports.query.filter(airports.name.ilike(search_string_endairport)).count();
	else:
		 airportsfound = 0



	if airportsfound < 1:
		flash('No results found!') 
		return redirect('/')

	else:	
	
		sights_db = sights.query.filter(sights.airport_id.ilike(endairport_db.id)).first()
        	# calculate and display results
		mytravelplan = travelplan(startairport_db.name, startairport_db.lat, startairport_db.long, endairport_db.name, endairport_db.lat, endairport_db.long)
		mytravelplan.calculate_distance()
		mytravelplan.calculate_fuelemission()
		return render_template('results.html', airportsfound=airportsfound, startairport=startairport_db, endairport=endairport_db , mytravelplan=mytravelplan , sights_db = sights_db  )



#if __name__ == '__main__': 
#      app.run(host='http://flightsherif.dnsuser.de/', port=80, 
#      debug=True)
if __name__ == '__main__': 
	app.run(host='0.0.0.0', port=80, debug=True)
