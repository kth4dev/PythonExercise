import os

ans = 'y'
while ans == 'y':
    s = int(input("Strat= "))
    e = int(input("End= "))
    for mul in range(1, 13):
        for a in range(s, e + 1):
            print(a, '*', mul, '=', a * mul, "\t", end="")
        print()
    ans = input('yes or no')
    os.system('cls')

