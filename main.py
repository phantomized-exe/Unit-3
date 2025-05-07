import json
import urllib.request

POKE_URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = urllib.request.urlopen(POKE_URL)

pokemon = json.load(response)
print(pokemon['forms'][0]['url'])
print(pokemon['types'][0]['type']['name'])
print(pokemon['abilities'][0]['ability']['name'])
print(pokemon['abilities'][1]['ability']['name'])

for ability in pokemon['abilities']:
    print(f"Name: {ability['ability']['name']}")

for stat in pokemon['stats']:
    print(f"Name: {stat['stat']['name']} \t Value: {stat['base_stat']}")

for move in pokemon['moves']:
    print(f"Name: {move['move']['name']}")