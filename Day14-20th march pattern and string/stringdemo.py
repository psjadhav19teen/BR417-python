#string=set of literals(digit,alphabets,special charcater) and enclosed with quotes
#it is squence,order,indexing follows,slicing and immutable(not modifyable) data type

#empty string

# s=""
# print(s,type(s))
# msg=str()
# print(msg,type(msg))

# s="a"
# print(s,type(s))
# s1="python is easy"
# print(s1,type(s1))
# s2="3534654"
# print(s2,type(s2))
# features="""dynamic
# easy
# case-sensitive
# """
# print(features,type(features))

# name=input("enter name=")
# print(name,type(name))
# percentage=str(77.878) #explicit conversion
# print(percentage,type(percentage))


#Accessing/reading string elements via index
#syntax:- stringname[indexnumber]
#Two type of index-
# 1) Postive-start with 0 left to right
# 2) Negative-start with -1 right to left

msg="welcome"
print(msg)
#postive index
# print("first char=",msg[0]) #w
# print("second char=",msg[1]) #e
# print(len(msg)) #7
# print("moddle char=",msg[len(msg)//2]) #c
# print("second last char=",msg[len(msg)-2]) #m
# print("last char=",msg[len(msg)-1]) #e

#negative index
print("first char=",msg[-len(msg)]) #w
print("second char=",msg[-len(msg)+1]) #e
print(len(msg)) #7
print("moddle char=",msg[-len(msg)//2]) #c
print("second last char=",msg[-2]) #m
print("last char=",msg[-1]) #e