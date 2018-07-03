import random
import sys

name = input("who dare chalange the mits?")
health= 40
class MIT(object):
    def __init__(self,name):
        self.name =name
        self.health= 10
        self.damage= random.randint(1,5)

    def isAlive(self):
        return self.health > 0

    def attack(self):
        hitDamage = random.randint(0,10)
        self.health -= hitDamage
        return hitDamage

mits = [
 MIT  ("bennett"),
 MIT ("kaitlin"),
 MIT ("rhiamon"),
 MIT ("austin"),
 MIT ("travis")
 ]

random.shuffle(mits)
score = 0
while len(mits) > 0:
    mit = mits.pop()
    print("wild {} appears".format(mit.name))
    while mit.isAlive():
        print("you have {} health".format(health))
        print("do you want to fight or flee?")
        if input("fight / flee > ").lower() == "fight":
                damage = mit.attack()
                print("you did {} damage".format(damage))
        else:
            caught = random.randint(1,5) == 1
            if not caught:
                print("you have escaped")
                print("you score was {}".format(score))
                sys.exit(0)
            else:
                print("you falied to run away")
