line = str(input())
s = 0
g = 0
vse_g = ['a', 'e', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count = 0
for i in line:
    if i in vse_g:
        g += 1
    else:
        s += 1
print('Гласных:', g, '\nСогласных:', s)