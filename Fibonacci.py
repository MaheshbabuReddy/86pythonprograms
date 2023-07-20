n=int(input('Enter the number'))
a=0
b=1
i=0
while i<=n:
    c=a+b
    i+=1
    print(c)
    a=b
    b=c
    