import pygame
import random 

#Presentado por Jonathan Steven Gonzalez Pulido
#Para Politecnico Gran Colombiano
#Audio tomado de Flappy Bird Project
#Fuente tomada de Dafont Flappy Bird

#Definimos funciones que serán el nucleo que usará pygame

#V2


#Creamos el suelo en posición 900
def creador_piso():
	screen.blit(piso_sf,(piso_x_pos,900))
	screen.blit(piso_sf,(piso_x_pos + 576,900))

#def xxx():
	#screen.blit(r1, (r1pos,900))
	#screen.blit(r1, (r1pos + 576,900))

#Creamos los tubos de arriba y abajo, se está implementando la creación del tubo de la mitad
def creador_tubo():
	random_tubo_pos = random.choice(tubo_height)
	bottom_tubo = superficie_t.get_rect(midtop = (700,random_tubo_pos + 300))
	top_tubo = superficie_t.get_rect(midbottom = (700,random_tubo_pos - 300))
	return bottom_tubo,top_tubo

#Se generan tubos aleatorios (posible función eliminada en versión 2.1)
def tubosmovim(tubos):
	for tubo in tubos:
		tubo.centerx -= 5
	return tubos

#Generador de tubos
def tuboscrea(tubos):
	for tubo in tubos:
		if tubo.bottom >= 1024:
			screen.blit(superficie_t,tubo)
		else:
			flip_tubo = pygame.transform.flip(superficie_t,False,True)
			screen.blit(flip_tubo,tubo)
def retubosmovim(tubos):
	for tubo in tubos:
		if tubo.centerx == -600:
			tubos.remove(tubo)
	return tubos

#Detecta colisiones del jugador, que significarán Game Over, se ampliará para detectar los numeros equivocados como colisiones tambien
def jugador_falla(tubos):
	for tubo in tubos:
		if mathp_rect.colliderect(tubo):
			muerte_s.play()
			return False

	if mathp_rect.top <= -100 or mathp_rect.bottom >= 900:
		return False

	return True

#Movimiento dinamico de nuestro personaje principal Mathp
def rotar_mathp(mathp):
	new_mathp = pygame.transform.rotozoom(mathp,-mathp_movement * 3,1)
	return new_mathp

def movimiento_mathp():
	new_mathp = mathp_frames[mathp_index]
	new_mathp_rect = new_mathp.get_rect(center = (100,mathp_rect.centery))
	return new_mathp,new_mathp_rect

#Genera el puntaje actual
def puntaje(juegoactual):
	if juegoactual == 'principal_j':
		score_surface = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)
	if juegoactual == 'game_over':
		score_surface = game_font.render(f'Puntuacion: {int(score)}' ,True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)

		high_score_surface = game_font.render(f'Puntaje mas alto: {int(high_score)}',True,(255,255,255))
		high_score_rect = high_score_surface.get_rect(center = (288,850))
		screen.blit(high_score_surface,high_score_rect)

#Almacena el puntaje más alto de la sesión, no fue posible conectarlo con DB, posble para versión 2.1
def puntaje_jn(score, high_score):
	if score > high_score:
		high_score = score
	return high_score

def operacion():
		operacion1 = game_font.render('oper'),True,(255,255,255)
		operacion1r = score_surface.get_rect(center = (288,100))
		screen.blit(operacion1,operacion1r)





#Se realiza el llamado a Pygame y se dispone de resolución, audio y se importa la fuente.
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

#Variables
gravity = 0.50
mathp_movement = 0
game_active = True
score = 0
oper = 0
high_score = 0

