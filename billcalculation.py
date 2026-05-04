def getinput(n):
    l=[]
    for i in range(n):
        i_name=input("enter item name:")
        quantity=int(input("enter quantity:"))
        price=float(input("enter price:"))
        l.append((i_name,quantity,price))
    return l
def subtotal(l):
    s=[]
    for i in range(0,len(l)):
        sub=l[i][1]*l[i][2]
        s.append(sub)
    return s
def total(l):
    t=0
    for i in range(0,len(s)):
        t=t+s[i]
    print("total:",t)
    if t>=3000:
        d=t*(10/100)
        t=t-d
        print("after discount:",t)
    else:
        d=0
        t=t+d
        print("after discount:",t)
    g=t*(5/100)
    t=t+g
    print("GST:",g)
    print("after GST applied:",t)
n=int(input("enter no of items:"))
r=getinput(n)
print("items:",r)
s=subtotal(r)
print("subtotal:",s)
total(s)
