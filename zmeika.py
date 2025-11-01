from colorama import init
init()
from colorama import Fore
import os
from time import sleep
from pynput import keyboard
from random import randint
x = "x "
V = "r"
h = "# "
Apple = "a "
step = 375
field = [[h,h,h,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x],         
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x], 
        [x,x,x,x,x,x,x,x,x,x]] 
def cls():
    os.system("clear")
def printf(f):
    global Apple, x, h, step, score
    cls()
    for r in f:
        for c in r:
            if c == Apple:
                print(Fore.RED + c, end="")
            elif c == x:
                print(Fore.WHITE + c, end="")
            elif c == h:
                print(Fore.GREEN + c, end="")
        print("\n", end="")
    print(Fore.WHITE + f"SCORE: {score}")
    print(Fore.WHITE + f"SPEED: {step//5+1}/75") if step < 375 else print(f"SPEED: 75/75")

def on_press(key):
    global V, field
    try:
        last = key.char
    except AttributeError:
        last = key
    if last == "d":
        v = 'r'
    elif last == "a":
        v = 'l'
    elif last == "w":
        v = 'u'
    elif last == "s":
        v = 'd'
    else:
        v = V
    V = v
def on_release(key):
    if key == keyboard.Key.esc:
        return False
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
zmeika = [[0, 2], [0, 1], [0, 0]]
apples = 0
apple_coord = ['no', 'no']
score = 0
def apple(field):
    global apple_coord, zmeika, Apple
    if apple_coord[0] == 'no' and apple_coord[1] == 'no':
        apple_coord = [randint(0, 9), randint(0, 9)]
    if not apple_coord in zmeika:
        field[apple_coord[0]][apple_coord[1]] = Apple
def die(apples):
    global score
    cls()
    print("GAME OVER")
    print(f"YOU HAVE COLLECTED {score} APPLE" if score%10 == 1 else f"YOU HAVE COLLECTED {score} APPLES")
    sleep(3)
    cls()
    quit(score)
def move(zmeika, V):
    global field, apples, apple_coord, score
    match V:
        case 'r':
            if zmeika[0][1] == 9:
                die(apples)
            check = list(zmeika[0])
            check[1] += 1
            if apples == 0:
                field[zmeika[-1][0]][zmeika[-1][1]] = x
                n = 1
            else:
                apples -= 1
                n = 2
                zmeika.append(list(zmeika[-1]))
            if list(check) == list(apple_coord):
                apples += 1
                score += 1
                apple_coord = list(['no', 'no'])
            for a in range(len(zmeika)-n, 0, -1):
                zmeika[a] = list(zmeika[a-1])
            zmeika[0][1] += 1
            if list(zmeika[0]) in list(zmeika[1::]):
                die(apples)
            field[zmeika[0][0]][zmeika[0][1]] = h
        case 'l':
            if zmeika[0][1] == 0:
                die(apples)
            check = list(zmeika[0])
            check[1] -= 1
            if apples == 0:
                field[zmeika[-1][0]][zmeika[-1][1]] = x
                n = 1
            else:
                apples -= 1
                n = 2
                zmeika.append(list(zmeika[-1]))
            if list(check) == list(apple_coord):
                apples += 1
                score += 1
                apple_coord = list(['no', 'no'])
            for a in range(len(zmeika)-n, 0, -1):
                zmeika[a] = list(zmeika[a-1])
            zmeika[0][1] -= 1
            if list(zmeika[0]) in list(zmeika[1::]):
                die(apples)
            field[zmeika[0][0]][zmeika[0][1]] = h
        case 'u':
            if zmeika[0][0] == 0:
                die(apples)
            check = list(zmeika[0])
            check[0] -= 1
            if apples == 0:
                field[zmeika[-1][0]][zmeika[-1][1]] = x
                n = 1
            else:
                apples -= 1
                n = 2
                zmeika.append(list(zmeika[-1]))
            if list(check) == list(apple_coord):
                apples += 1
                score += 1
                apple_coord = list(['no', 'no'])
            for a in range(len(zmeika)-n, 0, -1):
                zmeika[a] = list(zmeika[a-1])
            zmeika[0][0] -= 1
            if list(zmeika[0]) in list(zmeika[1::]):
                die(apples)
            field[zmeika[0][0]][zmeika[0][1]] = h
        case 'd':
            if zmeika[0][0] == 9:
                die(apples)
            check = list(zmeika[0])
            check[0] += 1
            if apples == 0:
                field[zmeika[-1][0]][zmeika[-1][1]] = x
                n = 1
            else:
                apples -= 1
                n = 2
                zmeika.append(list(zmeika[-1]))
            if list(check) == list(apple_coord):
                apples += 1
                score += 1
                apple_coord = list(['no', 'no'])
            for a in range(len(zmeika)-n, 0, -1):
                zmeika[a] = list(zmeika[a-1])
            zmeika[0][0] += 1
            if list(zmeika[0]) in list(zmeika[1::]):
                die(apples)
            field[zmeika[0][0]][zmeika[0][1]] = h
listener.start()
while True:
    printf(field)
    step += 1 
    sleep(1-step//5*0.012) if step < 375 else sleep(0.1)
    move(zmeika, V)
    apple(field)