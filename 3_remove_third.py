nums = [1,2,3,4,5,8]


def remove_and_print(list):
    while len(list) > 2:
        i = 1
        for item in list:
            if i % 3 == 0:
                list.remove(item)
                print(item)
            i += 1
    return list


print(remove_and_print(nums))
