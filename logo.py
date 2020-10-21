import pygame
import random
import time
import math
from pygame.locals import *
def sin(a):
	return math.sin((22/7)/180*a)
def cos(a):
	return math.cos((22/7)/180*a)
def color(a):
	a = (a-(round(a/360)+(((a/360)>round(a/360))*1)-1)*360)
	R = (((int(a>=0) == int(120>=a)) or (int(a>=300) == int(360>=a)))*255)+(((int(a>=60) == int(120>=a))*((60-a)*(255/60))))+((int(a>240) == int(300>a))*((a-240)*(255/60)))
	G = (((int(a>=0) == int(60>=a))*((a)*(255/60))))+((int(a>60) == int(240>=a))*255)+((int(a>=180) == int(240>=a))*((180-a)*(255/60)))
	B = (((int(a>=120) == int(180>=a))*((a-120)*(255/60))))+(((int(a>180) == int(360>a))*255))+((((int(a>300) == int(360>a))*(300-a)*(255/60))))
	return (R,G,B)
class AbstracLogo:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.oldx = 0
		self.oldy = 0
		self.speed = []
		self.length = []
		self.deg = []
		self.startpos = 0
		self.r = 0
	def random(self,speed=100,length=10,n=3):
		random.seed(round(time.time()*200))
		self.speed = [round((round(random.random())*2-1)*(random.random()*(speed-1)+1)) for x in range(n)]
		self.length = [round((round(random.random())*2-1)*(random.random()*(length-1)+1)) for x in range(n)]
		self.deg = [0 for x in range(n)]
	def new(self):
		self.deg = [0 for x in range(len(self.deg))]
		self.getpos()
		self.oldx = self.x
		self.oldy = self.y
		self.startpos = (self.x,self.y)
	def load(self,speed,length):
		self.speed = speed
		self.length = length
		self.deg = [0 for x in range(len(length))]
	def save(self):
		return (self.speed,self.length)
	def draw(self,pygame,screen,play=False):
		if not play:
			self.new()
			self.x =  0
			self.y = 0
			r = 0
			while not self.startpos == (self.x,self.y):
				self.oldx = self.x
				self.oldy = self.y
				self.getpos()
				a = (self.x+self.y)/2
				if r:
					pygame.draw.line(screen,color(a),(self.oldx,self.oldy),(self.x,self.y),5)
				r = 1
		else:
			self.new()
			self.x =  0
			self.y = 0
			r = 0
			while not self.startpos == (self.x,self.y):
				self.r += 0.005
				self.oldx = self.x
				self.oldy = self.y
				self.getpos()
				a = ((self.x+self.y)/2)+self.r
				if r:
					pygame.draw.line(screen,color(a),(self.oldx,self.oldy),(self.x,self.y),5)
				r = 1
	def getpos(self):
		self.x = 0
		self.y = 0
		for x in range(len(self.length)):
			self.deg[x] += self.speed[x]
			if 360 < abs(self.deg[x]):
				self.deg[x] += (-360*(2*(0 < self.deg[x])-1))
			self.x += sin(self.deg[x])*self.length[x]
			self.y += cos(self.deg[x])*self.length[x]
		w, h = pygame.display.get_surface().get_size()
		self.x = self.x*10
		self.y = self.y*10
		self.x += w/2
		self.y += h/2
win = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.init()
clock = pygame.time.Clock()
run = True
KeyDown = [[],[],[]]
win.fill((0,0,0))
a = AbstracLogo()
a.random()
a.draw(pygame,win)
r = 0
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			break
		if event.type == MOUSEBUTTONDOWN:
			MouseClick = (event.pos,event.button)
		if event.type == MOUSEBUTTONUP:
			pass
			#print(event,event.pos,event.button)
		if event.type == MOUSEMOTION:
			pass
			#print(event)
		if event.type == pygame.KEYDOWN:
			if event.key == 1073742048:
				KeyDown[0].append('Lctrl')
			elif event.key == 1073742050:
				KeyDown[0].append('Lalt')
			elif event.key == 1073742049:
				KeyDown[0].append('Lshift')
			elif event.key == 1073741881:
				KeyDown[0].append('capslock')
			elif event.key == 9:
				KeyDown[0].append('tab')
			elif event.key == 27:
				KeyDown[0].append('esc')
			elif event.key == 13:
				KeyDown[0].append('enter')
			elif event.key == 1073742053:
				KeyDown[0].append('Rshift')
			elif event.key == 1073742054:
				KeyDown[0].append('Ralt')
			elif event.key == 1073742052:
				KeyDown[0].append('Rctrl')
			elif event.key == 1073741906:
				KeyDown[0].append('up')
			elif event.key == 1073741905:
				KeyDown[0].append('down')
			elif event.key == 1073741903:
				KeyDown[0].append('right')
			elif event.key == 1073741904:
				KeyDown[0].append('left')
			elif event.key == 8:
				KeyDown[0].append('backspace')
			else:
				KeyDown[0].append(event.unicode)
			KeyDown[1].append(event.key)
			KeyDown[2] = KeyDown[0][-1:]
			if ' ' in KeyDown[0]:
				win.fill((0,0,0))
				a.random()
				a.new()
				if not r:
					a.draw(pygame,win)
			if 's' in KeyDown[0]:
				pygame.image.save(win,f'{round(time.time()*1000)}.png')
			if 't' in KeyDown[0]:
				open('load.txt','w').write(str(a.save()))
			if 'l' in KeyDown[0]:
				win.fill((0,0,0))
				u = eval(open('load.txt','r').read())
				a.load(u[0],u[1])
				a.draw(pygame,win)
			if '-' in KeyDown[0]:
				win.fill((0,0,0))
				u = eval(str(a.save()))
				print([x-1 for x in u[1]])
				a.load(u[0],[x-1 for x in u[1]])
				a.draw(pygame,win)
			if '=' in KeyDown[0]:
				win.fill((0,0,0))
				u = eval(str(a.save()))
				print([x-1 for x in u[1]])
				a.load(u[0],[x+1 for x in u[1]])
				a.draw(pygame,win)
			if 'r' in KeyDown[0]:
				if r:
					r = 0
					a.draw(pygame,win)
				else:
					r = 1
		try:
			if event.type == pygame.KEYUP:
				del KeyDown[0][KeyDown[1].index(event.key)]
				del KeyDown[1][KeyDown[1].index(event.key)]
			#print(KeyDown[0])
		except:
			pass
	if r:
		a.draw(pygame,win,play=1)
	clock.tick(250)
	pygame.display.flip()
pygame.quit()