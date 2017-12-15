# IMPORTANT
# pygame is a little off [buggy] on mac
# please run on pc

# http://www.cogsci.rpi.edu/~destem/gamedev/pygame.pdf
# https://docs.python.org/3/
# those links use as refrence

# these modules are not as important, they come with python 3.x, and osx, and window 
import sys
import os
import math

# comments REALLY help

# [n2d] i need to do this on a windows machine
# ascii that are needed (251, 0178, 227, 248, 43, 45, 0215, 0247)
# those ascii chars do not seem to work on mac os...
# i dont need those anymore, i used a psd

# you need pygame for this to work.
# Instructions to Download Pygame
# windows:
# win + r, type in cmd
# type in 'pip 3 install pygame'
# osx:
# search 'terminal'
# run terminal, type in 'pip3 install pygame'

"""
[n2s] = note to self
[n2d] = need to do
[stc] = subject to change
0 [Thu March 13] [b] = buggy

TO DO
- [Thu, March 23] do i want to have arc angles? hard math and i dont know
	pygame.draw.arca() well enough

"""

try: # tests if pygame is installed
	import pygame
except ImportError: # if it isnt, stops the rest of a program
	print('You do not have the required modules installed!')
	input()
	sys.exit()

pygame.init() # starts pygame

displaySize = (600,600) # sets display size
display = pygame.display.set_mode(displaySize) # starts the display

clock = pygame.time.Clock() # starts the clock
background = pygame.Surface(display.get_size()) # background, layer one

circleData, triData = {}, {}
# basic colors
colors = {
	'black':(0,0,0),
	'gray':(192,192,192),
	'white':(255,255,255),
	'red':(255,0,0),
	'green':(0,255,0),
	'blue':(0,0,255)
}

# work around? alt codes are for windows but every operating system has unicode
# sooo this works. i dont know of any bugs yet
# i dont think i need this... 4/5/2017 - current

font = pygame.font.SysFont("timesnewroman", 15)
text = ['a','b','c']
horzText = font.render(text[0], False, (245,245,245))
vertText = font.render(text[1], False, (245,245,245))
hypeText = font.render(text[2], False, (245,245,245))
#auth = font.render("Code and design by **redacted** ", False, (255,255,255))


"""
							menu
circle formulas
area = pir^2
circumfrence = 2pir
length of circular arc = theta x (pi/180) x r

degrees = radians x (180/pi)
radians = degrees x (pi/180)

:: this part will be on the right of the circle formulas ::
[n2d] i need to figure out a faster way to blit text
function text?
"""

# sets center, center for pygame is width>x>0 and height>y>0
center = (int(displaySize[0]/2), int(displaySize[1]/2))

# just clears display, it blits the background which is just black
def clearScreen(background=background):display.blit(background,(0,0))

# faster way of drawingline, i set default for almost everything
def drawLine(xEnd, yEnd, color=colors['white'], xStart=center[0], yStart=center[1], display=display):
	pygame.draw.line(display,color,(xStart, yStart), (xEnd, yEnd))

