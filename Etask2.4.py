l=[]
for i in range(1,100):
    if (i%3==0) and (i%2==0):
        l.append(str(i))

print(','.join(l))