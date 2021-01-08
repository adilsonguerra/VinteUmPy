import pygame
from pygame.locals import *

# Sempre tem que colocar logo no começo
pygame.init()

IMAGES_DIR = './resources/'
SCREEN_WIDTH = 512#288
SCREEN_HEIGHT = 512
BACKGROUND = pygame.image.load(IMAGES_DIR + 'background-branco.png')

images_card= []
images_card.append(pygame.image.load(IMAGES_DIR + 'joker.jpg'))
#copas
images_card.append(pygame.image.load(IMAGES_DIR + 'as_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dois_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'tres_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'quatro_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'cinco_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'seis_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'sete_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'oito_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'nove_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dez_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dama_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'valete_copas.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'rei_copas.jpg'))
#espadas
images_card.append(pygame.image.load(IMAGES_DIR + 'as_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dois_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'tres_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'quatro_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'cinco_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'seis_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'sete_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'oito_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'nove_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dez_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dama_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'valete_espada.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'rei_espada.jpg'))
#ouros
images_card.append(pygame.image.load(IMAGES_DIR + 'as_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dois_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'tres_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'quatro_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'cinco_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'seis_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'sete_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'oito_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'nove_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dez_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dama_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'valete_ouro.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'rei_ouro.jpg'))
#paus
images_card.append(pygame.image.load(IMAGES_DIR + 'as_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dois_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'tres_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'quatro_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'cinco_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'seis_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'sete_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'oito_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'nove_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dez_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'dama_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'valete_paus.jpg'))
images_card.append(pygame.image.load(IMAGES_DIR + 'rei_paus.jpg'))

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

class Baralho():
	#Daunder init, construtor
	def __init__(self):
		self.monte=[]
		for i in range(53):
			self.monte.append(Carta(images_card[i], pygame.image.load(IMAGES_DIR + 'verso_py.jpg'),1,1,100+i,100+i))
		
baralho = Baralho()

# Cria um array de objetos
carta_group = pygame.sprite.Group()

cartas=[]
cartas = baralho.monte

# Adiciona cada carta objeto ao grupo
for i in range(len(cartas)):
	carta_group.add(cartas[i])

#Quantidade de cartas visíveis na mesa
qty_cards=53

while True:
	# Aqui no "FOR" definimos os eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Close your program if the user wants to quit.
			raise SystemExit	#  OU pygame.quit() # 	

		#print(event)
		if event.type == pygame.MOUSEMOTION:
			
			for i in range(qty_cards):
				if event.buttons[0]==1 and \
					event.pos[0] - cartas[i].rect[0]>=0 and \
					event.pos[0] - cartas[i].rect[0]<=58 and \
					event.pos[1] - cartas[i].rect[1]>=0 and \
					event.pos[1] - cartas[i].rect[1]<=84:

					if event.rel[0] != 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
						#print("You're moving the mouse to the right")
						if cartas[i].rect[0] < SCREEN_WIDTH-58 and cartas[i].rect[0] > 0:
							cartas[i].rect[0] +=  event.rel[0]
						else:
							if cartas[i].rect[0] <= 0 :
								cartas[i].rect[0] = 2
							else:
								cartas[i].rect[0] = SCREEN_WIDTH-58-2

					if event.rel[1] != 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
						#print("You're moving the mouse down")
						if cartas[i].rect[1] > 0 and cartas[i].rect[1] < SCREEN_HEIGHT-84:
							cartas[i].rect[1] +=  event.rel[1]
						else:
							if cartas[i].rect[1] <= 0:
								cartas[i].rect[1] = 2
							else:
								cartas[i].rect[1] = SCREEN_HEIGHT-84-2

		#---------------------------------------------------------------

		if event.type == pygame.MOUSEBUTTONDOWN:
			for j in range(qty_cards):
				if event.button == 3 and \
					event.pos[0] - cartas[j].rect[0]>=0 and \
					event.pos[0] - cartas[j].rect[0]<=58 and \
					event.pos[1] - cartas[j].rect[1]>=0 and \
					event.pos[1] - cartas[j].rect[1]<=84:
					#print("You pressed the right mouse button")
					if cartas[j].current_image==0:
						cartas[j].current_image=1
					else:
						cartas[j].current_image=0

		if event.type == pygame.MOUSEBUTTONUP:
			qt=0
			for i in range(qty_cards):
				if event.button==4 and \
					event.pos[0] - cartas[i].rect[0]>=0 and \
					event.pos[0] - cartas[i].rect[0]<=58 and \
					event.pos[1] - cartas[i].rect[1]>=0 and \
					event.pos[1] - cartas[i].rect[1]<=84:

					qt=qt+1
					if cartas[i].rect[0] < SCREEN_WIDTH-58 and cartas[i].rect[0] > 0:
						cartas[i].rect[0] += qt
					else:
						if cartas[i].rect[0] <= 0 :
							cartas[i].rect[0] = 2
						else:
							cartas[i].rect[0] = SCREEN_WIDTH-58-2

				if event.button==5 and \
					event.pos[0] - cartas[i].rect[0]>=0 and \
					event.pos[0] - cartas[i].rect[0]<=58 and \
					event.pos[1] - cartas[i].rect[1]>=0 and \
					event.pos[1] - cartas[i].rect[1]<=84:

					qt=qt+1
					if cartas[i].rect[0] < SCREEN_WIDTH-58 and cartas[i].rect[0] > 0:
						cartas[i].rect[0] -= qt
					else:
						if cartas[i].rect[0] <= 0 :
							cartas[i].rect[0] = 2
						else:
							cartas[i].rect[0] = SCREEN_WIDTH+58+2


					
		
	# A cada iteração de tela, coloca o fundo novamente
	screen.blit(BACKGROUND,(0,0))

	# Atualiza os atributos de cada objeto do grupo
	carta_group.update()

	# Desenha na tela(screen) cada objeto do grupo
	carta_group.draw(screen)

	# Atualiza a tela
	pygame.display.update()