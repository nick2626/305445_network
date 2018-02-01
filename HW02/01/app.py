from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json,time
from datetime import datetime,date
from werkzeug.datastructures import FileStorage

app = Flask (_name_)

api = Api(app)

def calculate_age(born):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))

parser = reqparse.RequestParser()
parser.add_argument('birthdate')
parser.add_argument('image', type=FileStorage, location='files')

class Home(Resource):
	def get(self):
		return {"message":"'./born' to calculate age or './image' to upload image "}

class Birth(Resource):
	def get(self):
		return {"message":"Plese sent 'birthdate' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		birthdate = args['birthdate']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(calculate_age(datetime_object))
		return {"birthdate":birthdate,"age":age}
class Image(Resource):
	def get(self):
		return {"message":"Plese sent 'image' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		image = args['image']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"Upload success"}
		

api.add_resource(Home,'/')
api.add_resource(Birth,'/born')
api.add_resource(Image,'/image')
if _name_ == '_main_':
	app.run(host='0.0.0.0',port=5000)