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
	 'make' : 'Audi', 
	 'model' : 'R8',
	 'year' : '2017',
	 'engine' : 'V10',
	 'engine displacement' : '5.2L',
	 'horsepower' : '542hp',
	 'torque' : '294lb-ft'
	},
	
	{'id' : '4', 
	 'make' : 'Bentley', 
	 'model' : 'Mulsanne',
	 'year' : '2017',
	 'engine' : 'V8',
	 'engine displacement' : '6.8L',
	 'horsepower' : '498hp',
	 'torque' : '555lb-ft'
	},
	
	{'id' : '5', 
	 'make' : 'McLaren', 
	 'model' : '650S Spider',
	 'year' : '2017',
	 'engine' : 'V8',
	 'engine displacement' : '3.8L',
	 'horsepower' : '632hp',
	 'torque' : '369lb-ft'
	},
	
	{'id' : '6', 
	 'make' : 'Mazda', 
	 'model' : 'RX7',
	 'year' : '1994',
	 'engine' : 'R2',
	 'engine displacement' : '1.3L',
	 'horsepower' : '255hp',
	 'torque' : '217lb-ft'
	},
	
	{'id' : '7', 
	 'make' : 'Rolls-Royce', 
	 'model' : 'Ghost',
	 'year' : '2017',
	 'engine' : 'V12',
	 'engine displacement' : '6.6L',
	 'horsepower' : '555hp',
	 'torque' : '424lb-ft'
	},
	
	{'id' : '8', 
	 'make' : 'Subaru', 
	 'model' : 'BRZ',
	 'year' : '2017',
	 'engine' : 'Flat 4',
	 'engine displacement' : '2.0L',
	 'horsepower' : '197hp',
	 'torque' : '111lb-ft'
	},
	
	{'id' : '9', 
	 'make' : 'Toyota', 
	 'model' : 'Celica',
	 'year' : '2005',
	 'engine' : 'I4',
	 'engine displacement' : '1.8L',
	 'horsepower' : '180hp',
	 'torque' : '130lb-ft'
	},
	
	{'id' : '10', 
	 'make' : 'Chevrolet', 
	 'model' : 'Camaro',
	 'year' : '1977',
	 'engine' : 'V8',
	 'engine displacement' : '5.7L',
	 'horsepower' : '165hp',
	 'torque' : '264lb-ft'
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
