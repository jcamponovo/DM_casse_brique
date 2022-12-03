"""--------------------------------------------------------------------------
Jeu de Casse_Brique
    Baptiste PECOURT 1ère3
    Version 6.0 - 03/12/2022
      - Bug suppression brique
      - fonction math de pyxel
      - augmentation de la vitesse tous les 5 niveaux
      - affichage aide
    Version 5.0 - 03/12/2022
      - Ajout de niveau de jeu
      - Ref couleurs pyxel
    Version 4.0 - 03/12/2022
      - 5 lignes de briques
    Version 3.1 - 03/12/2022
      - gestion plus fine du bord de balle
    Version 3.0 - 03/12/2022
      - Angle vitesse sur les cotés plateau
      - Réinit du jeu
    Version 2.0 - 03/12/2022
      - Vitesse incrémentale
--------------------------------------------------------------------------"""
import pyxel

"""--------------------------------------------------------------------------
                                CONSTANTES
--------------------------------------------------------------------------"""

""" COULEUR """
# couleur standard pyxel
"""
COLOR_BLACK: 0
COLOR_NAVY: 1
COLOR_PURPLE: 2
COLOR_GREEN: 3
COLOR_BROWN: 4
COLOR_DARK_BLUE: 5
COLOR_LIGHT_BLUE: 6
COLOR_WHITE: 7
COLOR_RED: 8
COLOR_ORANGE: 9
COLOR_YELLOW: 10
COLOR_LIME: 11
COLOR_CYAN: 12
COLOR_GRAY: 13
COLOR_PINK: 14
COLOR_PEACH: 15
"""

""" ECRAN """
# taille de la fenetre
WIN_WITDH = 300
WIN_HEIGHT = 300

""" BALLE """
# couleur de la balle
BALLE_COLOR = pyxel.COLOR_RED #v5.0
# rayon de la balle
BALLE_RAYON = 4
# vitesse balle
BALLE_VITESSE = 5
BALLE_VITESSE_FACTEUR = 1.2 #v5.0
# 1 sur racine carrée de 2
SQR2 = (1 / (2 ** 0.5)) #v3.0

""" PLATEAU """
PLATEAU_COLOR = pyxel.COLOR_CYAN #v5.0
# taille du plateau
PLATEAU_WITDH = 50
PLATEAU_DECREMENT = 10 #v5.0 décrement de la taille a chaque niveau de jeu
PLATEAU_HEIGHT = 10 #v3.0
PLATEAU_BORD = (2 * PLATEAU_HEIGHT) #v3.0
PLATEAU_HEIGHT2 = (BALLE_VITESSE * (BALLE_VITESSE_FACTEUR ** 2)) #v2.0
# position initiale plateau au centre
# (origine des positions : coin haut gauche)
PLATEAU_X = ((WIN_WITDH - PLATEAU_WITDH) / 2)
PLATEAU_Y = 250
# vitesse du plateau
PLATEAU_VITESSE = 10

""" BRIQUES """
# nombre de briques
BRIQUE_N_LIGNES = 5 # un type par ligne #v4.0
BRIQUE_N_COLONNES = 10 #v3.0
BRIQUE_N = (BRIQUE_N_LIGNES * BRIQUE_N_COLONNES)
# couleurs des briques, une couleur par type
BRIQUE_SUPPRIMER = 0 #v5.0
BRIQUE_COLOR = [pyxel.COLOR_WHITE, pyxel.COLOR_RED, pyxel.COLOR_YELLOW, pyxel.COLOR_LIME, pyxel.COLOR_DARK_BLUE] #v5.0
# score brique par type
BRIQUE_SCORE = [50, 40, 30, 20, 10] #v4.0
# taille des briques
BRIQUE_INTERVAL = 4
BRIQUE_WITDH = (WIN_WITDH / BRIQUE_N_COLONNES - BRIQUE_INTERVAL)
BRIQUE_HEIGHT = 10
# position des briques
BRIQUE_X = (BRIQUE_INTERVAL / 2)
BRIQUE_Y = 30

""" TEXTES """
# couleur des textes
TEXTE_COLOR = pyxel.COLOR_WHITE
# position des textes
SCORE_X, SCORE_Y = 20, 10
NIV_X, NIV_Y = (WIN_WITDH / 2 - 20), 10 # v5.0
VIES_X, VIES_Y = (WIN_WITDH - 50), 10
GAME_OVER_X, GAME_OVER_Y = (WIN_WITDH / 2 - 18), (WIN_HEIGHT / 2)
VIES_MSG_X, VIES_MSG_Y = (WIN_WITDH / 2 - 32), (WIN_HEIGHT / 2 + 20)
AIDE_X, AIDE_Y = (WIN_WITDH / 2 - 140), (WIN_HEIGHT / 2 + 20)

""" JEU """
VIES_DEBUT = 3

"""--------------------------------------------------------------------------
                                FONCTIONS
--------------------------------------------------------------------------"""
    
