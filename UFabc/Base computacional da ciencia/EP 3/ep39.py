import math

x1 = float(input())
x2 = float(input())

y1 = float(input())
y2 = float(input())

dist = math.sqrt( (x1 - y1 )**2 + (x2 - y2)**2 )

print('%.3f' % dist)