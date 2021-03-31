import json

import requests

URLNAME = 'https://restcountries.eu/rest/v2/name/'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text #retorna uma string
    except:
        print('erro ao acessar banco de dados')

def parsing(resposta):
    try:
        return json.loads(resposta) #transforma a string numa lista

    except Exception as error:
        print('erro ao fazer parsing')
        print(error)

def adicionar_pais(URL):
    nome_pais = input('Vamos aprender mais sobre um pais? Escreva o nome de um pais: ')
    URL += nome_pais
    URL = requisicao(URL)
    return URL

def informacoes_pais(pais):
    a = pais[0]
    print(type(a))
    print('{} ou {}(nome internacional), eh um pais com {} habitantes, a lingua nativa e {},a moeda usada e {}, por fim sua capital eh {}'.format(a['translations']['br'], a['name'], a['population'], a['languages'][0]['nativeName'], a['currencies'][0]['name'],a['capital']))


if __name__ == '__main__':
    while True:
        pais = adicionar_pais(URLNAME) #a funcao pede pro usuario entrar com o nome de um pais e retorna uma string com informacoes do pais
        if pais: #verifica se o pais existe
            pais = parsing(pais) #transforma o pais numa lista
            informacoes_pais(pais)
        else:
            print('>>> pais invalido!')
        pass