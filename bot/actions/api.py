import requests
import os
token = os.environ['DEFENSORIA_TOKEN']

url = 'https://online.defensoria.sp.gov.br/autoatendimento/v1/'
headers = {'x-access-token': token}

def get_city_data(city='São Paulo'):
    new_url = url + 'estrutura'
    params = (('nomeCidade', city),)
    response = requests.get(new_url, headers=headers, params=params)
    return response.json()

def get_cejusc_data(city='São Paulo'):
    new_url = url + 'cejusc'
    params = (('nomeCidade', city),)
    response = requests.get(new_url, headers=headers, params=params)
    return response.json()
