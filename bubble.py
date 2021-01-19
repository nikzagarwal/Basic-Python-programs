a=[1,5,7,4,28,6,242,54]
for i in range(len(a)):
   for j in range(len(a)):
       if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)
