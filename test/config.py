#VAMOS PRECISAR DA API KEY UMA CREDENCIAL

import requests #Biblioteca para fazer requisições HTTP
from pprint import pprint # Biblioteca para imprimir de forma mais legível a resposta da API

API_KEY = "919145263fdc4b4d95a232914262909"

API_link = "http://api.weatherapi.com/v1/current.json"

parameters = {
    "key": API_KEY,
    "q": "São Paulo ",# CIDADE PARA QUAL QUEREMOS A COLETA DE DADOS 
    "lang": "pt" #LINGUAGEM EM QUE QUEREMOS A RESPOSTA
}
#ARMAZENANDO A RESPOTA DA API EM UMA VARIAVEL
response = requests.get(API_link, params=parameters)

pprint(response.json())

if response.status_code == 200:
    data = response.json()
    location = data['location']['name']
    country = data['location']['country']
    temperature_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print()
    print(40 * "=")
    print("Dados do clima obtidos com sucesso!")
    print(40 * "-")
    print(f"Localização: {location}, {country}")
    print(40 * "-")
    print(f"Temperatura: {temperature_c}°C")
    print(40 * "-")
    print(f"Condição: {condition}")
    print(40 * "=")

else:
    print("Erro ao obter dados da API:", response.status_code)