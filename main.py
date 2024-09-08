import pygame

from pendulum import Pendulum

WIDTH, HEIGHT = 400, 400

pendulum = Pendulum(WIDTH / 2, 0, 200, 1.0)
pendulum1 = Pendulum(WIDTH / 2, 0, 100, 1.0)

pygame.init()

pygame.display.set_caption("Pendulum")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
delta = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill('black')
	
	pendulum.update()
	pendulum.draw(screen)
 
	pendulum1.update()
	pendulum1.draw(screen)
	
	pygame.display.flip()
	
	delta = clock.tick(60) / 1000

pygame.quit()