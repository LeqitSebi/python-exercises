numbers = [1, -1, 0, 5, 6, 7, 8]


def find_triplets(list):
    i = 0
    while i < len(list):
        nums = list
        add = nums[i]
        returner1 = nums[i]
        nums.remove(nums[i])
        i += 1
        j = 0
        while j < len(nums):
            add += nums[j]
            returner2 = nums[j]
            nums.remove(nums[j])
            j += 1
            k = 0
            while k < len(nums):
                add += nums[k]
                returner3 = nums[k]
                k += 1
                if add == 0:
                    print(str(returner1) + ", " + str(returner2) + ", " + str(returner3))


print(find_triplets(numbers))
