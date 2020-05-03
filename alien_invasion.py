import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create games resources."""
		pygame.init()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# self.screen = pygame.display.set_mode([self.settings.screen_width, 
		# 	self.settings.screen_height])
		pygame.display.set_caption("Alien Invasion (Issaga' version)")

		# Create an instance of ship and assign an instance 
		# of AlienInvasion (self)
		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Call the helper method _check_events()
			self._check_events()

			# Call the method update_moving_LR() from the Ship Class
			self.ship.update_moving_LR()

			# Call the method update from the Bullet class
			self.bullets.update()

			# Get rid of bullets that have disappeared.
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
			print(len(self.bullets))

			# Call the helper method _update_screen()
			self._update_screen()

		
	def _check_events(self):
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)	

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)		



	def _check_keydown_events(self, event):
		# If pressed key is right, update flag to True
		if event.key == pygame.K_RIGHT:			
			self.ship.moving_right = True	

		# If pressed key is left, update flag to True
		elif event.key == pygame.K_LEFT:			
			self.ship.moving_left = True	

		# If q pressed, the game will be closed
		elif event.key == pygame.K_q:
				sys.exit()

		# if space bar is pressed, a bulet is method is called
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()		


	def _check_keyup_events(self, event):
		# If pressed key is is released, update flag to False
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False	

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False	

	def _fire_bullet(self):
			"""Create a new bullet and add it to the bullets group."""
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		# Redraw the screen during each pass through the loop
		# and add bg color.
		self.screen.fill(self.settings.screen_backgound_color)

		# Draw the ship on the screen
		self.ship.blitme()      

		# show bullets on the screen
		for bullet in self.bullets.sprites():

			bullet.draw_bullet()

		# Make the most recently drawn screen visible.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()