bg_surface = pygame.image.load('archivos/fondo.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

opr1 = pygame.image.load('archivos/opr1.png').convert()
opr1 = pygame.transform.scale2x(opr1)

#r0 = pygame.image.load('archivos/0.png').convert()
#r0 = pygame.transform.scale2x(r1)
#r0pos = 0

#r1 = pygame.image.load('archivos/1.png').convert()
#r1 = pygame.transform.scale2x(r1)
#r1pos = 0

#r2 = pygame.image.load('archivos/2.png').convert()
#r2 = pygame.transform.scale2x(r1)
#r2pos = 0

#r3 = pygame.image.load('archivos/3.png').convert()
#r3 = pygame.transform.scale2x(r1)
#r3pos = 0

#r4 = pygame.image.load('archivos/4.png').convert()
#r4 = pygame.transform.scale2x(r1)
#r4pos = 0

#r5 = pygame.image.load('archivos/5.png').convert()
#r5 = pygame.transform.scale2x(r1)
#r5pos = 0

#r6 = pygame.image.load('archivos/6.png').convert()
#r6 = pygame.transform.scale2x(r1)
#r6pos = 0

#r7 = pygame.image.load('archivos/7.png').convert()
#r7 = pygame.transform.scale2x(r1)
#r7pos = 0

#r8 = pygame.image.load('archivos/8.png').convert()
#r8 = pygame.transform.scale2x(r1)
#r8pos = 0

#r9 = pygame.image.load('archivos/9.png').convert()
#r9 = pygame.transform.scale2x(r1)
#r9pos = 0

piso_sf = pygame.image.load('archivos/base.png').convert()
piso_sf = pygame.transform.scale2x(piso_sf)
piso_x_pos = 0



mathp_downflap = pygame.transform.scale2x(pygame.image.load('archivos/mateabajo.png').convert_alpha())
mathp_midflap = pygame.transform.scale2x(pygame.image.load('archivos/matemedio.png').convert_alpha())
mathp_upflap = pygame.transform.scale2x(pygame.image.load('archivos/matearriba.png').convert_alpha())
mathp_frames = [mathp_downflap,mathp_midflap,mathp_upflap]
mathp_index = 0
mathp_surface = mathp_frames[mathp_index]
mathp_rect = mathp_surface.get_rect(center = (100,512))

mathpFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(mathpFLAP,200)

#Tubos en juego, altura, generador, etc

superficie_t = pygame.image.load('archivos/tverde.png')
superficie_t = pygame.transform.scale2x(superficie_t)
tubo_list = []
SPAWNtubo = pygame.USEREVENT
pygame.time.set_timer(SPAWNtubo,1200)
tubo_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('archivos/menu.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))

vuela_s = pygame.mixer.Sound('sound/sfx_wing.wav')
muerte_s = pygame.mixer.Sound('sound/sfx_hit.wav')
musica_s = pygame.mixer.Sound('sound/sfx_point.wav')
musica_s_countdown = 100

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				mathp_movement = 0
				mathp_movement -= 12
				vuela_s.play()
				#xxx()

			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				tubo_list.clear()
				mathp_rect.center = (100,512)
				mathp_movement = 0
				score = 0

		if event.type == SPAWNtubo:
			tubo_list.extend(creador_tubo())

		if event.type == mathpFLAP:
			if mathp_index < 2:
				mathp_index += 1
			else:
				mathp_index = 0

			mathp_surface,mathp_rect = movimiento_mathp()
	
	screen.blit(bg_surface,(0,0))
	#screen.blit(opr1,(0,0))

	if game_active:
		# mathp
		mathp_movement += gravity
		rotated_mathp = rotar_mathp(mathp_surface)
		mathp_rect.centery += mathp_movement
		screen.blit(rotated_mathp,mathp_rect)
		game_active = jugador_falla(tubo_list)

		# tubos
		tubo_list = tubosmovim(tubo_list)
		tubo_list = retubosmovim(tubo_list)
		tuboscrea(tubo_list)
		

		score += 0.01
		puntaje('principal_j')
		musica_s_countdown -= 1
		if musica_s_countdown <= 0:
			musica_s.play()
			musica_s_countdown = 100
	else:
		screen.blit(game_over_surface,game_over_rect)
		high_score = puntaje_jn(score,high_score)
		puntaje('game_over')


	#Piso en movimiento, uso de creador_piso
	piso_x_pos -= 1
	creador_piso()
	if piso_x_pos <= -576:
		piso_x_pos = 0

	

	pygame.display.update()
	clock.tick(120)
		

