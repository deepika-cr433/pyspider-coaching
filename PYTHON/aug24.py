'''n=input("enter the gender:")
if n in ['male','female','others']:
    m=int(input('age:'))
    if ((n in ['male','others']) and (m>=18 and m<=65)) or (n == 'female' and (m>=18 and m<=65)) :
        print("eligible for voting")
    else:
        print("invalid age")
else:
    print("invalid gender")'''

op = input("enter operator\n+\t-\t*\t/\noption:")
if op in '+-*/':
    a=float(input("a:"))
    b=float(input("b:"))
    if op=='+':
        print(a+b)  
    elif op=='-':
        print(a-b)
    elif op=='*':
        print(a*b)
    else:
        print(a/b)
else:
    print('invalid operator')


