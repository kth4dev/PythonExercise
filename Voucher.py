total=0
for i in range(3):
    user_input = input("Enter :")
    one = ''
    ans = 1
    for k in range(len(user_input)):
        if user_input[k].isdigit():
            one += user_input[k]
            if k < len(user_input) - 1:
                if not (user_input[k + 1].isdigit()):
                   ans*=int(one)
                   one=""
            if k==len(user_input)-1:
                if user_input[k].isdigit():
                   ans*=int(one)
                   one=""
    print('price =',ans)
    total+=ans
print("total amount =",total)