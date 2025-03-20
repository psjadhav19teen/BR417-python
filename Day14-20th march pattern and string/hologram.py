#Hologram Box
# for i in range(1,4):
#     for j in range(1,4):
#         if i==1 or i==3 or j==1 or j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#Hologram Box
# row=int(input("enter row="))
# column=int(input("enter column="))
# for i in range(1,row+1):
#     for j in range(1,column+1):
#         if i==1 or i==row or j==1 or j==column:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''
Q.17 Zig-Zag Number Pattern
Input: n = 5

1  2  3  4  5  
10 9  8  7  6  
11 12 13 14 15  
20 19 18 17 16  
21 22 23 24 25  
'''
# row=int(input("enter row="))
# count=0
# for i in range(1,row+1):
#     for j in range(1,row+1):
#             if i%2==0:
#                 print(count,end=" ")
#                 count-=1
#             else:          
#                 count+=1
#                 print(count,end=" ")
                
#     count+=row
#     print()

'''
Q.18 Print Fibonacci numbers in a n × n matrix.
Example (n = 3):
0   1   1  
2   3   5  
8   13  21  
'''
row=int(input("enter row="))
a=0
b=1
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==1 and j==1:
            print(a,end=" ")
        elif i==1 and j==2:
            print(b,end=" ")
        else:
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    print()

