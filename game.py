import pygame
import os
from players.hero_tank import HeroTank

game_world_x = 800
game_world_y = 400
frames_per_second = 40
animation_cycle = 4

class NESTank:
	def __init__(self):
		self.clock = pygame.time.Clock()

	# initial level setup and pygame initiation
	def game_setup(self):
		pygame.init()
		self.game_world = pygame.display.set_mode([game_world_x,game_world_y])
		self.game_background = pygame.image.load(os.path.join('sprites','main_background_with_bricks.png'))
		self.game_background = pygame.transform.scale(self.game_background, (800, 400))
		self.game_background_size = self.game_world.get_rect()
	
	def game_main_loop(self):
		while True:
			hero_tank = HeroTank()
			hero_tank.rect.x = 0
			hero_tank.rect.y = 0
			players_list = pygame.sprite.Group()
			players_list.add(hero_tank)

			self.game_world.blit(self.game_background, self.game_background_size)
			players_list.draw(self.game_world)
			pygame.display.flip()
			self.clock.tick(frames_per_second)

if __name__ == "__main__":
	nes = NESTank()
	nes.game_setup()
	nes.game_main_loop()

