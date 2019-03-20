sentence = "Ich heiße Sebastian und bin 15 Jahre alt."
all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '.',
             '?']
chars = []


def remove_doubles(char, list):
    i = 0
    for word in list:
        if word == char:
            list.remove(word)
            i += 1
    print(char + ": " + str(i))
    return list


def occurency(sentence):
    print(sentence)
    sentence = sentence.lower()
    i = 0
    for char in sentence:
        chars.append(char)
    while i <= 42:
        remove_doubles(all_chars[i], chars)
        i += 1


print(occurency(sentence))
