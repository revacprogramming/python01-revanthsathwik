hrs = input("Enter Hours:")
h = float(hrs)
rps=input("enter rate:")
r=float(rps)
if (h<=40):
    pay=h*r
elif h>40:
    pay=40*r+(h-40)*r*1.5
print(pay)