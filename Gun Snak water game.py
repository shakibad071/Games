var = ["g", "w", "s"]

import random

print("This is 'Snake, Water and Gun' Games.\n"
    "You can chose s for Snake, w for water and g for gun.\n"
    "Please input all latter in small case")
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0

def count():
    round= 1
    while  round<=20:
        ai = random.choice(var)
        user = str(input("Choice your option: ")).lower()
        print("Computer Choice: ",ai)
        if ai=="g" and user=="w":
            print("You win!")
            global e
            e= e+ 1
        elif ai=="g" and user=="s":
            print("Computer Win!")
            global f
            f= f+ 1
        elif ai=="g" and user=="g":
            print("Drawn!")
            global g
            g=g+ 1
        elif ai=="s" and user=="w":
            print("Computer Win!")
            global h
            h=h+ 1
        elif ai=="s" and user=="s":
            print("Drawn!")
            global i
            i=i+ 1
        elif ai=="s" and user=="g":
            print("You Win!")
            global j
            j=j+ 1
        elif ai=="w" and user=="w":
            print("Drawn!")
            global k
            k=k+ 1
        elif ai=="w" and user=="s":
            print("You Win!")
            global l
            l=l+ 1
        elif ai=="w" and user=="g":
            print("Computer Win!")
            global m
            m=m+ 1
        else:
            print("Please input valid option.\n")
            continue
        round= round +1
        round= round +1


    while round>20:
        print("Game over!")
        break

count()
total_win= (e+j+l)
total_lose= (f+h+m)
total_drawn= (g+i+k)
print(f"You win {total_win}, Computer win {total_lose}, Drawn {total_drawn}")
if total_win>total_lose:
    print("You are the winner")

elif total_lose>total_win:
    print("You are the losser")
elif total_lose==total_lose and total_win!= 0:
    print("No One win the game")
