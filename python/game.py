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
    print("wild {brett} appears".format(mit.name))
    while mit.isAlive():
        print("you have {50} health".format(health))
        print("do you want to fight or flee?")
        if input("fight / flee > ").lower() == "fight":
                damage = mit.attack()
                print("you did {10} damage".format(damage))
        else:
            caught = random.randint(1,5) == 1
            if not caught:
                print("you have escaped")
                print("you score was {}".format(score))
                sys.exit(0)
            else:
                print("you falied to run away")
                import pygame

import random



from settings import Settings

from button import Button

from mit import MIT



class Game():

	def __init__(self):

		self.background = pygame.image.load("images/background.png")

		self.enemy = None

		self.mits = [

			MIT("Kaitlin"),

			MIT("Rhiannon"),

			MIT("Travis"),

			MIT("Austin"),

			MIT("Bennett")

		]

		random.shuffle(self.mits)



		self.font = pygame.font.SysFont('Comic Sans MS', 30)



		self.buttons = [

			Button(0, Settings.height - 100, 100, 100, "Fight"),

			Button(Settings.width - 100, Settings.height - 100, 100, 100, "Flee")

		]



	def loop(self, screen):

		clock = pygame.time.Clock()



		if not self.enemy:

			self.enemy = self.mits.pop()

			self.text = self.font.render(self.enemy.name, False, (0, 0, 0))



		while True:

			delta_t = clock.tick(Settings.frameRate)



			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					return



			screen.fill((0, 0, 0))

			screen.blit(self.background, (0, 0))



			screen.blit(self.enemy.img, (Settings.width - 150, 50))

			pygame.draw.rect(screen, (0, 0, 0), (Settings.width - 150, 150, 100, 10))

			pygame.draw.rect(screen, (0, 255, 0), (Settings.width - 150, 150, (self.enemy.health / 20) * 100, 10))

			screen.blit(self.text, (Settings.width - 150, 160))



			for button in self.buttons:

				pygame.draw.rect(screen, (0, 0, 255), (button.x, button.y, button.w, button.h))

				screen.blit(button.text, (button.x, button.y))



			pygame.display.flip()



	def quit(self):
