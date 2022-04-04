max1,max2,buff=0,0,0

while s := int(input()):
 if s>max2:
  max1 = max2
  max2 = s
 elif s>max1 and s<max2:
  max1 = s
print(max1) if max1 != 0 else print("NO")