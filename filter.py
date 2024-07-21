a=[1,3,9,7,5]
b=[]
for i in a:
    if i>3:
        b.append(i)
print(b)

c=list(filter(lambda x:x>3, a))
print(c)
