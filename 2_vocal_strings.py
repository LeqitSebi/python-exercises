import random
characters = ['a', 'e', 'i', 'o', 'u']
output = []


def string_gen():
    random.shuffle(characters)
    if check_doubles(''.join(characters), output)!=0:
        output.append(''.join(characters))

def check_doubles(string, list):
    for word in list:
        if word == string:
            return 0


while len(output) <120:
    string_gen()

print(output)

