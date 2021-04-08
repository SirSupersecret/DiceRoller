import sys
import random

n = 100000

if len(sys.argv) > 0:
  if sys.argv[1].isnumeric():
    n = int(sys.argv[1])
  else:
    print("argument not an integer")

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for x in range(n):
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

print("relative frequencies:")
print("1: " + str(a/n))
print("2: " + str(b/n))
print("3: " + str(c/n))
print("4: " + str(d/n))
print("5: " + str(e/n))
print("6: " + str(f/n))
print("")
print("n = " + str(n))
