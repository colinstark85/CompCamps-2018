import pygame

class MIT:
    def __init__(self, name):
        self.name = name
        self.image = "images/" + self.name.lower()+".png"
        self.img = pygame.image.load(self.image)
        self.img= pygame.transfers.scale(self.img,(100,100))
        self.health =20
