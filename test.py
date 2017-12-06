import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
gameExit = False

pygame.display.set_caption("Snake")


while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	gameDisplay.fill((0,0,255))
	pygame.draw.rect(gameDisplay, (0,0,0), [400,300,15,15])
	gameDisplay.fill((255,0,0), rect=[200,300,15,15])
	pygame.display.update()

pygame.quit()
quit()