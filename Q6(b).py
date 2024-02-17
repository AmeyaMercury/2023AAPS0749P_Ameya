#Q6(b)
n=5
l1=[]
for i in range(n):
    for j in range(2*n+1):
        if j in range(n-i,n+i+1):
            print("*",end='')
        elif j==n+i+1:
            print("\n",end='')
            break
        else:
            print(" ",end='')
for i in range(n):
    for j in range(2*n+1):
        if j in range(i+1,2*n-i):
            print("*",end='')
        elif j==2*n-i:
            print("\n",end='')
            break
        else:
            print(" ",end='')
