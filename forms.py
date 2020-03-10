
# forms.py
from wtforms import Form, StringField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import airports
class AirportSearchForm(Form):
	startairport = StringField('')
	endairport = StringField('')


