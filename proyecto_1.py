import sys
import re
import threading


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
            if len(word2) != int(com[1:]):
                # print('retornado')
                return
        elif com[0] == 'b':
            if int(com[1:]) != contar_vocales(word2):
                # print('retornado')
                return
        elif com == 'c':
            if contar_vocales(word2) < contar_conso(word2):
                return
        elif com == 'c-':
            if contar_vocales(word2) > contar_conso(word2):
                return
        elif com == 'd':
            if word2[0] not in vocales:
                return
        elif com == 'd-':
            if word2[0] in vocales:
                return
        elif com == 'e':
            if word2[-1] not in vocales:
                return
        elif com == 'e-':
            if word2[-1] in vocales:
                return
        frase = frase + ' ' + word2
        # print(frase)
    frases.append(frase)

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
comands = open('comands.txt', 'r').read().split('\n')
# print(comands)
text_name = "enwik8.txt"
text_file = open(text_name, encoding="utf8")
text = text_file.read()
text = re.sub(r'[^a-zA-Z \n]', '', text)
text = re.sub(r'\n', ' ', text)
data = re.findall(r'[a-zA-Z]+\b', text)
frases = []
for c in comands:
        c = c.split()
        print(c)
        first = c.pop(0)
        # print(first)
        for i in range(0, len(data)):
            word = data[i]
            if first[0] == 'a':
                if len(word) != int(first[1:]):
                    continue
            elif first[0] == 'b':
                if int(first[1:]) != contar_vocales(word):
                    continue
            elif first == 'c':
                if contar_vocales(word) < contar_conso(word):
                    continue
            elif first == 'c-':
                if contar_vocales(word) > contar_conso(word):
                    continue
            elif first == 'd':
                if word[0] not in vocales:
                    continue
            elif first == 'd-':
                if word[0] in vocales:
                    continue
            elif first == 'e':
                if word[-1] not in vocales:
                    continue
            elif first == 'e-':
                if word[-1] in vocales:
                    continue
            sequences(i, word, data, c)
            # thread = threading.Thread(target=sequences, args=(i, word, data, comands))
            # thread.start()
        #print(len(frases))
        # comands = []
        #print()
print(len(frases))
