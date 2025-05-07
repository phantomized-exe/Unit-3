import json
import urllib.request

POKE_URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = urllib.request.urlopen(POKE_URL) # get response from URL

pokemon = json.load(response) # converts API JSON response to dict
print(pokemon['forms'][0]['url'])
print(pokemon['types'][0]['type']['name'])
print(pokemon['abilities'][0]['ability']['name'])
print(pokemon['abilities'][1]['ability']['name'])

for ability in pokemon['abilities']:
    print(f"Name: {ability['ability']['name']}")

for stat in pokemon['stats']:
    print(f"Name: {stat['stat']['name']} \t Value: {stat['base_stat']}")

# expected HW solution
for move in pokemon['moves']:
    print(f"Move: {move['move']['name']}")

# fancy, numbered homework solution
for index,move in enumerate(pokemon['moves']):
    print(f"Move {index+1}: {move['move']['name']}")

'''
How does this work?

Enumerate creates an object of the form

((0, item),(1, item),(2, item),(3, item), ... )

for all items in some iterable like a list. 

This allows us to essentially access and use the index 
like a variable through tuple unpacking

When I write index,item
it takes each tuple and assigns the first part to
the variable index and the second part to item.
'''