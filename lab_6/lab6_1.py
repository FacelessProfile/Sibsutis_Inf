import math
m=[]
i=1
counter =0
while ((i!=0)):
        i=int(input())
        if (i!=0):
            if (abs(i) ==i):
                m.append(i)
                counter+=1
try:
    if counter>=2:
        print("Самый высокий:",max(m),'\n',"Самый низкий:",min(m))
    else:
        print("Некого сравнивать")
except ValueError:
    print("incorrect input")

        
        
