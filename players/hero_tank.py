import pygame
import os

class HeroTank(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []

		hero_tank_image = pygame.image.load(os.path.join('sprites', 'hero_tank.png')).convert()
		self.images.append(hero_tank_image)
		self.image = self.images[0]
		self.rect = self.image.get_rect()

