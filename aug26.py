'''n=int(input("n:"))
match n:
    case 1:
        print("spider man")
    case 4:
        print("iron man")
    case 7:
        print("bat man")
    case 3:
        print("shanthi mann")
    case _:
        print("hanuman")'''

op=input("enter the operator\n+\t-\t*\t/\noption")
if op in '+-*/':
    a=int(input('a:'))
    b=int(input('b:'))
    match op:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)
        case _:
            print(a/b)
else:
    print('invalid operator')
    
    
    
      


