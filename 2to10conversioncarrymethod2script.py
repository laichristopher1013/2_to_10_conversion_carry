#introduction
print("This is a base c1(2-10) to base c2(2-10) calculator, please enter the d(value) below")

#input
c1 = input("c1: ")
if int(c1) < 2 or int(c1) > 10:
  print("Error")
  exit()
else:
  next
c2 = input("c2: ")
if int(c2) < 2 or int(c2) > 10:
  print("Error")
  exit()
else:
  next
d = input("d: ")

#first stage
result = 0
nd = int(d)
nc1 = int(c1)
for i in range(len(d)):
  result += nd % 10 * pow(nc1, i)
  nd = nd // 10

#second stage
nresult = []
nc2 = int(c2)
o = 0
q = 0
while pow(nc2, o) <= result:
  o += 1
o -= 1
while o >= 0:
  while pow(nc2, o) * q <= result:
    q += 1
  q -= 1
  nresult.append(q)
  result -= pow(nc2, o) * q
  o -= 1
  q = 0

#print result
for u in nresult:
  print(u, end = "")
input()