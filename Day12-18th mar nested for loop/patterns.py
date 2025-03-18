#Left incremental Triangle
'''
row=int(input("enter rows="))
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()

'''
'''
output
enter rows=3
* 
* * 
* * * 
'''
'''
#Left decremental Triangle
row=int(input("enter rows="))
for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

'''
'''
output
enter rows=3
* * * 
* * 
* 
'''

'''
row=int(input("enter rows="))
for i in range(1,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
'''
'''
output
enter rows=3
1 
1 2 
1 2 3 

'''

'''
row=int(input("enter rows="))
for i in range(1,row+1):
    for j in range(i):
        print(i,end=" ")
    print()

'''
'''
output
enter rows=3
1 
2 2 
3 3 3
'''

'''
row=int(input("enter rows="))
count=0
for i in range(1,row+1):
    for j in range(i):
        count+=1
        print(count,end=" ")
    print()
'''
'''
#output
1
2 3
4 5 6
'''

row=int(input("enter rows="))
count=1
for i in range(1,row+1):
    i=count
    for j in range(i): 
        print(i,end=" ")
    count+=1
    print()

