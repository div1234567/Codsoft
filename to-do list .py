txt ="welcome to to-do list"
a = txt.center(50,'-')
print(a,"\n")  
list1 = []
msg='''-> Press 1 to add task,
-> Press 2 to view task,
-> Press 3 to update task,
-> Press 4 to remove task,
-> Press 5 to exit.
'''
print(msg)


while True:
    response = int(input("Enter your command:"))
    if(response== 1):
        rabbit=int(input("enter the no. of task:"))
        for i in range(0,rabbit):
            route=input("enter the task:")
            list1.append(route)
        
        print("task has been added.")
            
    elif(response==2):
        for i in range(0,len(list1)):
            print(list1[i])
            
    elif(response==3):
        donkey=int(input("enter index of the task to update:"))
        list1[donkey-1] = input("update a task:")
        
    elif(response==4):
        copper=int(input("Delete the task:"))
        list1.pop(copper-1)
        
    else:
        break;

















