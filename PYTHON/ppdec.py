# n=int(input())
# res=''
# while n!=0:
#     rem=n%8
#     res+=str(rem)
#     n=n//8
# rev=res[::-1]
# print(rev)

# n=int(input())
# p=1
# res=0
# while n!=0:
#     rem =n%10
#     res +=rem*p
#     p*=8
#     n//=10
# print(res)


# n=int(input())
# res=0
# p=1
# while n!=0:
#     rem=n%16
#     res=res+rem*p
#     n=n//16
#     p*=10
# print(res)

# n=int(input())
# p=1
# res=0
# while n!=0:
#     rem=n%10
#     res+=rem*p
#     p*=16
#     n//=10
# print(res)

n=int(input())
res=0
p=1
while n!=0:
    rem=n%2
    res=res+rem*p
    n=n//2
    p*=10
print(res)

n=int(input())
p=1
res=0
while n!=0:
    rem=n%10
    res+=rem*p
    p*=2
    n//=10
print(res)