"""
    Gestion du déplacement du plateau en fonction des touches flèches
"""
def plateau_deplacement():
    global p_x, p_y
    # touche fleche gauche
    if pyxel.btn(pyxel.KEY_LEFT):
        if (p_x - PLATEAU_BORD >= PLATEAU_VITESSE):
            p_x = p_x - PLATEAU_VITESSE
    # touche fleche droite
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (p_x + p_witdh + PLATEAU_BORD <= WIN_WITDH - PLATEAU_VITESSE): #v5.0
            p_x = p_x + PLATEAU_VITESSE
            
"""
    Paramètres initiaux de la balle à chaque session
"""
def balle_initialisation():
    global b_x, b_y, b_vx, b_vy, balle_active
    # activation balle (inactive au départ)
    balle_active = False
    # position initiale de la balle
    b_x = p_x + (p_witdh + BALLE_RAYON) / 2 #v5.0
    b_y = p_y - (BALLE_RAYON + 1)
    # vitesse initiale de la balle aléatoire en x de 50 à 100% de V
    b_vx = pyxel.floor(pyxel.rndf(0.5, 1.0) * BALLE_VITESSE) #v6.0
    b_vx *= 2 * pyxel.rndi(0, 1) - 1 #v6.0 signe pos ou neg
    # complement Vy pour avoir un module = BALLE_VITESSE
    b_vy = -((BALLE_VITESSE ** 2 - b_vx ** 2) ** 0.5)
    
"""
    Gestion deplacement de la balle et détection des collisions
"""
def balle_deplacement():
    global b_x, b_y, b_vx, b_vy, balle_active, score, brique_n
    # pas de fin de partie par défaut
    fin_partie = False
    # déplacement de la balle
    b_x += b_vx
    b_y += b_vy
    # collision bord gauche
    if b_x - BALLE_RAYON <= 0 and b_vx < 0: #v5.0
        b_vx = -b_vx
    # collision bord haut
    elif b_y - BALLE_RAYON <= 0 and b_vy < 0: #v5.0
        b_vy = -b_vy
    # collision bord droit
    elif b_x + BALLE_RAYON >= WIN_HEIGHT and b_vx > 0: #v5.0
        b_vx = -b_vx
    # collision dessus plateau
    elif b_x + BALLE_RAYON >= p_x and b_x - BALLE_RAYON <= p_x + p_witdh and b_y + BALLE_RAYON >= p_y and b_y - BALLE_RAYON <= p_y and b_vy > 0: #v3.1 #v5.0
        b_vy = -b_vy
    # collision coté gauche plateau
    elif b_x + BALLE_RAYON >= p_x - PLATEAU_BORD and b_x - BALLE_RAYON <= p_x and b_y + BALLE_RAYON >= p_y and b_y - BALLE_RAYON <= p_y + PLATEAU_HEIGHT + PLATEAU_HEIGHT2 and pyxel.pget(b_x + b_vx, b_y + b_vy) == PLATEAU_COLOR: #v3.1
        b_vx, b_vy = SQR2 * (b_vx - b_vy), -SQR2 * (b_vx + b_vy) #v3.0
    # collision coté droit plateau
    elif b_x + BALLE_RAYON >= p_x + p_witdh and b_x - BALLE_RAYON <= p_x + p_witdh + PLATEAU_BORD and b_y + BALLE_RAYON >= p_y and b_y - BALLE_RAYON <= p_y + PLATEAU_HEIGHT + PLATEAU_HEIGHT2 and pyxel.pget(b_x + b_vx, b_y + b_vy) == PLATEAU_COLOR: #v3.1 #v5.0
        b_vx, b_vy = SQR2 * (b_vx + b_vy), SQR2 * (b_vx - b_vy) #v3.0
    # collision bord bas
    elif b_y - BALLE_RAYON >= WIN_HEIGHT:
        fin_partie = True
    # collision avec brique type n
    else:
        for i in range(BRIQUE_N_LIGNES):
            if pyxel.pget(b_x + b_vx, b_y + b_vy) == BRIQUE_COLOR[i]:
                j = pyxel.floor((b_x + b_vx) / (BRIQUE_WITDH + BRIQUE_INTERVAL))
                if j >= 0 and j < BRIQUE_N_COLONNES:
                    if brique_color[i][j] > 0: #v6.0 si pas déjà supprimer
                        brique_color[i][j] = BRIQUE_SUPPRIMER 
                        brique_n += 1
                        b_vy = -b_vy
                        score += BRIQUE_SCORE[i]
                        #v2.0 si derniere brique de la ligne
                        # alors incrémentation de la vitesse
                        sum = 0
                        for c in range(BRIQUE_N_COLONNES):
                            sum += brique_color[i][c]
                        if sum == 0:
                            b_vx *= BALLE_VITESSE_FACTEUR
                            b_vy *= BALLE_VITESSE_FACTEUR
                        break #v3.1 une seule brique supprimée
    return fin_partie
                
