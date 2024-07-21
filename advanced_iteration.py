first = [[1,2,3],[4,5,6],[1,29]]
# second=[]
# for i in first:
#  second.append(sum(i))
# print(second)

second=list(map(lambda x:sum(x), first))
print(second)
