from flask import Flask 
from flask_cors import CORS
from scrape_weather_data import scrape_weather_data

app = Flask(__name__)
CORS(app)

@app.route("/api/weather_data")
def weather_data():
	return scrape_weather_data()

app.run()
