# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>9:
#         val=1
#     print( )

# n=int(input())
# val=n
# if val>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print( )

# n=int(input())
# val=n
# if val>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print( )

# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>9:
#         val=1
#     print( )

# n=int(input())
# val=65
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>90:
#         val=65
#     print( )

# n=int(input())
# val=90
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print( )

# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>9:
#         val=1
#     print( )

# n=int(input())
# val=n
# if val>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print( )

# n=int(input())
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#         if val>9:
#            val=1
#     print( )

# n=int(input())
# val=n
# if val>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print( )

# n=int(input())
# for i in range(n):
#     val=65
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#         if val>90:
#            val=65
#     print( )

n=int(input())
for i in range(n):
    val=n+64
    if val>90:
        val=90
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
        if val<65:
           val=90
    print( )


