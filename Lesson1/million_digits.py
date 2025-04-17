from pathlib import Path
# from pathlib module, import Path class

path = Path("Unit-3/Lesson1/pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthdate = input("Birthdate(mmddyy): ")

# standard/basic solution
if birthdate in pi_string:
    print("Found your birthday!")
else:
    print("Sorry :( ")

# more advanced solution
try:
    location = pi_string.index(birthdate)
    print(f"I found your birthday at the {location-1} digit of pi")
except ValueError:
    print("Your birthday is not in the first million digits of pi")