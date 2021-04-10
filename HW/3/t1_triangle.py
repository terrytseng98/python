Circle Area formula:
Triangle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
@@ -20,3 +19,16 @@
perimeter: 12.000000
Area: 6.000000
"""
a=input("a=?")
b=input("b=?")
c=input("c=?")
a=int(a)
b=int(b)
c=int(c)
p =1/2*(a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if (c<a+b)and(c>b-a):
    print(a+b+c)
    print(area)
else:
    print("can't make a triangle")