"""
    UPDATE POUR PYXEL RUN
    mise à jour des variables avant l'appel de DRAW
"""
def update():
    global balle_active, vies, niveau, aide
    if balle_active: # si balle active
        # mise à jour de la position du plateau
        plateau_deplacement()
        # mise à jour du jeu
        if balle_deplacement(): # si session perdue
            if vies > 0: #v3.0 # si reste des vies
                vies = vies - 1
                balle_initialisation()
            else: #v5.0 game over réinit du jeu
                niveau = 0
                initialisation()
        if brique_n == BRIQUE_N: # si fin de partie gagné
            #v5.0 incrément du niveau
            balle_active = False
            niveau += 1
            initialisation()
    else: # balle inactive
        #v5.0 réinit avec niveau
        if pyxel.btnr(pyxel.KEY_SPACE):
            # lancement de la session
            balle_active = True
            aide = False

"""
    DRAW POUR PYXEL RUN 
    redessine les objets (30 fois par seconde)
"""
def draw():
    # vide la fenetre
    pyxel.cls(0)
    # textes
    pyxel.text(SCORE_X, SCORE_Y, 'SCORE: %d' % score, TEXTE_COLOR)
    pyxel.text(NIV_X, NIV_Y, 'NIVEAU: %d' % niveau, TEXTE_COLOR)
    pyxel.text(VIES_X, VIES_Y, 'VIES: %d' % vies, TEXTE_COLOR)
    if aide:
        pyxel.text(AIDE_X, AIDE_Y, 'Touches : <- ou -> pour bouger la raquette, ESPACE pour lancer le jeu', TEXTE_COLOR)
    # s'il reste des vies le jeu continue
    if vies > 0:    
        # plateau : carré central, coins gauche et droit, puis base
        pyxel.rect(p_x, p_y, p_witdh, PLATEAU_HEIGHT, PLATEAU_COLOR) #v5.0
        pyxel.tri(p_x, p_y, p_x, p_y + PLATEAU_HEIGHT, p_x - PLATEAU_BORD, p_y + PLATEAU_HEIGHT, PLATEAU_COLOR)
        pyxel.tri(p_x + p_witdh, p_y, p_x + p_witdh, p_y + PLATEAU_HEIGHT, p_x + p_witdh + PLATEAU_BORD, p_y + PLATEAU_HEIGHT, PLATEAU_COLOR) #v5.0
        pyxel.rect(p_x - PLATEAU_BORD, p_y + PLATEAU_HEIGHT, p_witdh + 2 * PLATEAU_BORD + 1, PLATEAU_HEIGHT2, PLATEAU_COLOR) #v2.0 #v5.0
        # balle
        pyxel.circ(b_x, b_y, BALLE_RAYON, BALLE_COLOR)
        # briques
        for i in range(BRIQUE_N_LIGNES):
            for j in range(BRIQUE_N_COLONNES):
                if brique_color[i][j] != BRIQUE_SUPPRIMER:
                    pyxel.rect(BRIQUE_X + j * (BRIQUE_WITDH + BRIQUE_INTERVAL), BRIQUE_Y + i * (BRIQUE_HEIGHT + BRIQUE_INTERVAL), BRIQUE_WITDH, BRIQUE_HEIGHT, brique_color[i][j])
        #v5.0 affichage message de fin de partie
        if vies < VIES_DEBUT and not balle_active:
            pyxel.text(VIES_MSG_X, VIES_MSG_Y, 'UNE VIE DE MOINS !', TEXTE_COLOR)
        if brique_n == BRIQUE_N: # fin de partie gagné
            pyxel.text(GAME_OVER_X, GAME_OVER_Y, '* NIV %d *' % niveau, TEXTE_COLOR) #v5.0
    else: # sinon (vies == 0): GAME OVER
        pyxel.text(GAME_OVER_X, GAME_OVER_Y, 'GAME OVER', TEXTE_COLOR)

"""
    Initialisation des paramètres du jeu
"""
def initialisation():
    global score, vies, brique_n, p_x, p_y, b_vx, b_vy, brique_color, p_witdh #v6.0
    # score et vies
    if niveau == 0: #v5.0
        score = 0
    vies = VIES_DEBUT
    # nombre de brique détruite
    brique_n = 0
    # position initiale du plateau
    p_x, p_y = PLATEAU_X, PLATEAU_Y
    #v5.0 taille plateau
    p_witdh = PLATEAU_WITDH - niveau * PLATEAU_DECREMENT
    if p_witdh < 0:
        p_witdh = 0
    # initialisation de la balle
    balle_initialisation()
    # augmentation de la vitesse tous les 5 niveaux
    n = pyxel.floor(niveau / 5)
    b_vx *= BALLE_VITESSE_FACTEUR ** n
    b_vy *= BALLE_VITESSE_FACTEUR ** n
    # creation des briques
    brique_color = [[BRIQUE_COLOR[i]] * BRIQUE_N_COLONNES for i in range(BRIQUE_N_LIGNES)]

"""--------------------------------------------------------------------------
                                    MAIN
--------------------------------------------------------------------------"""
#v5.0 niveau de jeu
niveau = 0
# création de la fenêtre du jeu
pyxel.init(WIN_WITDH, WIN_HEIGHT, title="Casse Brique")
# affiche l'aide
aide = True 
# init des paramètres du jeu
initialisation()
# boucle infini du jeu
pyxel.run(update, draw)
