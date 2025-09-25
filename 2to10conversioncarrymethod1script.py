#introduction
introduction = print("This is a base i(2-10) to base o(2-10) calculator, please enter the value below")

#input
i = int(input("i: "))
if i < 2 or i > 10:
  print("Error")
  exit()
else:
  next
o = int(input("o: "))
if o < 2 or o > 10:
  print("Error")
  exit()
else:
  next
value = int(input("value: "))

#first stage
dec = 0
pb = 0
while value > 0:
  rpartofvalue = value % 10
  rdpartofaddvalue = rpartofvalue * (pow(i, pb))
  dec = dec + rdpartofaddvalue
  value = value // 10
  pb+=1

#second stage
l = list()
while dec != 0:
  rpartofdec = dec % o
  l.append(rpartofdec)
  dec = dec // o

#print result
l.reverse()
for newdec in l:
  print(newdec, end="")
input()