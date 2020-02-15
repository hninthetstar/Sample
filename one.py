import pygame
pygame.init()

win = pygame.display.set_mode(800,480))
pygame.display.set_caption("First Game")

walkLeft = [pygame.image.load("L1.png"),
			pygame.image.load("L2.png"),
			pygame.image.load("L3.png"),
			pygame.image.load("L4.png"),
			pygame.image.load("L5.png"),
			pygame.image.load("L6.png"),
			pygame.image.load("L7.png"),
			pygame.image.load("L8.png"),
			pygame.image.load("L9.png"),]

walkright = [pygame.image.load('R1.png'),
			 pygame.image.load('R2.png'),
			 pygame.image.load('R4.png'),
			 pygame.image.load('R5.png'),
			 pygame.image.load('R6.png'),
			 pygame.image.load('R7.png'),
			 pygame.image.load('R8.png'),
			 pygame.image.load('R9.png'),]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.tme.Clock()

