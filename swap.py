a=list(map(int,input("enter first array").split()))
b=list(map(int,input("enter second array").split()))
a,b=b,a
print("a is {} and b is {}".format(a,b))