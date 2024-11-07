# n=int(input())
# m=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(m,end=" ")
#             m+=1
#         else:
#             print("*",end=" ")
#         if m>9:
#            m=1
#     print( )

# n=int(input())
# for i in range(n):
#     m=1
#     s=1
#     for j in range(n):
#         if i>j:
#             print(m,end=" ")
#             m+=1
#         elif i<j:
#             print(s,end=" ")
#             s+=1
#         else:
#             print("*",end=" ")
#         if m>9:
#            m=1
#         if s>9:
#            s=1
#     print( )

# n=int(input())
# m=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=(n-1):
#             if i%2==0:
#                print(m,end=" ")
#             else:
#                print("*",end=" ")
#         else:
#             print(" ",end=" ")  
#     if i%2==0:    # if row is even then only increment the value of m.
#         m+=1
#         if m>9:
#             m=1    
#     print( )

n=int(input())
m=1
for i in range(n):
    for j in range(n):
        if i>=j:
            if i%2==0:
               print(m,end=" ")
            else:
               print("*",end=" ")
        else:
            print(" ",end=" ")  
    if i%2==0:    # if row is even then only increment the value of m.
        m+=1
        if m>9:
            m=1    
    print( )

