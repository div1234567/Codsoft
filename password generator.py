import random as r
import string as s
var=int(input("enter the length of password: "))

fuse=s.ascii_uppercase
fuse1=s.ascii_lowercase
fuse2=s.digits
fuse3=s.punctuation
total_characters=fuse+fuse1+fuse2+fuse3
list1=[]
for i in range(0,var):
    list1.append(r.choice(total_characters))
    
 
password=''.join(list1)
    
print(f"Here is your password: {password}")
