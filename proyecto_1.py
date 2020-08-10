import sys
import re
import threading
from timeit import default_timer as timer

def contar_vocales(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return len([x for x in palabra if x in vocals])


def contar_conso(palabra):
    vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return len([x for x in palabra if x not in vocals])


def sequences(ind, word, data, comands):
    global vocales
    global frases
    frase = word
    for com in comands:
        # print(com)
        # print(com[1:])
        if ind == len(data)-1:
            return
        ind += 1
        word2 = data[ind]

        if com[0] == 'a':
            if len(word2) == int(com[1:]):
                frase = frase + ' ' + word2
                continue
        elif com[0] == 'b':
            if int(com[1:]) == contar_vocales(word2):
                frase = frase + ' ' + word2
                continue
        elif com == 'c':
            if contar_vocales(word2) > contar_conso(word2):
                frase = frase + ' ' + word2
                continue
        elif com == 'c-':
            if contar_vocales(word2) <= contar_conso(word2):
                frase = frase + ' ' + word2
                continue
        elif com == 'd':
            if word2[0] in vocales:
                frase = frase + ' ' + word2
                continue
        elif com == 'd-':
            if word2[0] not in vocales:
                frase = frase + ' ' + word2
                continue
        elif com == 'e':
            if word2[-1] in vocales:
                frase = frase + ' ' + word2
                continue
        elif com == 'e-':
            if word2[-1] not in vocales:
                frase = frase + ' ' + word2
                continue
        return
    # print(frase)
    frases.append(frase)

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# print(comands)
text_name = input("text: ")
start = timer()
comands = open('comands.txt', 'r').read().split('\n')
text_file = open(text_name, encoding="utf8")
text = text_file.read()
text = re.sub(r'[^a-zA-Z \n]', '', text)
text = re.sub(r'\n', ' ', text)
data = re.findall(r'[a-zA-Z]+\b', text)
frases = []
for c in comands:
        temp_data = data
        c = c.split()
        print(c)
        first = c.pop(0)
        # print(first)
        if first[0] == 'a':
            temp_data = [w for w in range(0, len(data)) if len(data[w]) == int(first[1:])]
        elif first[0] == 'b':
            temp_data = [w for w in range(0, len(data)) if contar_vocales(data[w]) == int(first[1:])]
        elif first == 'c':
            temp_data = [w for w in range(0, len(data)) if contar_vocales(data[w]) > contar_conso(data[w])]
        elif first == 'c-':
            temp_data = [w for w in range(0, len(data)) if contar_vocales(data[w]) <= contar_conso(data[w])]
        elif first == 'd':
            temp_data = [w for w in range(0, len(data)) if data[w][0] in vocales]
        elif first == 'd-':
            temp_data = [w for w in range(0, len(data)) if data[w][0] not in vocales]
        elif first == 'e':
            temp_data = [w for w in range(0, len(data)) if data[w][-1] in vocales]
        elif first == 'e-':
            temp_data = [w for w in range(0, len(data)) if data[w][-1] not in vocales]
        # print(temp_data)
        for i in temp_data:
            sequences(i, data[i], data, c)
            # print(word)
            # thread = threading.Thread(target=sequences, args=(i, word, data, comands))
            # thread.start()
print(len(frases))
output = open('salida.txt', 'w')
output.write(str(len(frases))+'\n')
for f in frases:
    output.write(f+'\n')
output.close()
end = timer()
# print(end - start)
