import requests as requests
from flask import Flask, render_template, flash, request, session
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
import http.client
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Qwerty123!'


miasta = ['Krakow', 'Gdansk', 'Warszawa',  'Poznan', 'Wroclaw']
@app.route('/')
def index():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": "Krakow,pl"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "17049ea5b4msh589f52157007bcfp122cb8jsna38ff77f582b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    data = json.loads(data)
    temp = round(float(data['main']['temp']) - 273.15, 1)
    icon = data["weather"][0]["icon"]
    clouds = data['clouds']['all']
    wind = data['wind']['speed']
    humidity = data['main']['humidity']
    print(data)

    return render_template('index.html', data=data, temp=temp, icon=icon, clouds=clouds, wind=wind, humidity=humidity, miasta=miasta)


@app.route('/pogoda', methods=['POST'])
def searchContact():
    searchCriteria = request.form['searchCriteria']
    print(searchCriteria)
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": searchCriteria + ",pl"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "17049ea5b4msh589f52157007bcfp122cb8jsna38ff77f582b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    data = json.loads(data)
    temp = round(float(data['main']['temp']) - 273.15, 1)
    icon = data["weather"][0]["icon"]
    clouds = data['clouds']['all']
    wind = data['wind']['speed']
    humidity = data['main']['humidity']
    print(data)

    return render_template('index.html', data=data, temp=temp, icon=icon, clouds=clouds, wind=wind, humidity=humidity,
                           miasta=miasta)

if __name__ == '__main__':
    app.run(debug=True)