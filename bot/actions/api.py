import requests
import os
token = os.environ['DEFENSORIA_TOKEN']

url = 'https://online.defensoria.sp.gov.br/autoatendimento/v1/estrutura'
headers = {'x-access-token': token}

def get_city_data(city='São Paulo'):
    params = (('nomeCidade', city),)
    response = requests.get(url, headers=headers, params=params)
    return response.json()
