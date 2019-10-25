import random

com = random.randint(0, 1)
com_m = 1000
u_m = 1000
ans = 'y'
print("Player Amount:", end="")
print(u_m)
print("Computer Amount:", end="")
print(com_m)
while ans == 'y':
    amount = int(input("Enter Amount: "))
    if amount <= u_m:
        player = int(input("Enter hard or tail ( 1/0)"))
        print('*****************')
        if player == 1:
            print("You: ", end="")
            print("Head")
        else:
            print("You: ", end="")
            print("Tail")
        if com == 1:
            print("Computer: ", end="")
            print("Head")
        else:
            print("Computer: ", end="")
            print("Tail")
        print('*****************')
        if com == player:
            print("<<<  Win  >>>")
            print('*****************')
            print("Player Amount:", end="")
            u_m += amount
            print(u_m)
            print("Computer Amount:", end="")
            com_m -= amount
            print(com_m)

        else:
            print("<<<  Lose  >>>")
            print('*****************')
            print("Player Amount:", end="")
            u_m -= amount
            print(u_m)
            print("Computer Amount:", end="")
            com_m += amount
            print(com_m)
        print('****************************************')

    else:
        print('Money have no availabe!')
        print('----------------------------')
    if u_m == 0:
        print("<<<  Game Over  >>>")
        break
    if com_m == 0:
        print("<<<   Computer have no more money. Thanks For Playing   >>>")
        break
    ans = input("Any more y or n?")
    print('-----------------------------------------------')
