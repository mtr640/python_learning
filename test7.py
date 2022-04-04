from math import *
s = int(input())
fl=0

for i in range(int((s/2)**(1/3))):
 for j in range(int((s/2-2*i)**(1/3)),int((s-2*i)**(1/3))):
  if (s-(i+1)**3 == (j+1)**3):
   print("YES")
   #print(i+1,j+1)
   fl=1
   break
  #print(i+1,j+1)
 if fl==1:
  break
if fl==0:
 print("NO")