import pygame
import os

animation_cycle = 4

class HeroTank(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tank_movement_x = 0
		self.tank_movement_y = 0
		self.frame = 0
		self.images = []
		hero_tank_image = pygame.image.load(os.path.join('sprites', 'hero_tank.png')).convert()
		self.images.append(hero_tank_image)
		self.image = self.images[0]
		self.rect = self.image.get_rect()

	def control(self, x_direction, y_direction):
		self.tank_movement_x += x_direction
		self.tank_movement_y += y_direction

	def update(self):
		self.rect.x = self.rect.x + self.tank_movement_x    
		self.rect.y = self.rect.y + self.tank_movement_y

		# moving left
		if self.tank_movement_x  < 0:
			self.frame += 1
			if self.frame > 3*animation_cycle:
				self.frame = 0
			self.image = pygame.transform.flip(self.images[self.frame//animation_cycle], True, False)

		# moving right
		if self.tank_movement_x > 0:
			self.frame += 1
			if self.frame > 3*animation_cycle:
				self.frame = 0
			self.image = self.images[self.frame//animation_cycle]