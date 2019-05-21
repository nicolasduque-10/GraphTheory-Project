import pygame
import math
pygame.init()
from pygame import font as pygame_font 
#-------------------------------------------------------------
def crear_punto():
	if x1 == 1:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		pygame.draw.circle(grafos, (255, 45, 60), (x,y), 5)
	return (x,y)

def distance((a,b),(c,d)):
	d1 = pow(a-c,2)
	d2 = pow(b-d,2)
	d3 = d1 + d2
	d4 = math.sqrt(d3)
	d5 = (0.03)*d4
	return d5

vertex = []
edges = []
distances = []
vertex_upper = -1

#--------------------------------------------------------------
grafos = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teorema de Pick")

run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render('HOLAAAAAAAAAAAAAAAA MUNDOOOOO', False, (0,0,0))
	grafos.blit(textsurface, (0,0))

	x1, x2, x3 = pygame.mouse.get_pressed()
	
	if x1 == 1 and (vertex_upper + 1, 1) not in edges:
		if crear_punto() not in vertex:	
			vertex_upper = vertex_upper + 1
			vertex.append(crear_punto())
		
			if vertex_upper != 0:
				pygame.draw.line(grafos, (255, 255, 255), vertex[vertex_upper - 1], vertex[vertex_upper], 2)
				edges.append((vertex_upper, vertex_upper + 1))
				if vertex_upper > 1:
					n = distance(edges[vertex_upper - 2], edges[vertex_upper - 1])
					distances.append(n)

			print "V(G) = ", vertex
			print "E(G) = ", edges
			print "D = ", distances
			print "----------------------------------"

	if x3 == 1 and len(vertex) > 2:
		if (vertex_upper + 1, 1) not in edges:
			pygame.draw.line(grafos, (255, 255, 255), vertex[vertex_upper], vertex[0], 2)
			edges.append((vertex_upper + 1, 1))
		
			print "V(G) = ", vertex
			print "E(G) = ", edges
			print "----------------------------------"

			pygame.event.clear()

	f = pygame_font.Font(None, 20)
	s = f.render("foo", True, (0,0, 0), (255, 255, 255))
    
	pygame.display.update()

pygame.quit()