#Q2
l1=['pokemon','origin','rhythm','syndicate','quick']
k=0
l2=[]
for string in l1:
    for j in range(len(string)):
        if string[j] in 'aeiouAEIOU':
            k=k+1
    l2.append(k)
    k=0
a=max(l2)  
for i in range(len(l1)):
    if l2[i]==a:
        print(l1[i])

        
