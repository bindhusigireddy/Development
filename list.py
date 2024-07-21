a=[2,3,4,5,6]
for i in range(len(a)):
    a[i] +=2
print(a)

b=list(map(lambda a:a+2, a))
print(b)