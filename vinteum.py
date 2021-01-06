import pygame
from pygame.locals import *

# Sempre tem que colocar logo no começo
pygame.init()

SCREEN_WIDTH = 512#288
SCREEN_HEIGHT = 512
BACKGROUND = pygame.image.load('./resources/background-verde.png')

# frames por segundo
SPEED = 15

#Criar a tela
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Essa classe está herdando funcionalidades da classe pygame.sprite.Sprite
class Bird(pygame.sprite.Sprite):
	#Daunder init, construtor
	def __init__(self):
		#Chama o construtor da classe herdada
		pygame.sprite.Sprite.__init__(self)

		# o pássaro é composto por 4 images que vão se alternando, dando movimento.
		# As imagens foram colocadas num array de imagens
		self.images = [pygame.image.load('./resources/as_copas.JPG').convert_alpha()]

		self.current_image = 0
		
		# o .convert_alpha() faz com que a imagem não seja considerada um retangulo, despreza a parte transparente
		self.image = pygame.image.load('./resources/as_copas.JPG').convert_alpha()
		

		# Cria uma variável que representa um retangulo em volta da imagem. É usado para posicionamento.
		self.rect = self.image.get_rect()
		#print(self.rect) # rect(0, 0, 58, 84) -> Esse retangulo começa na posição 0,0
		# Faz começar no meio da tela
		self.rect[0]=(SCREEN_WIDTH/2)-29
		self.rect[1]=(SCREEN_HEIGHT/2)-42

	
	def update(self):
		#Pega o número da próxima imagem do array
		##self.current_image = (self.current_image + 1) % 4
		#Cada atualização, altera para a próxima imagem
		self.image = self.images[self.current_image]


# Cria um array de objetos
bird_group = pygame.sprite.Group()

# Cria um objeto da classe Bird()
bird = Bird()

# Adiciona o objeto ao grupo
bird_group.add(bird)

# Cria um objeto tipo Clock e força um atraso no While
#clock = pygame.time.Clock()

while True:
	#Define 20 Frames por segundo
	#clock.tick(20)

	# Aqui no "FOR" definimos os eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Close your program if the user wants to quit.
			raise SystemExit
	#		pygame.quit()

		#print(event)

		if event.type == pygame.MOUSEMOTION:

			#print(bird.rect)
			if event.buttons[0]==1 and event.pos[0] - bird.rect[0]>=0 and event.pos[0] - bird.rect[1]<=58 and event.pos[1] - bird.rect[1]>=0 and event.pos[1] - bird.rect[1]<=84:

				if event.rel[0] != 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
					#print("You're moving the mouse to the right")
					bird.rect[0] = bird.rect[0] + event.rel[0]

				if event.rel[1] != 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
					#print("You're moving the mouse down")
					bird.rect[1] = bird.rect[1] + event.rel[1]
		'''
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				#print("You pressed the left mouse button")
				pass
			if event.button == 3:
				#print("You pressed the right mouse button")
				bird.rect[1] += 3

		if event.type == pygame.MOUSEBUTTONUP:
			print("You released the mouse button")
		'''
	# A cada iteração de tela, coloca o fundo novamente
	screen.blit(BACKGROUND,(0,0))

	# Atualiza os atributos de cada objeto do grupo
	bird_group.update()

	# Desenha na tela(screen) cada objeto do grupo
	bird_group.draw(screen)

	# Atualiza a tela
	pygame.display.update()