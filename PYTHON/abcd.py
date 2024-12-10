# n=int(input())
# for i in range(2*n-1):
#      for j in range(n):
#          if j==0 or i==j or i+j==n+1:
#              print("*",end=" ")
#          else:
#             print(" ",end=" ")
#      print()

# n=int(input())
# val=65
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
#     val+=1
#     if val>90:
#         val=65
#     print()

# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#         val+=1
#     if val>9:
#         val=1
#     print()

# n=int(input())
# val=n
# if val>9:
#     val=9
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print()

# n=int(input())
# val=64+n
# if val>90:
#     val=90
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print()

# n=int(input())
# spc=0
# str=2*n-1
# val=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print(val,end=" ")
#         val+=1
#         if val>9:
#            val=1
#     spc+=1
#     str-=2
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (i<n/2 and j<n/2) or (i>=n/2 and j>=n/2):
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j==n-1 or j-i==n-1 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print( )

# n=int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

n = 10
a, b = 0, 1
print("Fibonacci Series:")
print(a, b, end=" ")

for i in range(2, n):
    n3 = a + b
    print(n3, end=" ")
    a = b
    b = n3

