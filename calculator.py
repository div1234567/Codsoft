

txt = '''Press + for Addition
Press - for Subtraction
Press * for Multiplication
Press / for Division
'''
print(txt)
var=int(input("enter the number1: "))
var1=int(input("enter the number2: "))
op=input("enter the operation: ")
match op:
    case '+':
        print(var+var1)
    
    case '-':
        print(var-var1)
        
    case '*':
        print(var*var1)
        
    case '/':
        print(var/var1)
        
    case '%':
        print(var%var1)
        