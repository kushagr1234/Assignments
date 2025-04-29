#factorial


# 0!-->1
# 1!-->1 * 0!= 1*1
# 2!-->2 * 1!=2
#3!-->6
#4!-->24

p=int(input("Enter a number:\t"))

def factorial(n):
    if  n < 2:
        return 1
    else:
        return n * factorial(n-1)

result=factorial(p)
print("Factorial of",p,"is:\t",result)
