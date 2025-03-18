'''
for i in range(5):
    print("*")
'''

'''
for i in range(5):
    print("*",end=" ")
'''
'''
for i in range(3): 
    print("*"*3) #incorrect way of writing
'''

#WAP to show box pattern take rows and column from user
'''
row=int(input("enter rows="))
column=int(input("enter column="))
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()
'''

'''
row=int(input("enter rows="))
column=int(input("enter column="))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(i,end="")
    print()
'''    
'''
output
1111
2222
3333
'''

'''
row=int(input("enter rows="))
column=int(input("enter column="))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(j,end="")
    print()
'''
 
'''
output
enter rows=3
enter column=3
123
123
123
'''


'''
row=int(input("enter rows="))
column=int(input("enter column="))
count=0
for i in range(1,row+1):
    for j in range(1,column+1):
        count+=1
        print(count,end=" ")
    print()
'''
#output
'''
enter rows=3
enter column=3
1 2 3
4 5 6
7 8 9
'''

#WAP to 1 to 10 multiplication table
row=int(input("enter rows="))
column=int(input("enter column="))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(i*j,end=" ")
    print()