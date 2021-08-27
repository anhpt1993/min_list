# determine number in list
def min_list(list):
    min_number = list[0]
    for i in range(len(list)):
        if list[i] < min_number:
            min_number = list[i]
    return min_number

if __name__ == '__main__':
    number = [11, 3, 7, 5, 2]
    print(min_list(number))

