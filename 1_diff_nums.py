nums = [1, 4, 2, 23, 5, 5]


def checknums(toBeChecked, checkList):
    for number in checkList:
        if number == toBeChecked:
            return 0


def diff_nums(numbers):
    newlist = []
    for number in nums:
        if checknums(number, newlist) == 0:
            return "es gibt doppelte Zahlen"
        else:
            newlist.append(number)
    return "es gibt keine doppelten Zahlen"


print(diff_nums(nums))
