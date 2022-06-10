import requests


def get_data():
    response  = requests.get('https://rest-api-pract1se.herokuapp.com/api-endpoint').json()
    return response