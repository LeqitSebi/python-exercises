import random

with open("engmix.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def gen_text(word_count):
    output = ""
    i = 0
    while i < word_count:
        rnd = random.randint(0, 84000)
        output += content[rnd] + " "
        i += 1
    return output


def remove_doubles(string, list):
    i = 1
    for word in list:
        if word == string:
            list.remove(word)
            i += 1
    print(string + ": " + str(i))
    return list


def list_and_printfreq(word_count):
    sentence = gen_text(word_count)
    print("original sentence: " + sentence)
    list = []
    for words in sentence:
        list.append(words)
    while len(list) > 0:
        i = 0
        word = list[i]
        list.remove(word)
        list = remove_doubles(word, list)


print(list_and_printfreq(5))
