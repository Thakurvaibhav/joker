from flask import Flask
import requests
from constants import NAME_URL,JOKE_URL

app = Flask(__name__)

@app.route("/")
def serve():
  # Getting names 
  name_response = requests.get(url = NAME_URL)
  name_data = name_response.json()
  first_name = name_data['name']
  last_name = name_data['surname']

  #Getting Joke
  joke_response = requests.get(url = JOKE_URL)
  joke_data = joke_response.json()
  joke = joke_data['value']['joke']
  joke=joke.replace("John", first_name)
  joke=joke.replace("Doe", last_name)
  joke=joke + "\n"
  
  return joke


if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0')
