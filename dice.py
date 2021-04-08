import random

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for x in range(40):
  r = random.randint(1,6)
  if r == 1:
    a = a + 1
  elif r == 2:
    b = b + 1
  elif r == 3:
    c = c + 1
  elif r == 4:
    d = d + 1
  elif r == 5:
    e = e + 1
  elif r == 6:
    f = f + 1

print("1: " + str(a))
print("2: " + str(b))
print("3: " + str(c))
print("4: " + str(d))
print("5: " + str(e))
print("6: " + str(f))

print("sum: " + str(a+b+c+d+e+f))
