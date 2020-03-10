from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myairports.db'
app.config['SERVER_NAME'] = 'flightsherif.dnsuser.de'
app.secret_key = "flask rocks!"
db = SQLAlchemy(app)
