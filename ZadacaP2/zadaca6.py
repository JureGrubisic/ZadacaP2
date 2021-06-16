def unatrag(s):
    if len(s)==0:
        return s
    else:
        return unatrag(s[1:]) + s[0]

s=input("Unesite rijec: ")

print(unatrag(s))


