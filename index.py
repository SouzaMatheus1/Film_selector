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

def listByGenre(entrada, filmes):
    for i in filmes:
            if entrada in i['genre_ids']:
                print(i['title'])


generos = getGenres(params)
id_genero = 0

print(listGenres(generos))
entrada = input('Selecione o id ou nome do genero ou 0 para sair: ')
if entrada == '0':
    print('Obrigado por utilizar!')
elif any(entrada == str(i['id']) or entrada.lower() == i['name'].lower() for i in generos):
    while True:
        filmes = getFilmsAll(params)

        print(f'\nPágina {params["page"]} \n')

        if entrada.isdigit():
            listByGenre(int(entrada), filmes)
        else:
            for i in generos:
                if i['name'] == entrada:
                    id_genero = i['id']
                    break
            listByGenre(id_genero, filmes)

        next_page = input("\n1 - Próxima página\n0 - Sair.\n")
        if next_page == '1':
            params['page'] += 1
            continue
        elif next_page == '0':
            print('Obrigado por utilizar!')
            break
        else:
            print('Opção inválida!\nVerifique e tente novamente.')
else:
    print('Gênero não encontrado!\nVerifique o que foi digitado e tente novamente')