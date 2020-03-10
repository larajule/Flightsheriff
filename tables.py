

from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=True)
    name = Col('Name')
    image = Col('Image')
    lat = Col('Lat')
    long = Col('Long')
 
