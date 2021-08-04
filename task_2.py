sum_2 = 0
list_1 = []
for num_1 in range(1, 1001, 2):
    list_1.append(num_1 ** 3)
for num_2 in list_1:
    sum_1 = 0
    list_2 = list(str(num_2))
    for number_1 in list_2:
        sum_1 += int(number_1)
    if sum_1 % 7 == 0:
        sum_2 += num_2
print(sum_2)

sum_4 = 0
list_3 = []
for i in list_1:
    list_3.append(i + 17)
for num_3 in list_3:
    sum_3 = 0
    list_4 = list(str(num_3))
    for number_2 in list_4:
        sum_3 += int(number_2)
    if sum_3 % 7 == 0:
        sum_4 += num_3
print(sum_4)



