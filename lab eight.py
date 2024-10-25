##i = list(input("Input here:\n"))
##digits=[]
##letters=[]
##for j in i:
##    if j.isdigit():digits.append(j)
##    else:
##        letters.append(j)
##print(f"list1:{digits}\nlist2:{letters}")
################
##i = list(input("Input here:\n"))
##for x in i:
##    for j in i[i.index(x)+1::]:
##        if j>x:
##            print(f"mor {x} is {j}")
################
##m=[]
##lowerAVG=[]
##equalAVG=[]
##higherAVG=[]
##n=int(input("Input here:\n"))
##m.append(n)
##while n!="":
##    n=input("Input here:\n")
##    if n.isdigit(): m.append(int(n))
##print("massiv:",m)
##avg = sum(m)/len(m)
##print("avg:",avg)
##for i in m:
##    if i<avg:
##        lowerAVG.append(i)
##    if i==avg:
##        equalAVG.append(i)
##    if i==avg:
##        higherAVG.append(i)
##print(f"loverAVG:{lowerAVG}")
##print(f"equalAVG:{equalAVG}")
##print(f"higherAVG:{higherAVG}")
####################
m=[]
cnt=0
values = input().split(" ")
for j in range(len(values)):
    values[j]=int(values[j])
values=sorted(values)
height=int(input())
for i in range(len(values)-1):
    if values[i]==values[i+1] == height: cnt+=1
    if values[i]<=height<values[i+1]:
        for x in values[0:i+1]:
            m.append(x)
        m.append(height)
        for l in values[i+1:]:
            m.append(l)
print(m)
print(m.index(height)+cnt+1)
################
##import random as r
##bil=[]
##for x in range(6):
##    bil.append(r.randint(1,50))
##print(bil)
###############
##import random as r
##m=[]
##counter=0
##for i in range(3):
##    m.append(r.choice("OP"))
##    counter+=1
##while set(m[-3:])!=set(m[-3]):
##    m.append(r.choice("OP"))
##    counter+=1
##print(*m,f"(attempts: {counter})")
######################
##n=int(input())
##words=[]
##for x in range(n):
##    words.append(input())
##for i in words:
##    if len(i)>10:
##        print(i[0]+str(len(i[1:-2])+1)+i[-1])
##    else:
##        print(i)
#####################
##n=int(input())
##counter=0
##room=""
##for x in range(n):
##    room=input().split(" ")
##    if int(room[1])-int(room[0])>=2:
##        counter+=1
##print(counter)







        
