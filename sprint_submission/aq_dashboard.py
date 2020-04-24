
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify 
import openaq
import requests 

api = openaq.OpenAQ()

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

# model 
class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f"(datetime ' + self.datetime + ' ) (value ' + str(self.value) + ')"

def load_api():
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    date_vals = []
    for result in body['results']:
        date = result['date']['utc']
        val = result['value']
        date_vals.append((date, val))
    return date_vals

@APP.route('/')
def root():
    """Base view."""
    data = load_api()
    for datetime, value in data:
        record = Record(datetime=datetime, value=value)
        DB.session.add(record)
        DB.session.commit()
    table_data = Record.query.filter(Record.value >= 10).all()
    return str([(record.datetime, record.value) for record in table_data])
    
@APP.route('/refresh')
def refresh():
    """
    refresh and replace existing data.
    """
    DB.drop_all()
    DB.create_all()
    data = load_api()
    for datetime, value in data:
        record = Record(datetime=datetime, value=value)
        DB.session.add(record)
        DB.session.commit()
    
    return 'DB Refreshed'