import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '158010925d0d4da63c30361a4c366668'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# создать нового покемона
body_new_pokemon = {
    "name": "Покемошка",
    "photo": "https://dolnikov.ru/pokemons/albums/322.png"
}
# вывести ответ
response_new_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_new_pokemon)
print(response_new_pokemon.json())

pok_id = response_new_pokemon.json()['id']
print("Id созданного покемона: ", pok_id)

# переименовать созданного покемона
body_new_name = {
    "pokemon_id": pok_id,
    "name": "Сплюха",
    "photo": "https://dolnikov.ru/pokemons/albums/322.png"
}
# вывести ответ
response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.json())

new_name = body_new_name["name"]
print("Новое имя покемона: ", new_name)

# поймать в покебол
body_add_pokeball = {
    "pokemon_id": pok_id
}
# вывести ответ
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json())
print(f'Покемон {new_name} пойман в покебол')


# отправить в нокаут (если живых покемонов 5)
'''body_kill_pokemon = {
    "pokemon_id": "28467"
}
response_kill_pokemon = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_kill_pokemon)
print(response_kill_pokemon.json())
print('Покемон в нокауте')
'''