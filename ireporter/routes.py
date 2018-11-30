from flask import Flask,jsonify, abort, make_response, request
from ireporter import app

@app.route('/', methods=['GET'])
def abc():
	return "hello"
	
@app.route('/v1/red-flags', methods=['POST'])
def create_red_flag():
	res = {"status" : 200, 
		"data" : [{
			"id" : 1,
			"message" :  "Created red-flag record"
		}]
		}

	return jsonify(res)


if __name__ == '__main__':
	app.run(debug=True, port=8080)