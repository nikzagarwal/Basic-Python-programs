from functools import reduce
a=[1,2,3,4]
sum=reduce(lambda x,y:x+y,a,0)
print(sum)

