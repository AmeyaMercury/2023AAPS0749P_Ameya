#Q6(a)
n=5
for i in range(n):
    for j in range(n+1):
        if j==n:
            print("\n")
        elif i+j>n-2:
            print(i+j-n+2,end='')
        elif i+j<=n-2:
            print(" ",end='')
        
        
        
