#we are going to creat the strong password with python

#for this we should first import random

import random

lowers="qwertyuiopasdfghjklzxcvbnm"
uppers="QWERTYUIOPASDFGHJKLZXCVBNM"

numbers="1234567890"
symbols="!@#$%^&*(){}[]"

all=lowers+uppers+numbers+symbols

lenght=40

password="".join(random.sample(all,lenght))
print("password:",password)