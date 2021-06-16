import re

#ime.prezime@fpmoz.sum.ba
reg1="[a-z]+\.[a-z]+@fpmoz\.sum\.ba"

while 1:
    mail=input("Unesi mail: ")
    x=re.findall(reg1, mail)
    if x:
        break
print("Uspješno unesen mail.")

#iprezimex@sum.ba
#euid=input("Unesi euid: ")
reg2="ˇ[a-z]{1}[a-z]+\d?@sum\.ba$"
while 1:
    eduid=input("Unesi eduId: ")
    y=re.findall(reg2, eduid)
    if y:
        break
print("Uspješno unesen eduId.")

    

