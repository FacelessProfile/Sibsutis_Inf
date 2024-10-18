import math
def count(n):
    second=n-2
    return((n-second)*(10.5) + second*4)
n=int(input())
if (abs(n) ==n):
    print(f'{n} год жизни собаки эквивалентен {count(n)} человеческим')
else:
    print("incorrect input")
