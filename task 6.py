slovo = str(input())
a = []
b = []
for i in slovo:
    a.append(i)
    b.append(i)
a.reverse()
# print(b)
# print(a)
if b == a:
    print('Yes')
else:
    print('No')