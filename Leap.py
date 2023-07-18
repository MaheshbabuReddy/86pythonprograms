y = int(input('Enter the Year'))
if y%400 == 0 and y%100 == 0:
    print( y ,'This is year is leap year')
elif y%4 == 0 and y%100 !=0: 
    print(y , 'is a leap year')
else:
    print(y, 'is not a leap year')
    