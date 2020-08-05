import sys
import re
from time import time

def contar_vocales(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u']
    return len([x for x in palabra if x in vocals])

def contar_conso(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u']
    return len([x for x in palabra if x not in vocals])


# 3470, 43448, 1190, 78229
# 136243, 146917, 1026
# text_name = input("texto: ")
text_name = "bible.txt"
text_file = open(text_name, "r")
text = text_file.read()
text = re.sub(r'[^a-zA-Z0-9 \n\.]', '', text)
data = re.findall(r'\b[a-zA-z]+\b', text)
print(data)
comands = input("secuencia: ").split()
print(comands)
while comands:
    temp_data = data
    if comands[0][0] == 'a':
        temp_data = [w for w in temp_data if len(w) == int(comands[0][1:])]
        print(temp_data)
    elif comands[0][0] == 'b':
        temp_data = [w for w in temp_data if contar_vocales(w) == int(comands[0][1:])]
        print(temp_data)
    elif comands[0] == 'c':
        temp_data = [w for w in temp_data if contar_vocales(w) > contar_conso(w)]
        print(temp_data)
    elif comands[0] == 'c-':
        temp_data = [w for w in temp_data if contar_vocales(w) < contar_conso(w)]
        print(temp_data)
    elif comands[0] == 'd':
        temp_data = [w for w in temp_data if w[0] in ['a', 'e', 'i', 'o', 'u']]
        print(temp_data)
    elif comands[0] == 'd-':
        temp_data = [w for w in temp_data if w[0] not in ['a', 'e', 'i', 'o', 'u']]
        print(temp_data)
    elif comands[0] == 'e':
        temp_data = [w for w in temp_data if w[-1] in ['a', 'e', 'i', 'o', 'u']]
        print(temp_data)
    elif comands[0] == 'e-':
        temp_data = [w for w in temp_data if w[-1] not in ['a', 'e', 'i', 'o', 'u']]
        print(temp_data)

    comands = input("secuencia: ").split()
