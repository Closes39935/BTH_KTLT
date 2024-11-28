print("Nguyen Van An")
print("Msv:235752021610082")
str=input("Enter a sting:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] +=1
    else:
        dict[n] = 1
print (dict)        
