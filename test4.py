s = int(input())
summa=buff=full=0
while s != 0:
 buff = min(buff+s, 0)
 full = max(full, buff)
 s = int(input())
print(full)