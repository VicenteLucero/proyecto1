
import sys
import re
import threading
from timeit import default_timer as timer

def contar_vocales(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u']
    return len([x for x in palabra if x.lower() in vocals])


def contar_conso(palabra):
    consonantes = ['b','c','d','f','g','h','j','k','l','m','n','r','p','q','r','s','t','v','w','x','y','z']
    return len([x for x in palabra if x.lower() in consonantes])


def sequences(ind, word, comands, data):
    global frases
    frase = word
    ind = int(ind)+1
    for c in comands:
        if ind == len(dict):
            return
        if c in data[ind][1]:
            frase += ' '+data[ind][0]
            ind += 1
        else:
            return
    frases.append(frase)

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text_name = input("text: ")
start = timer()
comands = open('comands.txt', 'r').read().split('\n')
dict = {}
frases = []
count = 0
text = re.sub(r'[^a-zA-Z \n]', '', open(text_name, encoding="utf8").read())
text = re.sub(r'\n', ' ', text)
data = re.findall(r'[a-zA-Z]+\b', text)

for w in data:
    vocal = contar_vocales(w)
    conso = contar_conso(w)
    comandos = []
    comandos.append('a{}'.format(vocal + conso))
    comandos.append('b{}'.format(vocal))
    if vocal > conso:
        comandos.append('c')
    else:
        comandos.append('c-')
    if w[0] in vocales:
        comandos.append('d')
    else:
        comandos.append('d-')
    if w[-1] in vocales:
        comandos.append('e')
    else:
        comandos.append('e-')
    dict[count] = [w, comandos]
    count += 1
work = True
count = 1
while work:
    for c in comands:
        c = c.split()
        first = c.pop(0)
        temp_data = [word for word in dict if first in dict[word][1]]
        for i in temp_data:
            sequences(i, dict[i][0], c, dict)
    print(len(frases))
    output = open('salida{}.txt'.format(count), 'w')
    count += 1
    output.write(str(len(frases)) + '\n')
    for f in frases:
        output.write(f+'\n')
    output.close()
    end = timer()
    print(end - start)
    work = input('next?: ')
    if work != 'y':
        work = False
    else:
        comands = open('comands.txt', 'r').read().split('\n')
        frases = []
