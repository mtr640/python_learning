from math import *

s = eval(input())
a, b, c = s[0], s[1], s[2]


if a == 0:
 if b == 0:
     if c == 0:
      print("mnogo")
     else:
      print("net")
 else:
     print(-c/b) 
else:
  if b == 0:
    print("+-",sqrt(-c/a)) if -c/a > 0 else print("net")
  else:
   d = b**2-4*a*c
   if d > 0:
    if a > 0:
     print((-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a))
    else:
     print((-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a))
   elif d == 0:
    print(-b/(2*a))
   elif d < 0:
    print("net")