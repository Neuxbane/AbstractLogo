import time


from Guide import *


import pygame
from pygame.locals import *


#List of Keys in keyboard
actionKeys = [  [107342048, 'Lctrl'], 
				[1073742050, 'Lalt'], 
				[1073742049, 'Lshift'], 
				[1073741881, 'capslock'], 
				[9, 'tab'], 
				[27, 'esc'], 
				[13, 'enter'],
				[1073742053, 'Rshift'],
				[1073742054, 'Ralt'], 
				[1073742052, 'Rctrl'], 
				[1073741906, 'up'],
				[1073741905, 'down'],
				[1073741903, 'right'],
				[1073741904, 'left'], 
				[8, 'backspace'] ]


class HotKeys():
	"""Class HotKeys event listener on the keyborad and mouse"""
	def __init__(self):
		pass


	"""Function for fill the screen by default
		Arguments:
			value {Tuple} -- default value for filling screen by default (0, 0, 0)

		Keyword Arguments: None
		Raises: None

		Returns:
			[Tuple] -- by default value (0, 0, 0) but if arguments with value it can change the value
	"""
	def screenFillByDefault(self, value=(0, 0, 0)):
		return value


	"""Exit from application
		Arguments:
			action {Event} -- value for action only event for exiting program
		
		Keyword Arguments: None
		Raises: None
		Returns: None
	"""
	def quit(self, action):
		if action.type == pygame.QUIT:
			exit()


	"""The mouse function can be used to get the current state of the mouse device
		Arguments:	
			action {Event} -- action value for event listner for mouse

		Keyword Arguments: None
		Raises: None
		Returns: None
	"""
	def mouseButtons(self, action):
		if action.type == MOUSEBUTTONDOWN:
			pass
		elif action.type == MOUSEBUTTONUP:
			pass
		elif action.type == MOUSEMOTION:
			pass


	"""Action keys function event listener to get each press from keyboard and returning current state of the keyboard
		Arguments:
			action {Event} -- event listener for buttons in keyboard

		Keyword Arguments: None
		Raises: None
		Returns: 
			[String] -- return value for pressed buttons
	"""
	def actionKeys(self, action):
		for item in range(len(actionKeys)):
			if action.key == actionKeys[item][0]:
				return actionKeys[item][1]
			return action.unicode


	"""Change image function to change shape of the object real time
		Arguments:
			actionKeys {Array} -- array of cordinats
			screen {Tuple} -- screen size
			logo {Class} -- class value for calling methods
			rainbow {Integer} -- rainbow value for moving colors real time

		Keyword Arguments: None
		Raises: None
		Return: None	
	"""
	def changeImage(self, actionKeys, screen, logo, rainbow):
		if ' ' in actionKeys[0]:
			screen.fill(self.screenFillByDefault())
			logo.random()
			logo.new()
			if not rainbow:
				logo.draw(pygame, screen)


	"""Save image function to save image in png format
		Arguments:
			actionKeys {Array} -- array of cordinats
			screen {Tuple} -- screen size
		
		Keyword Argumets: None
		Raises: None
		Return: None
	"""
	def saveImage(self, actionKeys, screen):
		if 's' in actionKeys[0]:
			pygame.image.save(screen, f'{round(time.time() * 1000)}.png')


	"""Save object shape function to save current shape of the object 
		Arguments:
			actionKeys {Array} -- array of cordinats
			logo {Class} -- class for calling methods

		Keyword Argumets: None
		Raises: None
		Return: None
	"""
	def saveObjectShape(self, actionKeys, logo):
		if 't' in actionKeys[0]:
			open('load.txt', 'w').write(str(logo.save()))


	"""Open saved object shape function to read old postion of shapes
		Arguments:
			actionKeys {Array} -- array of cordinats
			logo {Class} -- class for calling methods
			screen {Tuple} -- screen size
		
		Keyword Arguments: None
		Raises: None
		Return: None
	"""
	def openSavedObjectShape(self, actionKeys, logo, screen):
		if 'l' in actionKeys[0]:
			screen.fill(self.screenFillByDefault(self))
			units = eval(open('load.txt', 'r').read())
			logo.load(units[0], units[1])
			logo.draw(pygame, screen)


	"""Private function zooming units this function only for zoomInzoomOut()
		Arguments:
			screen {Tuple} -- screen size
			logo {Class} -- class for calling methods

		Keyword Arguments: None
		Raises: None
		Return: 
			[List]
	"""
	def __zoomingUnits(self, screen, logo):
		screen.fill(self.screenFillByDefault())
		return eval(str(logo.save()))


	"""Zoom in zoom out function to make close and away
		Arguments:
			actionKeys {Array} -- array of cordinats
			screen {Tuple} -- screen size
			logo {Class} -- class for calling methods
		
		Keyword Arguments: None
		Raises: None
		Return: None
	"""
	def zoomInzoomOut(self, actionKeys, screen, logo):
		if '=' in actionKeys[0]:
			units = self.__zoomingUnits(screen=screen, logo=logo)
			logo.load(units[0], [x + 1 for x in units[1]])
			logo.draw(pygame, screen)
		elif '-' in actionKeys[0]:
			units = self.__zoomingUnits(screen=screen, logo=logo)
			logo.load(units[0], [x - 1 for x in units[1]])
			logo.draw(pygame, screen)


	"""Contrast colors changing function to move colors in real time
		Arguments:
			rainbow {} -- rainbow value for moving colors real time
			actionKeys {} -- array of cordinats
			logo {} -- class for calling methods
			screen {} -- screen size

		Keyword Arguments: None
		Raises: None
		Return: 
			[Integer] -- for activating rainbow colors
	"""
	def contrastColorsChanging(self, rainbow, actionKeys, logo, screen):
		if 'r' in actionKeys[0]:
			if rainbow:
				logo.draw(pygame, screen)
				return 0
			return 1