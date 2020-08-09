import sys
import re
import time
import multiprocessing
from threading import Thread


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
        if ind == len(data) - 1:
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

def ProcessComand(c):
    c2 = c.split()
    print(c2)
    first = c2.pop(0)
    # print(first)
    for i in range(0, len(data)):
        word = data[i]
        if first[0] == 'a':
            if len(word) == int(first[1:]):
                sequences(i, word, data, c2)
                continue
        elif first[0] == 'b':
            if int(first[1:]) == contar_vocales(word):
                sequences(i, word, data, c2)
                continue
        elif first == 'c':
            if contar_vocales(word) > contar_conso(word):
                sequences(i, word, data, c2)
                continue
        elif first == 'c-':
            if contar_vocales(word) <= contar_conso(word):
                sequences(i, word, data, c2)
                continue
        elif first == 'd':
            if word[0] in vocales:
                sequences(i, word, data, c2)
                continue
        elif first == 'd-':
            if word[0] not in vocales:
                sequences(i, word, data, c2)
                continue
        elif first == 'e':
            if word[-1] in vocales:
                sequences(i, word, data, c2)
                continue
        elif first == 'e-':
            if word[-1] not in vocales:
                sequences(i, word, data, c2)
                continue
        # print(word)

if __name__ == '__main__':
    start = time.perf_counter()
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text_name = "enwik8.txt"
    text_file = open(text_name, encoding="utf8")
    text = text_file.read()
    text = re.sub(r'[^a-zA-Z \n]', '', text)
    text = re.sub(r'\n', ' ', text)
    data = re.findall(r'[a-zA-Z]+\b', text)

    frases = []

    threads = []
    comands = open('comands.txt', 'r').read().split('\n')
    for c in comands:
        threads.append(Thread(target=ProcessComand(c)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')
    print(f'Answer: {len(frases)}')
