from pathlib import Path

path = Path("Unit-3/Lesson2/programming.txt") # copy relative path
path.write_text("I love Python!!")
contents = path.read_text() # save current text of file
contents += "\nJava is pretty good too" # add new text
path.write_text(contents) # write updated text back
contents = path.read_text()
contents += "\nHere is some\ttabbed\ttext"
path.write_text(contents)

# Homework is 10-4 and 10-5 on page 192
# 10-5 Clarification: Quit when user types "q"