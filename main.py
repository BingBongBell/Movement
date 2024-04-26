import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Rectangles")
soldier = pygame.image.load("Standing (1).png").convert_alpha()

rect_2 = soldier.get_rect()


clock = pygame.time.Clock()

run = True
while run:

	#refresh the screen at 60 FPS
	clock.tick(60)

	#fill the background white
	screen.fill((255, 255, 255))

	#player controls
	key = pygame.key.get_pressed()
	if key[pygame.K_a] == True:
		rect_2.x -= 5
	if key[pygame.K_d] == True:
		rect_2.x += 5
	if key[pygame.K_w] == True:
		rect_2.y -= 5
	if key[pygame.K_s] == True:
		rect_2.y += 5

	#draw the rectangle and soldier image
	screen.blit(soldier, rect_2)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#refresh display
	pygame.display.flip()

pygame.quit()
