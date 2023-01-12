import requests
import json


def cars_api():
    response = requests.get("http://nix-linux.local:3000/cars")

    cars_return = json.dumps(response.json()["cars"])
    
    print(cars_return)


def computers_api():
    response = requests.get("http://nix-linux.local:3000/computers")

    computers_return = json.dumps(response.json()["computers"])
    
    print(computers_return)

cars_api()
computers_api()