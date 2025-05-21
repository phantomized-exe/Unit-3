'''
start a virtual enviroment
pip install pillow (*NOT* PIL, I know it's weird)
pip install requests
On windows, tkinter is installed by default
'''

import requests
import io # needed to process the bytes that we will download the sprite in
from pathlib import Path # if you want to create a cache of sprites
import tkinter as tk
from PIL import Image, ImageTk # allows us to manipulate images
import random


# ---------- constants ----------
POKE_COUNT = 1025                              # adjust if new pokemon come out (is this a thing?)
API_URL    = "https://pokeapi.co/api/v2/pokemon/{}" # we will use {} later for substitution with .format()
POKE_ID = random.randint(0,POKE_COUNT)

# ---------- create our own dictionary of pokemon info ----------
def rand_poke():
    POKE_COUNT = 1025                              # adjust if new pokemon come out (is this a thing?)
    API_URL    = "https://pokeapi.co/api/v2/pokemon/{}" # we will use {} later for substitution with .format()
    POKE_ID = random.randint(0,POKE_COUNT)
    request = requests.get(API_URL.format(POKE_ID),timeout=10)
    request.raise_for_status()
    data = request.json()
    formatted_data = {
        "id":           POKE_ID,
        "name":         data["name"].title(),
        "types":        [t["type"]["name"] for t in data["types"]], 
        "weight_kg":    data["weight"]/10,
        "sprite":       data["sprites"]["front_default"]
        
    }
    return formatted_data

# ---------- GUI Stuff ----------

root = tk.Tk()
root.title("Random Pokémon Generator")
root.geometry("400x400")
root.resizable(False, False)
        
formatted_data = rand_poke()
img_bytes = requests.get(formatted_data["sprite"],timeout=10).content
pillow_image = Image.open(io.BytesIO(img_bytes)).resize((200,200))
tk_image = ImageTk.PhotoImage(pillow_image)

def show_pokemon():
    formatted_data = rand_poke()
    img_bytes = requests.get(formatted_data["sprite"],timeout=10).content
    pillow_image = Image.open(io.BytesIO(img_bytes)).resize((200,200))
    tk_image = ImageTk.PhotoImage(pillow_image)
    try:
        root.img_label.photo = tk_image
        root.img_label.config(image=tk_image)

        types = " / ".join(formatted_data["types"]).title() # convert dict to string
        root.info_label.config(
            text=f"{formatted_data['name']}  (#{formatted_data["id"]})\n"
                    f"Type: {types}\n"
                    f"Weight: {formatted_data['weight_kg']} kg"
        )
    except Exception as e:
        root.info_label.config(text=f"Error: {e}")
        
# widgets
root.img_label = tk.Label()
root.img_label.pack(pady=(10, 5))
root.info_label = tk.Label(font=("Helvetica", 12), justify="center")
root.info_label.pack(pady=(0, 10))

root.btn = tk.Button(
    text="Show Pokémon",
    font=("Helvetica", 14, "bold"),
    command = show_pokemon
)
root.btn.pack(fill="x", padx=20, pady=5)



root.mainloop()
