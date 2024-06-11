filename = "myfile.txt"

with open(filename, 'r') as file:
    ascii_codes = file.readlines()

text = ""
for code in ascii_codes:
    code = code.strip()
    character = chr(int(code)) # asscii code to sybol
    text += character

print("decodetext: ", text)