a = []
for i in range(3):
    a.append([])
    for j in range(3):
            a[i].append(int(input("matrix=")))
print("matrix 1=",a)

b=[]
for g in range(3):
    b.append([])
    for k in range(3):
        b[g].append(int(input("matrix=")))
print("matrix 2=",b)

c=[]
for l in range(3):
    c.append([])
    for n in range(3):
        c[l].append(0)
for i in range(3):
    for j in range(3):
        c[i][j]+=a[i][n]*b[n][j]
print("multiplied=",c)