# main graphics function, center is defaulted to be the global var center.
# i dont think i will ever need to change 'center=center'
def graphics(mouseInfo, horzText, vertText, hypeText, center=center, display=display):

	global triData, circleData
	# clears screen
	# mouseInfo = mouseCoord, why not a change?
	clearScreen()

	# triangle
	drawLine(mouseInfo[0], center[0]) # horizontal ___
	drawLine(mouseInfo[0], mouseInfo[1], xStart=mouseInfo[0]) # vertical |
	drawLine(mouseInfo[0], mouseInfo[1]) # hypotneuse /
	lenHori = math.fabs(center[0] - mouseInfo[0]) # horizontal, ___
	lenVert = math.fabs(center[0] - mouseInfo[1]) #vertical |
	lenHyp = int(math.sqrt((lenHori ** 2) + (lenVert ** 2))) # lenHyp is equal to radius /

	circleData = {
		"radi":round(lenHyp,2),
		"dia":round(lenHyp*2,2),
		"area":round(math.pi*(lenHyp**2), 2),
		"circ":round(2*math.pi*lenHyp, 2)
	}

	triData = {
		"area":(lenHori * lenVert)/2,
		"peri":lenHori + lenVert + lenHyp,
		"hypo":round(math.sqrt((lenHori ** 2) + (lenVert ** 2)), 2),
		"horz":lenHori,
		"vert":lenVert
	}

	def statsText():
		# triangle text
		text("triangle data", (110,5))
		text("a = {}px".format(triData["horz"]), (20,20))
		text("b = {}px".format(triData["vert"]), (110,20))
		text("c = {}px".format(triData["hypo"]), (200, 20))
		text("area = {}px".format(triData["area"]), (20, 35))
		text("perimeter = {}px".format(triData["peri"]), (140, 35))

		# circular text
		text("circle data", (450, 5))
		text("radius = {}px".format(float(circleData["radi"])), (490, 20))
		text("area = {}px".format(circleData["area"]), (350, 20))
		text("circumfrence = {}px".format(circleData["circ"]), (400, 35))
	
	statsText()
	
	# [stc] draws single circle, i 'a' didnt think i wanted to make a function for this because i only use it one
	pygame.draw.circle(display, colors["white"], center, circleData['radi'] + 1, 1)

	# [stc] these two try statements are annoying me
	"""
	try:
		tempSlope = (mouseInfo[1] - center[0])/(mouseInfo[0] - center[0])
		perpSlope = -1/tempSlope
	except ZerorDivisionError:
		tempSlope = 0
		perpSlope = -1/tempSlope
	"""
	try:tempSlope = (mouseInfo[1] - center[0])/(mouseInfo[0] - center[0])
	except ZeroDivisionError:tempSlope = 0

	try:perpSlope = -1/tempSlope
	except ZeroDivisionError:pass

	if mouseInfo[0] == center[0]:
		drawLine(mouseInfo[0] + circleData['radi'], mouseInfo[1], xStart=mouseInfo[0] - circleData['radi'], yStart=mouseInfo[1])
	elif mouseInfo[1] == center[0]:
		drawLine(mouseInfo[0], mouseInfo[1] + circleData['radi'], xStart=mouseInfo[0], yStart=mouseInfo[1] - circleData['radi'])

	# *note* running through sublime text will distort the tangent line
	# python idle works perfectly fine, as of March 22, 9:46pm
	# any line with 'math.sin' or 'math.cos' contained help from fellow classmate
	else:
		try:
			ang = math.atan(tempSlope)
			xChange, yChange = math.sin(ang)*circleData['radi'], math.cos(ang)*circleData['radi']
			# positive quadrant
			if mouseInfo[0] > center[0]:
				drawLine(((circleData['radi'] / math.cos(ang)) + center[0]), center[0], xStart=mouseInfo[0], yStart=mouseInfo[1])
				drawLine(center[0], ((circleData['radi'] / math.sin(ang)) + center[0]), xStart=mouseInfo[0], yStart=mouseInfo[1])

			# negative quadrant
			else:
				drawLine((-(circleData['radi'] / math.cos(ang)) + center[0]), center[0], xStart=mouseInfo[0], yStart=mouseInfo[1])
				drawLine(center[0], (-(circleData['radi'] / math.sin(ang)) + center[0]), xStart=mouseInfo[0], yStart=mouseInfo[1])
		except ZeroDivisionError:pass

		#for data in circleData:
		#print(data + "=" + str(circleData[data]))

	"""
	def text(text, xy, display=display, color=colors['white'], size=20):
		font = pygame.font.SysFont("AmericanTypewritter", size)
		text = str(text)
		temp = font.render(text, True, color)
		display.blit(temp, xy)
	"""

	# -- starts --
	# text offsets, the letters for lines dont look nice if you just put it in the middle of the line
	# so this just asks where your mouse is and either adds to x or y depending on where you are
	# i personally adjusted all of these to make them look right
	if circleData['circ'] >= 275:
		x,y,z= 0,0,0
		cX, cY = 0,0
		x = -16 if (mouseInfo[1] > center[0]) else -2
		y = 4 if (mouseInfo[0] > center[0]) else -11
		if mouseInfo[0] > center[0]:
			cX, cY = -12, -12
			if mouseInfo[1] > center[0]:cX, cY = -4, 6.5
		else:
			cX, cY = 10, -10
			if mouseInfo[1] > center[0]:cX, cY = 4, 6.5
	# -- end --
		# displays 'a', 'b', and 'c'
		display.blit(horzText, ((mouseInfo[0] + center[0]) / 2, center[0] + x))
		display.blit(vertText, (mouseInfo[0] + y, ((mouseInfo[1] + center[0]) / 2)))
		display.blit(hypeText, (((mouseInfo[0] + center[0]) / 2) + cX, ((mouseInfo[1] + center[0]) / 2) + cY))

