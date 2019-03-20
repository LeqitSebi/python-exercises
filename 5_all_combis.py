characters1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = []


def num_gen():
    i = 0
    j = 0
    k = 0
    while i < 10:
        while k < 10:
            while j < 10:
                outstring = str((characters1[i] * 100) + (characters2[k] * 10) + characters3[j])
                if (len(outstring) == 2):
                    outstring = "0" + outstring
                if (len(outstring) == 1):
                    outstring = "00" + outstring
                print(outstring)
                j += 1
            j = 0
            k += 1
        j = 0
        k = 0
        i += 1


print(num_gen())
