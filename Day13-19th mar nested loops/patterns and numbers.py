#Right incremental Triangle

# row=int(input("enter row="))
# for i in range(1,row+1):
#     for k in range(row-i):
#         print(end="  ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#Right decremental Triangle

# row=int(input("enter row="))
# for i in range(row,0,-1):
#     for k in range(row-i):
#         print(end="  ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


#Hill incremental Triangle

# row=int(input("enter row="))
# for i in range(1,row+1):
#     for k in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


#Hill decremental Triangle

# row=int(input("enter row="))
# for i in range(row,0,-1):
#     for k in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#Diamond 

# row=int(input("enter row="))
# for i in range(1,row+1):
#     for k in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(row-1,0,-1):
#     for k in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


#Hill incremental 1,3,5,7

row=int(input("enter row="))
for i in range(1,row+1):
    for k in range(row-i):
        print(end=" ")
    for j in range(2*i-1):
        print("*",end="")
    print()