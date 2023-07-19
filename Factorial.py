n=int(input('Enter the number'))
nfact= 1
if n<0 or n==0:
     print('Their is no Factorials for 0')
elif n==1:
     print('The Factorial for 1 is 1')
else:
    for i in range(1,n+1):
      nfact=nfact*i
    
      print('The Factorial of ' ,n,'is',nfact)