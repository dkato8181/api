from flask import Flask,jsonify, abort, make_response, request
from ireporter import app

successResponse = {"status" : None,"data" : []}
errorResponse = {"status" : None,"error" : ""}


@app.route('/', methods=['GET'])
def baseUrl():
	return "hello"

@app.route('/v1/red-flags', methods=['GET'])
def getRedflags():
	pass

@app.route('/v1/red-flags/<red-flag-id>', methods=['GET'])
def getRedflag():
	pass 

@app.route('/v1/red-flags', methods=['POST'])
def create_red_flag():
	res = {"status" : 200, 
			"data" : [{
				"id" : 1,
				"message" :  "Created red-flag record"
			}]
		}from flask import Flask, jsonify, abort, make_response, request
from ireporter import app
import datetime
import json

incidents = [
	{
		"id" : 1,
		"createdOn" : datetime.datetime(2018, 11, 17),  
		"createdBy" : 2,
		"type" : "red-flag",
		"location" : json.dumps({"lat": "0.3260416", "long": "32.5976064"}),
		"status" : "draft",
		"Images" : [],
		"Videos" : [],
		"comment" : "Police wants me to pay money to follow up my case"
	},
	{
		"id" : 2,
		"createdOn" : datetime.datetime(2018, 11, 22),  
		"createdBy" : 2,
		"type" : "red-flag",
		"location" : json.dumps({"lat": "0.3560416", "long": "32.5956064"}),
		"status" : "draft",
		"Images" : [],
		"Videos" : [],
		"comment" : "Chairman solicites bribes from residents"
	},
	{
		"id" : 3,
		"createdOn" : datetime.datetime(2018, 11, 19),  
		"createdBy" : 2,
		"type" : "intervention",
		"location" : json.dumps({"lat": "1.3260416", "long": "32.5976064"}),
		"status" : "rejected",
		"Images" : [],
		"Videos" : [],
		"comment" : "No medical supplies in hospital"
	},
	{
		"id" : 4,
		"createdOn" : datetime.datetime(2018, 11, 30),  
		"createdBy" : 2,
		"type" : "red-flag",
		"location" : json.dumps({"lat": "0.3260541", "long": "32.595464"}),
		"status" : "resolved",
		"Images" : [],
		"Videos" : [],
		"comment" : "Clerk wants money for his signature"
	}
]

users = [
	{
		"id" : 1, 
		"firstname" : "Kato",
		"lastname" : "David",
		"othernames" : "",
		"email" : "davidk35@gmail.com",
		"phoneNumber" : "0752477539",
		"username" : "davidk", 
		"registered" : datetime.datetime(2018, 11, 15),
		"isAdmin" : True,
	},
	{
		"id" : 2, 
		"firstname" : "Hamala",
		"lastname" : "Paul",
		"othernames" : "John",
		"email" : "hpaul@gmail.com",
		"phoneNumber" : "0771477539",
		"username" : "pham", 
		"registered" : datetime.datetime(2018, 11, 15),
		"isAdmin" : False,
	},
	{
		"id" : 3, 
		"firstname" : "Assimwe",
		"lastname" : "Aggrey",
		"othernames" : "Muhumza",
		"email" : "assim@gmail.com",
		"phoneNumber" : "0792477539",
		"username" : "aggrey", 
		"registered" : datetime.datetime(2018, 11, 15),
		"isAdmin" : False,
	}
]

successResponse = {"status" : None,"data" : []}
errorResponse = {"status" : None,"error" : ""}

@app.route('/', methods=['GET'])
def baseUrl():
	return "hello"

""" Fetch all red-flag records """
@app.route('/v1/red-flags', methods=['GET'])
def getRedflags():
	data = []
	for incident in incidents:
		if incident["type"] == "red-flag":
			data.append(incident)

	successResponse['status'] = 200
	successResponse["data"] = data
	response = jsonify(successResponse)
	return response

""" Fetch a specific red-flag record """
@app.route('/v1/red-flags/<int:incident_id>', methods=['GET'])
def getRedflag(incident_id):
	data = []
	for incident in incidents:
		if incident["id"] == incident_id:
			data.append(incident)

	successResponse['status'] = 200
	successResponse["data"] = data
	response = jsonify(successResponse)
	return response

""" Create a red-flag record """
@app.route('/v1/red-flags', methods=['POST'])
def create_red_flag():
	print(incidents[-1]["id"])
	new_id = incidents[-1]["id"] + 1
	new_incident = {
		"id" : new_id,
		"createdOn" : request.json.get("createdOn"),  
		"createdBy" : request.json.get("createdBy"), 
		"type" : "red-flag",
		"location" : request.json.get("location"), 
		"status" : "draft",
		"Images" : [],
		"Videos" : [],
		"comment" : request.json.get("comment"), 
	}
	incidents.append(new_incident)
	data = {
		"id": new_id,
		"message": "Created red-flag record"
	}
	successResponse['status'] = 200
	successResponse["data"] = data
	
	return jsonify(successResponse)

""" Edit the location of a specific red-flag record """
@app.route('/v1/red-flags/<int:incident_id>/location', methods=['PATCH'])
def editRedflagLocation(incident_id):
	location = request.json.get("location")
	for incident in incidents:
		if incident["id"] == incident_id:
			incident["location"] = location
			break
	data = {"id": incident_id, "message": "Updated red-flag record's location"}
	successResponse['status'] = 200
	successResponse["data"].append(data)
	return jsonify(successResponse)

@app.route('/v1/red-flags/<int:incident_id>/comment', methods=['PATCH'])
def editRedflagComment(incident_id):
	comment = request.json.get("comment")
	for incident in incidents:
		if incident["id"] == incident_id:
			incident["comment"] = comment
			break
	data = {"id": incident_id, "message": "Updated red-flag record's comment"}
	successResponse['status'] = 200
	successResponse["data"].append(data)
	return jsonify(successResponse)

@app.route('/v1/red-flags/<int:incident_id>', methods=['DELETE'])
def deleteRedflagRecord(incident_id):
	for incident in incidents:
		if incident["id"] == incident_id:
			incidents.remove(incident)
			break
	data = {"id": incident_id, "message": "red-flag record has been deleted"}
	successResponse['status'] = 200
	successResponse["data"] = data
	return jsonify(successResponse)


if __name__ == '__main__':
	app.run(debug=True, port=8080)
	return jsonify(res)

@app.route('/v1/red-flags/<red-flag-id>/location', methods=['PATCH'])
def editRedflagLocation():
	pass

@app.route('/v1 /red-flags/<red-flag-id>/comment', methods=['PATCH'])
def editRedflagComment():
	pass

if __name__ == '__main__':
	app.run(debug=True, port=8080)
