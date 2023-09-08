# print Hello, World!
#print("Hello, World!")

# a=hex(97)
# print(a)
# b=a.split("0x")
# print(b)
# c=int("b",base=16)
# print(c)
# d=chr(c)
# print(d)
x="abcdabc"
kode=[]
for k in x:
    a=ord(k)
    b=hex(a)
    kode.append(b)
c="".join(kode)

print(c)
d=c.split("0x")
d=d[1:len(x)]
print(d)

for p in d:
    e=int(p,base=16)
    print(e)




