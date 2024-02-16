#Q3
l1=[1,7.8,9,0,34,2,1,-9,9,127,127,100,101,99]
l2=l1
a=max(l1)
while a in l2:
    l2.remove(a)
    
print(max(l2))
