p=int(input("enter the principal"))
r=int(input("enter the interest rate"))
t=int(input("enter time in year"))
print("the return at the end of {} is {}".format(t,p+p*r/100*t))