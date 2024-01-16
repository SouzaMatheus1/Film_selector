import requests

api_key = "b005303fb1b5163d9a7d30df0743db84"  # Substitua com a sua chave de API do TMDb
url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": api_key,
    "language": "pt-BR", 
}

def getGenres(params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 

        return response.json()["genres"]

        # Exibe os IDs e nomes dos gêneros
    #     for genre in genres:
    #         print(f"ID: {genre['id']} | Nome: {genre['name']}")

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")


def getFilmsAll(params):
    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()["results"]


print(getGenres(params))
# filmes =  getFilmsAll(params)
# for filme in filmes:
#     if filme["adult"]:
#         print(filme['title'])

