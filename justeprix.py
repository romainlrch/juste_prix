import random

goal = random.randint(0,10000)
proposition = 0

while proposition != goal :
    proposition = int(input("Quel est le nombre ? \n"))
    if proposition > 10000 or proposition < 0 :
        print("Tu es hors intervalle, la valeur est entre 0 et 10 000")
    else:
        if proposition > goal :
            print("Le nombre est plus petit")
        elif proposition < goal :
            print("Le nombre est plus grand")
else:
    print("C'est gagné, le nombre était bien : " , goal)