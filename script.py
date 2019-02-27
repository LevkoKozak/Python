test_list = [1, 2, 4, 1, 2, 7, 9, 4, 0, 1, 1]


def get_list_sum(list):
    sum = 0

    for x in list:
        sum += x

    return sum


list_sum = get_list_sum(test_list)

list_average = list_sum / len(test_list)

print('The sum of random list is: ' + str(list_sum))
print('The average of random list is: ' + str(round(list_average, 2)))