#[n2d] need to add a menu for credits and formulas
# college board doesnt allow names, remove names
def menu(center=center,display=display):
	global horzText
	global vertText
	global hypeText
	menuSurface = pygame.Surface(display.get_size())
	mouseInfo = pygame.mouse.get_pos()
	pygame.display.set_caption("Triangler - Menu")

	def drawRectFilled(rectLoc, color=(255,255,255), opacity=255, menuSurface=menuSurface):
		# just the filled rectangle version of the pygame.draw.rect function, also has the ability to draw opacity
		pygame.draw.rect(menuSurface, color, rectLoc)
		menuSurface.set_alpha(opacity)
		display.blit(menuSurface, (0,0))

	def drawRect(rectLoc, line, color=(255,255,255), opacity=255, menuSurface=menuSurface):
		# drawing the rect and then make all of the surface opaque
		pygame.draw.rect(menuSurface, color, rectLoc, line)
		menuSurface.set_alpha(opacity) #* this is how to make the opactity work
		display.blit(menuSurface, (0,0))
	

	while True:
		menuImg = pygame.image.load("menu.png")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
					# from this menu mouseInfo is not important. 
					mainLoop()

		graphics(mouseInfo, horzText, vertText, hypeText)

		drawRectFilled([100,50,400,300], opacity=128) # main rectangle
		drawRect([105,55,390,290], 2, color=(0,0,0), opacity=128) # outline
		display.blit(menuImg, (100,50))

		# i think the fastest way of doing this is to create a .png and blit it...
		# blit every single line of text is annoying and takes too much time...
		#text('menu', (260,60), color=(0,0,0), size=40)
		#text('cirlce formulas', (125,85), color=(10,10,10), size=25) # i had two bugs, 'color(x,y,z)' remember to put '='

		text("fps {}".format(int(clock.get_fps())), (560,580), color=(0,255,0))
		# display.blit(auth, (5, 580)) # redacted
		pygame.display.update()
		clock.tick(24)
#font = pygame.font.SysFont("AmericanTypewritter", size)

def text(text, xy, display=display, color=colors['white'], size=15, alias=False):
	font = pygame.font.SysFont("timesnewroman", size)
	text = str(text)
	temp = font.render(text, alias, color)
	display.blit(temp, xy)

def pause():
	pygame.display.set_caption("Triangler - Paused")
	while True:
		text("paused, press any key to continue...", (160,60), color=(0,251,251), size=20)
		# display.blit(auth, (5, 580)) # redacted
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				mainLoop()
		pygame.display.update()

def mainLoop():
	global horzText
	global vertText
	global hypeText
	# i dont really understand variable globilazation, in some cases i cant use a var unless i get it
	# def func(var) or func(var=var)
	# func(var)
	pygame.display.set_caption("Triangler")

	while True:
		# [stc] i want to add a terminal which you can view formulas and math
		for event in pygame.event.get():
			key = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif pygame.mouse.get_focused() == 1:
					mouseInfo = pygame.mouse.get_pos()
					graphics(mouseInfo, horzText, vertText, hypeText)
					text("fps {}".format(int(clock.get_fps())), (560,580), color=(0,255,0))
					text("p - pause           h - help menu", (5,580), color=(0,255,0))

					#if circleData['circ'] >= 275:
					#	x,y,z= 0,0,0
					#	if mouseInfo[1] > center[0]:x = -12
					#	if mouseInfo[0] > center[0]:y = 7
					#	else:y = -12

					#display.blit(horz, ((mouseInfo[0] + center[0]) / 2), center[0] - x)
			if key[pygame.K_h]:menu()
			if key[pygame.K_p]:pause()
		# why not pygame.display.flip()? i have not seen a difference in them... whats the difference?
		# display.blit(auth, (5, 580)) # for author creds
		pygame.display.update()
		clock.tick(64)
		
mainLoop()
