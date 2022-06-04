# with open('names.txt', 'w+') as file:
#     names_list = file.readlines()
#     new_list = []
#     for word in names_list:
#         if word == 'Johan' or word == 'Johan\n':
#             word = 'Alex'
#
#
#
#     print(names_list)

# 1
def write_avg(filename_1, filename_2):
    with open(filename_1, 'r') as firstfile, open(filename_2, 'w') as secondfile:
        f1 = firstfile.readlines()
        arr = []
        for n in f1:
            arr.append(n.strip())

        total = 0
        for num in arr:
            total += int(num)
        avg = total / len(arr)

        secondfile.write(str(avg))


# write_avg('first.txt', 'second.txt')

# 2
def find_min_max_positive_int(filename_1, filename_2):
    with open(filename_1, 'r') as firstfile, open(filename_2, 'w') as secondfile:
        f1 = firstfile.readlines()
        arr = []
        for n in f1:
            if int(n) > 0 and int(n) % 2 == 0:
                arr.append(int(n.strip()))

        newline = f'{min(arr)}\n{max(arr)}'
        secondfile.write(newline)


# find_min_max_positive_int('first.txt', 'second.txt')

#3
