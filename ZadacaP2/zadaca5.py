def Brojevi(n):
    for i in range(n):
        if i%2==0 or i%2!=0:
            yield i

Br=iter(Brojevi(30))

while 1:
    try:
        print(next(Br))
    except:
        break
