import re
file = open('raw.data' , 'r' , encoding="utf-8")

text = file.read()
print(text)

file.close()