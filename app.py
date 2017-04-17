from flask import Flask, jsonify, request
app = Flask(__name__)

cars = [
	{'id' : '1', 
	 'make' : 'Toyota', 
	 'model' : 'Supra',
	 'year' : '1997',
	 'engine' : 'I6',
	 'engine displacement' : '3.0L',
	 'horsepower' : '320hp',
	 'torque' : '210lb-ft'
	},
	
	{'id' : '2', 
	 'make' : 'Nissan', 
	 'model' : 'Skyline',
	 'year' : '1999',
	 'engine' : 'I6',
	 'engine displacement' : '2.6L',
	 'horsepower' : '276hp',
	 'torque' : '266lb-ft'
	},
	
	{'id' : '3', 
	 'make' : 'Mazda', 
	 'model' : 'RX7',
	 'year' : '1994',
	 'engine' : 'R2',
	 'engine displacement' : '1.3L',
	 'horsepower' : '255hp',
	 'torque' : '217lb-ft'
	}	
]

@app.route('/cars', methods=['GET'])
def returnAll():
    return jsonify({'cars' : cars})

@app.route('/cars/<string:id>', methods=['GET'])
def returnOne(id):
    Cars = [car for car in cars if car['id'] == id]
    return jsonify({'car' : Cars[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)