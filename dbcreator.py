# db_creator.py
from sqlalchemy import create_engine, ForeignKey, MetaData, Table
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
engine = create_engine('sqlite:///myairports.db', echo=True)
Base = declarative_base()
class airports(Base):
    __tablename__ = "airports"
    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    lat = Column(Float)
    long = Column(Float)

    def __repr__(self):
        return "{}".format(self.name)
class sights(Base):
    __tablename__ = "sights"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    wikilink = Column(String)
    airport_id = Column(String, ForeignKey("airports.id"))
#    airport = relationship("airports", backref=backref(
#        "airports", order_by=id))

# create tables

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

metadata = MetaData()
metadata.reflect(engine, only=['airports'])
airports = Table('airports', metadata, autoload=True, autoload_with=engine)
sights = Table('sights', metadata, autoload=True, autoload_with=engine)
engine.execute(airports.delete())
#engine.execute(airports.insert(), [{'id': 'dff': 'Hamburg' },
#                            {'id': 'fs'},
#                            {'id': 'dds'}])

#airports:

engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("HAM","HAMBURG","https://www-welt-de.cdn.ampproject.org/i/s/www.welt.de/img/regionales/hamburg/mobile101285414/9851623477-ci23x11-w1300/airport-DW-Hamburg-Hamburg-jpg.jpg",53.633621,9.997413)')

engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("DUS","DUESSELDORF","https://www.dus.com/~/media/fdg/dus_com/businesspartner/aviation/flugplatzhandbuch/header_flugplatz_970x320px.jpg?h=320&la=de-DE&w=970",51.276453,6.762533)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("MUC","MUNICH","https://cdn.muenchen-p.de/.imaging/stk/responsive/image980/dms/aktuell-2016/flughafen-totale1-hp/document/flughafen-totale1-hp.jpg",48.354828,11.782588)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("FRA","FRANKFURT","https://www.deutschlandfunk.de/media/thumbs/3/3f6aebd6ca546915cca9162a93593eccv1_max_755x425_b3535db83dc50e27c1bb1392364c95a2.jpg?key=85c472",50.025959,8.572310)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("JFK","NEWYORK","https://aerolatinnews.com/wp-content/uploads/2019/02/jfk-aeropuerto.jpg",40.641433,-73.778085)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("DXB","DUBAI","https://cdn.presstv.com//photo/20180930/b65b8a73-6a22-49ee-9123-0c9ebc8c381c.jpg",25.252898,55.364915)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("LHR","LONDON","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQU389EVtcp-8ZeHquUPURFBnMfU5ioyK_E3B1BUwCvSWo2gqYV",51.470069,-0.454489)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("CDG","PARIS","https://aircharterservice-globalcontent-live.cphostaccess.com/images/germany/destination-guide/airport/312038_paris20cdg20-20banner_tcm57-39385.jpg",49.009677,2.547978)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("YYZ","TORONTO","https://tpprodcdnep.azureedge.net/-/media/project/pearson/content/travel/transportation/thumbnail-images/generic-social.jpg?la=en&mh=630&mw=1200&modified=20190325145243&hash=39EAADC1E67C168C4DB3DF83E018437B471D2596",43.677617,-79.624959)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("BCN","BARCELONA","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS5sRyg-GT0HdhOC8XrtaU1i3M7mo4r32Ul9DymWLPrFmZtrBye",41.297179,2.083026)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("AMS","AMSTERDAM","https://www.aero.de/content/pics/p_11602.jpg",52.310427,4.767792)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("CPH","COPENHAGEN","https://www.shl.dk/wp-content/uploads/2019/07/SHL-Architects_Copenhagen-Airport-T3AE_Exterior_copyrightWAX-Cover-1170x555.jpg",55.629877,12.653368)')

engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("VIE","VIENNA","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSNIlFG3upIpiaa-G7hKUv8xMVEkUIUJ94E0Isu7Gff7Tbq0jQ2",48.112627,16.575321)')

engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("SYD","SYDNEY","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRvgEPHVRVhJKZpzyOj5UuDV-Q34L44jZhpiJBfn99YjtuBzdLK",-33.939700,151.175330)')


engine.execute('INSERT INTO "airports" '
               '(id, name,image,lat,long) '
               'VALUES ("CPT","CAPETOWN","https://www.capetownmagazine.com//media_lib/r1/c10a0cc3e7ca7c05afcd69c2da5db41b.img.jpg",-33.971463,4.767792)')

#sights:

engine.execute(sights.delete())

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (1,"ELBPHILARMONIE","https://de.wikipedia.org/wiki/Elbphilharmonie","HAM")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (2,"SCHLOSSTURM","https://de.wikipedia.org/wiki/Schlossturm_(Düsseldorf)","DUS")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (3,"MARIENPLATZ","https://de.wikipedia.org/wiki/Marienplatz_(München)","MUC")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (4,"MAINTOWER","https://de.wikipedia.org/wiki/Main_Tower)","FRA")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (5,"LONDONEYE","https://de.wikipedia.org/wiki/London_Eye","LHR")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (6,"EIFFELTOWER","https://de.wikipedia.org/wiki/Eiffelturm","CDG")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (7,"ANNEFRANKHOUSE","https://en.wikipedia.org/wiki/Anne_Frank_House","AMS")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (8,"AMALIENBORG","https://en.wikipedia.org/wiki/Amalienborg","CPH")')

engine.execute('INSERT INTO "sights" '
               '(id, name,wikilink,airport_id) '
               'VALUES (9,"SCHOENBRUNN","https://en.wikipedia.org/wiki/Schoenbrunn_Palace","VIE")')
