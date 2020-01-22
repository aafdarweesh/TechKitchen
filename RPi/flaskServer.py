from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
import os
import urllib
from time import sleep
import glob



app = Flask(__name__)
#CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

videoDuration = 0
tripDuration = 0
missionOnTheRun = False


@app.route('/', methods=['GET'])
def main():
	return render_template('tripDetails.html')

@app.route('/Data', methods=['GET'])
@cross_origin()
def tripDetails():
	f= open("./Data.txt","r")
	data = f.read()
	f.close()
	data = data.split(", ")
	print(type(data))

	return jsonify({'status' : str(data[0]), 'display' : str(data[1])})


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
