import random # Pour les tirages aleatoires
import sys # Pour quitter proprement
import pygame # Le module Pygame
import pygame.freetype # Pour afficher du texte
import math
pygame.init() # initialisation de Pygame
# Pour le texte.
pygame.freetype.init()
myfont=pygame.freetype.SysFont(None, 20) # texte de taille 20
# Taille de la fenetre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping")
# Pour limiter le nombre d'images par seconde
clock=pygame.time.Clock()
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
RAYON_BALLE = 10
XMIN, YMIN = 0, 0
XMAX, YMAX = width, height


class Balle:
def vitesse_par_angle(self, angle):
self.vx = self.vitesse * math.cos(math.radians(angle))
self.vy = -self.vitesse * math.sin(math.radians(angle))
def __init__(self):
self.x, self.y = (400, 400)
self.vitesse = 8 # vitesse initiale
self.vitesse_par_angle(60) # vecteur vitesse
def afficher(self):
pygame.draw.rect(screen, BLANC,

(int(self.x-RAYON_BALLE), int(self.y-RAYON_BALLE),
2*RAYON_BALLE, 2*RAYON_BALLE), 0)

def deplacer(self):
self.x += self.vx
self.y += self.vy
if self.x + RAYON_BALLE > XMAX:
self.vx = -self.vx
if self.x - RAYON_BALLE < XMIN:
self.vx = -self.vx
if self.y + RAYON_BALLE > YMAX:
self.vy = -self.vy
if self.y - RAYON_BALLE < YMIN:
  
  jeu = Jeu()
while True:
jeu.gestion_evenements()
jeu.mise_a_jour()
jeu.affichage()
pygame.display.flip() # envoi de l'image à la carte graphique
clock.tick(60) # on attend pour ne pas dépasser 60 images/seconde
self.vy = -self.vy


class Jeu:
def __init__(self):
self.balle = Balle()
def gestion_evenements(self):
# Gestion des evenements
for event in pygame.event.get():
if event.type == pygame.QUIT: sys.exit() # Pour quitter

def mise_a_jour(self):
self.balle.deplacer()
def affichage(self):
screen.fill(NOIR) # on efface l'écran
self.balle.afficher()

class Raquette:
def __init__(self):
self.x = (XMIN+XMAX)/2
self.y = YMAX - RAYON_BALLE
self.longueur = 10*RAYON_BALLE
def afficher(self):
pygame.draw.rect(screen, BLANC,

(int(self.x-self.longueur/2), int(self.y-RAYON_BALLE),
self.longueur, 2*RAYON_BALLE), 0)

def deplacer(self, x):
if x - self.longueur/2 < XMIN:
self.x = XMIN + self.longueur/2
elif x + self.longueur/2 > XMAX:
self.x = XMAX - self.longueur/2
else:
self.x = x

class Jeu:
def __init__(self):
self.balle = Balle()
self.raquette = Raquette()
def mise_a_jour(self):
x, y = pygame.mouse.get_pos()
self.balle.deplacer()
self.raquette.deplacer(x)
def affichage(self):
screen.fill(NOIR) # on efface l'écran
self.balle.afficher()
self.raquette.afficher()

class Balle:
...
def deplacer(self, raquette):
self.x += self.vx
self.y += self.vy
if raquette.collision_balle(self):
self.vy = -self.vy
if self.x + RAYON_BALLE > XMAX:
self.vx = -self.vx
...
class Raquette:
...
def collision_balle(self, balle):
vertical = abs(self.y - balle.y) < 2*RAYON_BALLE
horizontal = abs(self.x - balle.x) < self.longueur/2 + RAYON_BALLE
return vertical and horizontal

class Jeu:
...
def mise_a_jour(self):
x, y = pygame.mouse.get_pos()
self.balle.deplacer(self.raquette)
self.raquette.deplacer(x)
