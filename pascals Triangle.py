n = int(input("Enter n Value \n"))
i = 1
x = (n/2)
while i <= n:
    j = 1
    print(' ' * (n - i), end="  ")
    while j <= i:
        if i > 9:
            s = str(i)
            a = min(s)
            print(a, end="  ")
        else:
            print(i, end="  ")
        j = j + 1
    print('\n')
    i = i + 1