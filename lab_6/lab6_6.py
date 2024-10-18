import random

def cont():
    ans = input("Хотите продолжить? [y/n]")
    if ans.lower()=="y":
        return 1
        counter =0
    else:
        return 0

global counter
counter=0
secret = random.randint(1, 10)
print("Хорошо, я загадал число. Попробуй его отгадать")
while 1:
    num = int(input(f"Попытка {counter}:"))
    if num == secret:
        print("Поздравляю! Вы угадали!")
        if (cont()):
            secret = random.randint(1, 10)
            print("Хорошо, я загадал число. Попробуй его отгадать")
            continue
        else:
            print("Спасибо за игру!")
            break
    else:
        print("Нее, ты не угадал. Попробуй снова",'\n')
        counter+=1
        if num<secret: print("Подсказка: заданное число больше")
        else: print("Подсказка: заданное число меньше")
