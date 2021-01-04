# в двумерном массиве b[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j -1] + a[i][j + 1]
s = input()
a = []
b = []
# ввод двумерного массива с условием окончание(вери юзфул)
while (s != 'end'):
    a.append(list(map(int, s.split())))
    b.append(list(map(int, s.split())))
    s = input()

n = len(a[0]) # длина по горизонтали
m = len(a) #длина по вертикали
for i in range(len(a)):
    dwn = i + 1
    for j in range(len(a[i])):
        rght = j + 1
        if ((dwn == m) & (rght == n)): #если правая нижняя
            b[i][j] = a[i-1][j] + a[i][j-1] + a[len(a) - 1][0] + a[0][len(a[i]) - 1]
            #b = верхняя + левая + правая(1) + нижняя
        elif ((dwn == m)  & (rght != n)):#если нижний ряд
            b[i][j] = a[i-1][j] + a[0][j] + a[i][j + 1] + a[i][j - 1]
            #b = в + н + п + л
        elif ((rght == n) & (dwn != m)):
            b[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0]
            #b = в + н + л + п
        else:
            b[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j -1] + a[i][j + 1]   
    
for i in range(len(b)):
    print(*b[i])
