number = int(input('Введите число:'))
k = 0
for i in range(2, number // 2+1):
    if (number % i ==0):
        k = k+1
    if (k <=0):
        print('Число простое')
    else:
        print('Число не является простым')