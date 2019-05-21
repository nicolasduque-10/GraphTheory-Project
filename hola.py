import pygame
import math
pygame.init()
from pygame import font as pygame_font
#-------------------------------------------------------------
#funciones
def distance((a,b),(c,d)):
	d1 = pow(a-c,2)
	d2 = pow(b-d,2)
	d3 = d1 + d2
	d4 = math.sqrt(d3)
	d5 = (0.03)*d4
	return d5

def text_objects(text, font, colour):
	TextSurface = font.render(text, True, colour)
	return TextSurface, TextSurface.get_rect()

def mensaje_en_pantalla(text, x, y):
	largeText = pygame.font.Font('freesansbold.ttf', 15)
	TextSurf, TextRect = text_objects(text, largeText, (255, 255, 255))
	TextRect.center = ((x), (y))
	grafos.blit(TextSurf, TextRect)

def crear_punto(i):
	if x1 == 1:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		pygame.draw.circle(grafos, (72, 201, 176), (x,y), 15)
		str_num = str(i)
		mensaje_en_pantalla(str_num, x-20, y-20)
	return (x,y)

vertex = []
vertex_emb = []
edges = []
distances = []
vertex_upper = -1
v = 1
v1 = 1
finish = 0

#--------------------------------------------------------------
#Comienzo interfaz grafica 1
grafos = pygame.display.set_mode((1700, 1500))
pygame.display.set_caption("Poligono")

#Color background
grafos.fill((33, 47, 61))

run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	#dibujo del boton
	pygame.draw.rect(grafos, (0, 0, 0), (730, 920, 380, 60))
	mensaje_en_pantalla("DAR CLICK DOS VECES PARA EL EMBEBIMIENTO", 922, 950)

	#dibujo del grafo.
	x1, x2, x3 = pygame.mouse.get_pressed()

	if x1 == 1 and (vertex_upper + 1, 1) not in edges:
		if crear_punto(v) not in vertex:
			vertex_upper = vertex_upper + 1
			vertex.append(crear_punto(v))
			v = v + 1

			if vertex_upper != 0:
				pygame.draw.line(grafos, (142, 68, 173), vertex[vertex_upper - 1], vertex[vertex_upper], 4)
				edges.append((vertex_upper, vertex_upper + 1))
				distances.append(distance(vertex[vertex_upper - 1], vertex[vertex_upper]))

			print "V(G) = ", vertex
			print "E(G) = ", edges
			print "D = ", distances
			print "----------------------------------"

	#Acaba poligono
	if x3 == 1 and len(vertex) > 2:
		if (vertex_upper + 1, 1) not in edges:
			pygame.draw.line(grafos, (142, 68, 173), vertex[vertex_upper], vertex[0], 4)
			edges.append((vertex_upper + 1, 1))
			distances.append(distance(vertex[vertex_upper], vertex[0]))

			finish = finish + 1

			print "V(G) = ", vertex
			print "E(G) = ", edges
			print "D = ", distances
			print "----------------------------------"

	#paso al embebimiento
	if x1 == 1 and finish != 0:
		xa = pygame.mouse.get_pos()[0]
		ya = pygame.mouse.get_pos()[1]

		if 730 < xa and xa < 1110 and 920 < ya and ya < 980:
			 grafos.fill((255,255,255))

			 for i in range(1, 40):
				 pygame.draw.line(grafos, (213, 216, 220), (50*i, 0), (50*i, 1500), 4)
				 pygame.draw.line(grafos, (213, 216, 220), (0, 50*i), (1700, 50*i), 4)

			 pygame.draw.line(grafos, (0,0,0), (50, 0), (50, 1500), 4)
			 pygame.draw.line(grafos, (0,0,0), (0, 1000), (1700, 1000), 4)

		#vertices
		for i in vertex:
			xaprox = i[0]%50
			yaprox = i[1]%50

			if xaprox <= 25 and yaprox <= 25:
				pygame.draw.circle(grafos, (72, 201, 176), (i[0] - xaprox, i[1] - yaprox), 15)
				vertex_emb.append((i[0] - xaprox, i[1] - yaprox))

			elif xaprox <= 25 and yaprox >= 25:
				pygame.draw.circle(grafos, (72, 201, 176), (i[0] - xaprox, i[1] + 50 - yaprox), 15)
				vertex_emb.append((i[0] - xaprox, i[1] + 50 - yaprox))

			elif xaprox >= 25 and yaprox >= 25:
				pygame.draw.circle(grafos, (72, 201, 176), (i[0] + 50 - xaprox, i[1] + 50 - yaprox), 15)
				vertex_emb.append((i[0] + 50 - xaprox, i[1] + 50 - yaprox))


			elif xaprox >= 25 and yaprox <= 25:
				pygame.draw.circle(grafos, (72, 201, 176), (i[0] + 50 - xaprox, i[1] - yaprox), 15)
				vertex_emb.append((i[0] + 50 - xaprox, i[1] - yaprox))

		print vertex_emb

		#aristas
		for i in range(0, len(vertex_emb) - 1):
			pygame.draw.line(grafos, (142, 68, 173), vertex_emb[i+1], vertex_emb[i], 4)

		#conteo
		xl = []
		yl =[]
		for i in vertex_emb:
			xl.append(i[0])
			yl.append(i[1])

		for i in range(1, len(xl) - 1):
			menorx = 345340
			if xl[i-1] <= xl[i]:
				menorx = xl[i-1]

		for i in range(1, len(yl) - 1):
			menort = 90000
			if yl[i-1] <= yl[i]:
				menory = yl[i-1]

		for i in range(1, len(xl) - 1):
			mayorx =0
			if xl[i-1] >= xl[i]:
				mayorx = xl[i-1]

		for i in range(1, len(yl) - 1):
			mayory =0
			if yl[i-1] >= yl[i]:
				mayory = yl[i-1]

		print menorx, menory, mayorx, mayory







	pygame.display.update()


pygame.quit()
