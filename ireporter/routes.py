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
		}
	return jsonify(res)

@app.route('/v1/red-flags/<red-flag-id>/location', methods=['PATCH'])
def editRedflagLocation():
	pass

@app.route('/v1 /red-flags/<red-flag-id>/comment', methods=['PATCH'])
def editRedflagComment():
	pass

if __name__ == '__main__':
	app.run(debug=True, port=8080)