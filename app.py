import requests
import tkinter as tk
from tkinter import messagebox, simpledialog

api_key = "b005303fb1b5163d9a7d30df0743db84"

params = {
    "api_key": api_key,
    "language": "pt-BR",
    "page": 1
}

def getGenres(params):
    url_genre = "https://api.themoviedb.org/3/genre/movie/list"
    try:
        response = requests.get(url_genre, params=params)
        response.raise_for_status()
        return response.json()["genres"]
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"

def getFilmsByGenre(params, genre_id):
    url_films_by_genre = f"https://api.themoviedb.org/3/discover/movie"
    try:
        params["with_genres"] = genre_id
        response = requests.get(url_films_by_genre, params=params)
        response.raise_for_status()
        return response.json()["results"]
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"

def listGenres(generos):
    genre_str = "\n".join([f"{i['id']} - {i['name']}" for i in generos])
    return f"Gêneros\n{genre_str}"

def listByGenre(entrada, filmes):
    film_titles = [i['title'] for i in filmes if entrada in i['genre_ids']]
    return "\n".join(film_titles)

def showMessage(msg):
    messagebox.showinfo("Informação", msg)

def showMessageInput(title, message):
    input_dialog = simpledialog.askstring(title, message)
    return input_dialog

def on_select():
    entrada = entry.get()
    if entrada == '0':
        showMessage('Obrigado por utilizar!')
        root.quit()
    elif any(entrada == str(i['id']) or entrada.lower() == i['name'].lower() for i in generos):
        while True:
            filmes = getFilmsByGenre(params, int(entrada) if entrada.isdigit() else None)

            text.delete('1.0', tk.END) 

            text.insert(tk.END, f'Página {params["page"]}\n\n')

            if entrada.isdigit():
                text.insert(tk.END, listByGenre(int(entrada), filmes))
            else:
                for i in generos:
                    if i['name'] == entrada:
                        id_genero = i['id']
                        break
                text.insert(tk.END, listByGenre(id_genero, filmes))

            next_page = showMessageInput("Proxima pagina", "\n1 - Próxima página\n0 - Sair.")
            if next_page == '1':
                params['page'] += 1
            elif next_page == '0':
                showMessage('Obrigado por utilizar!')
                root.quit()
                break
            else:
                showMessage('Opção inválida. Tente novamente.')
                root.quit()
                break
    else:
        showMessage('Gênero não encontrado!\nVerifique o que foi digitado e tente novamente')

generos = getGenres(params)
id_genero = 0

root = tk.Tk()
root.title("Aplicação de Filmes")

root.geometry("600x800") 

label = tk.Label(root, text=listGenres(generos))
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Selecionar", command=on_select)
button.pack()

text = tk.Text(root, height=100, width=500)
text.pack()

root.mainloop()