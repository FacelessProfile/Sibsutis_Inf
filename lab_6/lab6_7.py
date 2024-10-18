n=input("input bin:")
dec=0
for i in range(len(n)):
    dec+=int(n[i])*(2**(len(n)-(i+1)))
print(dec)

#10110
#n[0] =1
#1 * 2**(len(n)-(i+1))
