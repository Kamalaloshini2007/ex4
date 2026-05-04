def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("enter the number:"))
print("the factorial of ",n," is ",factorial(n))
