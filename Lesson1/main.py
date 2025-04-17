from pathlib import Path
# from pathlib module, import Path class

path = Path("Unit-3/Lesson1/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
num_digits = f"Digits: {len(pi_string)-1}"
num_decimals = f"Decimals: {len(pi_string)-2}"
print(num_digits)
print(num_decimals)