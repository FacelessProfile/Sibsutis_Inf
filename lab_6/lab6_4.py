n = int(input())
i=0
otstup=0
for x in range(n):
    i+=1
    print("   "*(n-otstup),"#"*(x+i))
    otstup+=1
print("   "*n,"#",)
