from flask import Flask, render_template
import requests, json 

app = Flask(__name__)

@app.route('/')
def index():
    url='https://ghibliapi.herokuapp.com/Films/'
    respuesta = requests.get(url)
    peliculas = json.loads(respuesta.text) 
    return render_template("index.html", peliculas=peliculas) 

app.run(debug=True)   
