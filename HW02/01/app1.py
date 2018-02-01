from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json,time
from datetime import datetime,date

app = Flask (__name__)

api = Api(app)

def calculate_age(born):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))

parser = reqparse.RequestParser()
parser.add_argument('birthdate')

class Birth(Resource):
	def get(self):
		return {"message":"Plese sent 'birthdate' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		birthdate = args['birthdate']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(calculate_age(datetime_object))
		return {"birthdate":birthdate,"age":age}

api.add_resource(Birth,'/HBD')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5008)

