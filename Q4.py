#Q4
l1=[1,2,3,4,2,2,5,6,7,7,9,0,8,5,3,5,4,7]
l2=[]
for i in range(len(l1)):
    if l1[i] in l2:
        pass
    else:
        l2.append(l1[i])
print(l2)
