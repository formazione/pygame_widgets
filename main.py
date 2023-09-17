# Hello, this is a snippet
from button import *


pygame.init()

pygame.display.set_caption('Example of button')
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

def window():
	b1 = Button("CLICK ME", pos=(100,100),
		fontsize=36,
		colors="red on green",
		hover_colors="green on red",
		command=lambda: print("clicked right now"))


window()


is_running = True
while is_running:

	for event in pygame.event.get():
	 if event.type == pygame.QUIT:
	     is_running = False

	# to show buttons created
	buttons.update()
	buttons.draw(screen)

	pygame.display.update()
	clock.tick(60)

pygame.quit()