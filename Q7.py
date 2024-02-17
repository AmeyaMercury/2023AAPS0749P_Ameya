a=int(input("Enter hour:"))
b=int(input("Enter minutes:"))
a=(a%12)*30
d=b//2
b=b*6
c=abs(a-b)+d
if c>180:
    c=c-180
print(c)
