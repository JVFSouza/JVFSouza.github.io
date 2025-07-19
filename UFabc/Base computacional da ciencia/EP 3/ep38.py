import math

a = float(input())
b = float(input())
c = float(input())

s = a/2 + b/2 + c/2
A1 = s(s-b)(s-c)(s-a)
print(A1)
Area = math.sqrt(A1)
print(Area)
print('%.2f' % Area)