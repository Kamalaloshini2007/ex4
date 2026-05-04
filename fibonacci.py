def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
a=int(input("enter the first number:"))
print("fibonacci series of",a,"is\n")
for i in range(a):
    print(fibonacci(i),end=" ")
