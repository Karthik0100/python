a = input("enter the no : ")
b = len(a)
a = int(a)
t = a
s = 0
while (t>0):
    d = t % 10
    s = s+(d**b)
    t = t//10
if (a==s):
    print("armstrong no")
else:
    print("not armstrong no")
