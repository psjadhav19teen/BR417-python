# row=int(input("enter row="))
# for i in range(row):
#     for j in range(row):
#         if i==j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

count=1
for i in range(1,7):
    for j in range(1,6):
        if i%2==0:
            if j%2==0:
                print(count,end=" ")
                count+=1
            else:
                print("*",end=" ")
        else:
            if j%2==0:
                print("*",end=" ")
            else:
                print(count,end=" ")
                count+=1
    print()