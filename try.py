import sys

import pygame

class ColorBackground:
	"""Initialize game background"""

	def __init__(self):
		"""Initializing game"""
		pygame.init()

		self.screen = pygame.display.set_mode((600,750))
		pygame.display.set_caption("Try")
		self.bg_color = (140,235,160)

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bg_color)

			pygame.display.flip()

if __name__ == "__main__":
	ai = ColorBackground()
	ai.run_game()