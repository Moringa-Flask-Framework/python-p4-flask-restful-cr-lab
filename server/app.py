#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        records= [plant.to_dict() for plant in Plant.query.all()]
        response= make_response(records, 200)
        return response
    
    #maethod to post data
    def post(self):
        new_record= Plant(
            name= request.form['name'],
            image= request.form['image'],
            price=request.form['price']
        )
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            message= str(e)
        respo_dict= new_record.to_dict()
        response= make_response(respo_dict, 201)
        return response

class PlantByID(Resource):
    def get(self,id):
        record= Plant.query.filter_by(id=id).first().to_dict()
        if record is None:
            response= make_response("No records found for {id}", 400)
            return response
        else:
            response= make_response(record, 200)
            return response
        
api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, "/plants/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
