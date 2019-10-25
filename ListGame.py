import random
use_data=['G','B','Y','R']
c_data=[]
ans=''
delete=''
u_data=input("Enter ( G or B or Y or R) = ")
user_data=u_data.split(' ')

for i in range(4):
    c_data.append(use_data[random.randint(0,3)])
print('Computer: ',c_data)
print('User: ',user_data)
delete_data=[]

for i in range(len(user_data)):
    if user_data[i]==c_data[i]:
        ans+='1'
        delete_data.append(i)

temp=[]
for j in range(len(user_data)):
    if j not in delete_data:
        for k in range(len(c_data)):
            if k not in delete_data:
                if k not in temp:
                    if user_data[j]==c_data[k]:
                        ans+='0'
                        temp.append(k)
                        break

print(ans)