list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Указанный список: ')
print(list)
list_length = len(list)
sum_elements = 0
for i in range(list_length):
    sum_elements = sum_elements + list[i]
    print('Сумма всех элементов в списке', sum_elements)
