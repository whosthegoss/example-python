import requests

def my_api():
    response = requests.get("http://nix-linux.local:3000/cars")

    print(response.json())

my_api()