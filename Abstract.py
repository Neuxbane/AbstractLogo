import random
import time

import pygame
from pygame.locals import *

from Colors import *
from Coordinate import *

colors = Colors()
coordinate = Coordinate()

class Abstract:
	"""Abstract Logo class for creating object shape on the screen"""
	def __init__(self):
		self.x = 0
		self.y = 0
		self.oldx = 0
		self.oldy = 0
		self.speed = []
		self.length = []
		self.deg = []
		self.startpos = 0
		self.rainbow = 0


	"""Rangom object shape generator
		Arguments:
			speed {integer} -- drawing speed, by default 100
			length {integer} -- size of the shape, by default 10
			ranges {integer} -- ranges, by default 3

		Keyword Arguments: None
		Raises: None
		Returns: None
	"""
	def random(self, speed=100, length=10, ranges=3):
		random.seed(round(time.time() * 200))
		self.speed = [round((round(random.random()) * 2 - 1) * (random.random() * (speed - 1) + 1)) for x in range(ranges)]
		self.length = [round((round(random.random()) * 2 - 1) * (random.random() * (length - 1) + 1)) for x in range(ranges)]
		self.deg = [0 for x in range(ranges)]


	"""New position
		Arguments: None
		Keyword Arguments: None
		Raises: None
		Returns: None	
	"""
	def new(self):
		self.deg = [0 for x in range(len(self.deg))]
		self.getPosition()
		self.oldx = self.x
		self.oldy = self.y
		self.startpos = (self.x, self.y)


	"""Load postion
		Argumets:
			speed {integer}	-- drawing speed
			length {integer} -- size of the shape

		Keyword Arguments: None
		Raises: None
		Return: None
	"""
	def load(self, speed = 100, length = 10):
		self.speed = speed
		self.length = length
		self.deg = [0 for x in range(len(length))]


	"""Save current position
		Argumets: None
		Keyword Arguments: None
		Reises: None

		Returns:
			{integer} -- returns current speed and length
	"""
	def save(self):
		return (self.speed, self.length)


	"""Private function for keeping default values of X and Y __drawTheShape and __moveTheRainbow
		Arguments: 
			rainbow {Integer} 

		Keyword Arguments: None
		Reises: None

		Returns:
			{intger} -- return current value of rainbow
	"""
	def __defaultValueOfXY(self, rainbow = 0):
		self.new()
		self.x = 0
		self.y = 0
		return rainbow	


	"""Private function old sets of X and Y coordinats __drawTheShape and __moveTheRainbow
		Arguments: None
		Keyword Arguments: None
		Reises: None
		Returns: None
	"""
	def __oldSetsOfXY(self):
		self.oldx = self.x
		self.oldy = self.y
		self.getPosition()


	"""Private function to draw shape for __drawTheShape and __moveTheRainbow
		Arguments
			rainbow {Integer} -- for moving color on the shape
			coordinats {Integer} -- coordinats for color
			screen {Tuple} -- screen size

		Keyword Arguments: None
		Reises: None

		Returns: 
			{Integer} -- for activating color moving
	"""
	def __rainbowDrawing(self, rainbow = 0, coordinats = 0, screen = 0):
		if rainbow:
			pygame.draw.line(screen, colors.color(coordinats), (self.oldx, self.oldy), (self.x, self.y), 5)
		rainbow = 1
		return rainbow


	"""Private function for drawing shape for draw()
		Arguments: 
			screen {Tuple} -- screen size
		
		Keyword Arguments: None
		Reises: None
		Returns: None
	"""
	def __drawTheShape(self, screen = 0):
		rainbow = self.__defaultValueOfXY()
		while not self.startpos == (self.x , self.y):
			self.__oldSetsOfXY()	
			value = (self.x + self.y) / 2
			rainbow = self.__rainbowDrawing(rainbow=rainbow, coordinats=value, screen=screen)


	"""Privaet function for move rainbow for draw()
		Arguments: 
			screen {Tuple} -- screen size

		Keyword Arguments: None
		Reises: None
		Returns: None	
	"""
	def __moveTheRainbow(self, screen = 0):
		rainbow = self.__defaultValueOfXY()
		while not self.startpos == (self.x, self.y):
			self.rainbow += 0.005
			self.__oldSetsOfXY()
			value = ((self.x + self.y) / 2) + self.rainbow
			rainbow = self.__rainbowDrawing(rainbow=rainbow, coordinats=value, screen=screen)


	"""Draw new image
		Arguments:
			pygame {Class} -- pygame class for working pygame screen
			screen {Tuple} -- screen size
			play {Boolean} -- for running game none stop

		Keyword Arguments: None
		Reises: None
		Returns: None
	"""
	def draw(self, pygame, screen = 0, play=False):
		if not play:
			self.__drawTheShape(screen=screen)	
		else:
			self.__moveTheRainbow(screen=screen)			


	"""Private function to calculate coordinats for getPosition()
		Arguments: None
		Keyword Arguments: None
		Reises: None
		Returns: None	
	"""
	def __calculateCordinatsXY(self):
		v, h = pygame.display.get_surface().get_size()
		self.x *= 10
		self.y *= 10
		self.x += v / 2
		self.y += h / 2


	"""Private function to calculate range of coordinats for getPosition()
		Arguments: None
		Keyword Arguments: None
		Reises: None
		Returns: None
	"""
	def __calculateRangeOfXY(self):
		for x in range(len(self.length)):
			self.deg[x] += self.speed[x]
			if 360 < abs(self.deg[x]):
				self.deg[x] += (-360 * (2 * (0 < self.deg[x]) - 1))
			self.x += coordinate.sin(self.deg[x]) * self.length[x]
			self.y += coordinate.cos(self.deg[x]) * self.length[x]


	"""Get current postion
		Arguments: None
		Keyword Arguments: None
		Reises: None
		Returns: None	
	"""
	def getPosition(self):
		self.x = 0
		self.y = 0
		self.__calculateRangeOfXY()	
		self.__calculateCordinatsXY()	