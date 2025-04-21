x=int(input('Enter your first number:\t'))
y=int(input('Enter your second number:\t'))
z=input('Enter the operator you want (+,-,*,/):\t ')

if z=='+':
    print(x+y)
elif z=='-':
    print(x-y)
elif z=='*':
    print(x*y)
elif z=='/':
    print(x/y)
else:
    print('NONE')

print('THANK YOU!!')