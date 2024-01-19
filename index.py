import requests

api_key = "b005303fb1b5163d9a7d30df0743db84"

params = {
    "api_key": api_key,
    "language": "pt-BR",
    "page" : 1
}

def getGenres(params):
    url_genre = "https://api.themoviedb.org/3/genre/movie/list"
    try:
        response = requests.get(url_genre, params=params)
        response.raise_for_status() 

        return response.json()["genres"]
    
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"


def getFilmsAll(params):
    url_film = "https://api.themoviedb.org/3/movie/popular"
    try:
        response = requests.get(url_film, params=params)
        response.raise_for_status()

        return response.json()["results"]
    
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"

def listGenres(generos):
    print("Gêneros")
    for i in generos:
        print(f"{i['id']} - {i['name']}")
    return ''

generos = getGenres(params)
filmes = getFilmsAll(params)
id_genero = 0

print(listGenres(generos))
entrada = input('Selecione o id do genero: ')

for i in generos:
    if i['name'] == entrada:
        id_genero = i['id']
        break

for k in filmes:
    if id_genero in k['genre_ids']:
        print(k['title'])