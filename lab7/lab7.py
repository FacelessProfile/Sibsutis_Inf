##text = input("Type text here:\n").split(" ")
##print(text)
##for i in range (len(text)-1):
##    if text[i] == text[i+1]: text[i+1]=""
##print(*text)
########################
##text = input("Type text here:\n").split(" ")
##if len(text)==2:
##    print(*text[::-1])
##else:
##    print("eror")
###########
##text = input("Type text here:\n")
##text=[a+"." for a in text]
##text=' '.join(text)
##print(text[0:-1])
############
##import re
##a = input("Type text here:\n")
##a = re.sub(r"(не плохой)([.,!?])", r"хороший\2", a)
##a = re.sub(r"(не плоха)([.,!?])", r"хороша\2", a)
##a = re.sub(r"(не плохо)([.,!?])", r"хорошо\2", a)
##print(a)
###############
##gl="аеёиоуэюя"
##i = input("Type text here:\n")
##i=i.split("/")
##counter=0
##m=[]
##for k in i:
##    for n in range(len(k)):
##        if k[n].lower() in gl:
##            counter+=1
##    m.append(counter)
##    counter=0
##if m==[5,7,5]: print("Хокку")
##else:
##    if len(i)!=3:
##        print("Не хокку((( должно быть 3 строки")
##    else:
##        print("Не хокку(((")
##################
##msg = input("input ponkripted message:\n ")
##ans = msg[0:-1:2]+msg[1:-1:2][::-1]
##if (msg[-1]=="#") and (msg[:-2].isalpha()):
##    print("DEPONKED MESSAGE:", ans)
##else:
##    print("NEPONOVOE MESSAGE")
#################
##import random as r
##
##options=[]
##
##upLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##lowLetters=upLetters.lower()
##digits="0123456789"
##SpS="!@#$%^&*_-+="
##length = int(input("input length:\n"))
##
##options.append(input("capital needed? y/n:\n"))
##options.append(input("lower needed? y/n:\n"))
##options.append(input("digits needed? y/n:\n"))
##options.append(input("special symbols needed? y/n:\n"))
##
##pas =""
##
##for x in range(len(options)):
##    if options[x].lower() in ["y","yes"]:
##        options[x]=1
##    else:
##        options[x]=0
##total= upLetters*options[0]+lowLetters*options[1]+digits*options[2]+SpS*options[3]
##for i in range(length):
##    pas += r.choice(total)
##print(pas)
###################
i = input("Type text here:\n")
a=i.split("-")[0]
b=i.split("-")[1]
score =b.split(" ")[1]
b=b.replace(score,"")
if score.split(":")[0]>score.split(":")[1]:
    print(a)
else:
    if score.split(":")[0]==score.split(":")[1]:
        print("Ничья")
    else:
        print(b)
    











    
