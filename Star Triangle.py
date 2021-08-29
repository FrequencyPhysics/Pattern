rows = 5
t = rows - 1
while t >= 0:
    b = 0
    while b < t:
        print('', end=' ')
        b += 1
    k = t
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    t -= 1
