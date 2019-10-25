import random
for i in range(3):
    name = input("enter name ")
    myanmar = random.randint(50, 101)
    print("Myanmar=" , end="")
    print(myanmar)
    eng = random.randint(50, 101)
    print("English=", end="")
    print(eng)
    pro = random.randint(50, 101)
    print("Programming=", end="")
    print(pro)
    if myanmar > 39 and eng > 39 and pro > 39:
        ans = 'pass'
        avg = myanmar + eng + pro
        average = avg / 3
        c = 0
        if average >= 65:
            ans += ' with credit'
        if myanmar >= 80:
            c += 1
        if eng >= 80:
            c += 1
        if pro >= 80:
            c += 1
        if c == 3:
            ans += ' and All D'
        if c == 2:
            ans += ' and 2 D'
        if c == 1:
            ans += ' and 1 D'
        print(ans)
    else:
        print('fail')
