import pygame
from pygame.locals import *

# Sempre tem que colocar logo no começo
pygame.init()

SCREEN_WIDTH = 512#288
SCREEN_HEIGHT = 512
BACKGROUND = pygame.image.load('./resources/background-verde.png')

#Criar a tela
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Essa classe está herdando funcionalidades da classe pygame.sprite.Sprite
class Carta(pygame.sprite.Sprite):
	#Daunder init, construtor
	def __init__(self, image_fr=None, image_vs=None, valor=None, naipe=None, posx=None, posy=None):
		#Chama o construtor da classe herdada
		pygame.sprite.Sprite.__init__(self)

		self.image_fr = image_fr
		self.image_vs = image_vs
		self.valor = valor
		self.naipe = naipe
		self.posx = posx
		self.posy = posy

		# o pássaro é composto por 4 images que vão se alternando, dando movimento.
		# As imagens foram colocadas num array de imagens
		self.images = [self.image_fr,self.image_vs]

		self.current_image = 0
		
		# o .convert_alpha() faz com que a imagem não seja considerada um retangulo, despreza a parte transparente
		self.image = self.image_fr
		
		# Cria uma variável que representa um retangulo em volta da imagem. É usado para posicionamento.
		self.rect = self.image.get_rect()
		#print(self.rect) # rect(0, 0, 58, 84) -> Esse retangulo começa na posição 0,0
		# Faz começar no meio da tela
		
		self.rect[0]=posx    #(SCREEN_WIDTH/2)-29
		self.rect[1]=posy    #(SCREEN_HEIGHT/2)-42


	def update(self):
		#Pega o número da próxima imagem do array
		##self.current_image = (self.current_image + 1) % 4
		#Cada atualização, altera para a próxima imagem
		self.image = self.images[self.current_image]


# Cria um array de objetos
carta_group = pygame.sprite.Group()

# Cria um objeto da classe carta()
carta1 = Carta(pygame.image.load('./resources/as_copas.JPG'), pygame.image.load('./resources/verso_py.jpg'), 1,1,100, 100)
carta2 = Carta(pygame.image.load('./resources/dois_copas.JPG'),pygame.image.load('./resources/verso_py.jpg'),2,2, 200, 200)

# Adiciona o objeto ao grupo
carta_group.add(carta1)
carta_group.add(carta2)

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

			#print(carta.rect)
			if event.buttons[0]==1 and \
				event.pos[0] - carta1.rect[0]>=0 and \
				event.pos[0] - carta1.rect[0]<=58 and \
				event.pos[1] - carta1.rect[1]>=0 and \
				event.pos[1] - carta1.rect[1]<=84:

				if event.rel[0] != 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
					#print("You're moving the mouse to the right")
					carta1.rect[0] +=  event.rel[0]

				if event.rel[1] != 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
					#print("You're moving the mouse down")
					carta1.rect[1] +=  event.rel[1]

			#---------------------------------------------------------------

			if event.buttons[0]==1 and \
				event.pos[0] - carta2.rect[0]>=0 and \
				event.pos[0] - carta2.rect[0]<=58 and \
				event.pos[1] - carta2.rect[1]>=0 and \
				event.pos[1] - carta2.rect[1]<=84:

				if event.rel[0] != 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
					#print("You're moving the mouse to the right")
					carta2.rect[0] +=  event.rel[0]

				if event.rel[1] != 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
					#print("You're moving the mouse down")
					carta2.rect[1] +=  event.rel[1]

			#Descola as cartas
			if carta1.rect[0] == carta2.rect[0]:
				carta1.rect[0] += 2
				carta1.rect[1] += 2
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				#print("You pressed the right mouse button")
				if carta1.current_image==0:
					carta1.current_image=1
				else:
					carta1.current_image=0

				if carta2.current_image==0:
					carta2.current_image=1
				else:
					carta2.current_image=0

		if event.type == pygame.MOUSEBUTTONUP:
			print("You released the mouse button")
		
	# A cada iteração de tela, coloca o fundo novamente
	screen.blit(BACKGROUND,(0,0))

	# Atualiza os atributos de cada objeto do grupo
	carta_group.update()

	# Desenha na tela(screen) cada objeto do grupo
	carta_group.draw(screen)

	# Atualiza a tela
	pygame.display.update()