# Standard
import time

# Related
from HotKeys import *
from Abstract import *
from Guide import *

# Local
import pygame
from pygame.locals import *


windowSize = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Window default size
pygame.display.set_caption('Blume')									# Title of window
pygame.init()														# Init point

clock = pygame.time.Clock() # Create an object to help track time
run = True					# Game is running constantly
keyDown = [[], [], []]		# Arrays of cordinats
windowSize.fill((0, 0, 0))	# Fill function which fills the Surface object with black color

abstractLogo = Abstract()
hotKeys = HotKeys()
guide = Guide()

abstractLogo.random()
abstractLogo.draw(pygame=pygame, screen=windowSize)


def main():
	guide.guide()
	rainbow = 0 # Default value of rainbow colors moving real time
	while run:

		for event in pygame.event.get():
		
			hotKeys.quit(action=event)
		
			#hotKeys.mouseButtons(action=event)

			if event.type == pygame.KEYDOWN:

				keyDown[0].append(hotKeys.actionKeys(action=event))

				# Without this two line zooming doesn't work
				keyDown[1].append(event.key)
				keyDown[2] = keyDown[0][-1:]

				hotKeys.changeImage(actionKeys=keyDown, screen=windowSize, logo=abstractLogo, rainbow=rainbow)
				hotKeys.saveImage(actionKeys=keyDown, screen=windowSize)
				hotKeys.saveObjectShape(actionKeys=keyDown, logo=abstractLogo)
				hotKeys.openSavedObjectShape(actionKeys=keyDown, logo=abstractLogo, screen=windowSize)
				hotKeys.zoomInzoomOut(actionKeys=keyDown, screen=windowSize, logo=abstractLogo)
				rainbow = hotKeys.contrastColorsChanging(rainbow=rainbow, actionKeys=keyDown, logo=abstractLogo, screen=windowSize)

			try:
				if event.type == pygame.KEYUP:
					del keyDown[0][keyDown[1].index(event.key)]
					del keyDown[1][keyDown[1].index(event.key)]
			except:
				pass
		if rainbow:
			abstractLogo.draw(pygame, screen=windowSize, play=1)
		clock.tick(250)
		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()