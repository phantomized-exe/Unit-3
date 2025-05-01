from pathlib import Path
import json

song_info = {}
song_info["Artist"] = "David Bowie"
song_info["Title"] = "Heroes"
song_info["Release Year"] = 1977
song_info["Modern"] = False

print(song_info)

### Write contents to JSON file ###
path = Path("Unit-3/Lesson4/song_info.json")
contents = json.dumps(song_info) # convert Python dictionary to JSON format
path.write_text(contents) # write to JSON file
print(contents)

## Read content from JSON file ###
contents = path.read_text()
song_info = json.loads(contents) # converts JSON to Python dictionary
print(song_info)

# Homework is 10-11 through 10-14 on page 206