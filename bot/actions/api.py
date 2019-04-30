import requests

url = 'https://online.defensoria.sp.gov.br/autoatendimento/v1/estrutura'
headers = {'x-access-token': '43db84b5147baad505df2412f6303623'}

def get_city_data(city='São Paulo'):
    params = (('nomeCidade', city),)
    response = requests.get(url, headers=headers, params=params)
    return response.json()

#response = get_city_data('São Paulo')
#print(response[0]['nome'])
#print(response[0]['endereco']['logradouro'])
