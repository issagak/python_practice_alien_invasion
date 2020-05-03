class Settings:
	""" A class to store all the settings for the Alien Invasion."""
	def __init__(self):
		""" Initialize the game's settings."""
		# Screen Setings
		self.screen_width = 1200
		self.screen_height = 800
		self.screen_backgound_color = (230, 230, 230)
		self.ship_speed = 1.5

		# Bullet Settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
