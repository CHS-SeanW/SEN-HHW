import random

e = int(input('length of password'))
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '123456789'
password = ''
for i in range(e//2):
    password += random.choice(chars) + random.choice(num)
if e // 2 == 0:
    password += random.choice(num)
print(password)
else:
    print('error')

#while a < le:
#    le += 8
#    if le == 8:
#        password += random.choice(chars) and random.choice(num)
#        break
#    else:
#        print('error!')
#        break

    
