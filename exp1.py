# Importe la bibliothèque Turtle qui permet de dessiner avec une tortue graphique.
import turtle

# Importe la bibliothèque Random.
# Elle permet de générer des valeurs aléatoires.
# Dans ce programme elle n'est pas utilisée, mais elle pourrait servir
# à choisir des couleurs ou des tailles au hasard.
import random

# Configuration de la fenêtre

# Crée la fenêtre de dessin.
screen = turtle.Screen()

# Définit la couleur de fond de la fenêtre en noir.
screen.bgcolor("black")

# Création de la tortue

# Crée la tortue qui va dessiner à l'écran.
t = turtle.Turtle()

# Définit la vitesse maximale de dessin.
# 0 correspond à la vitesse la plus rapide.
t.speed(0)

# Définit l'épaisseur du trait à 2 pixels.
t.width(2)

# Liste des couleurs

# Liste contenant les couleurs utilisées pour les pétales.
couleurs = [
    "red",      # rouge
    "orange",   # orange
    "yellow",   # jaune
    "lime",     # vert clair
   # "cyan",     # bleu clair
  #  "blue",     # bleu
    #"magenta",  # violet/rose
    #"pink"      # rose
]

# Fonction pétale

# Fonction qui dessine un pétale.
# Le paramètre "taille" contrôle la taille du pétale.
def petale(taille):

    # Répète les instructions suivantes 2 fois.
    for _ in range(2):

        # Dessine un arc de cercle.
        # taille = rayon du cercle
        # 60 = angle parcouru
        t.circle(taille, 60)

        # Tourne la tortue de 120 degrés vers la gauche.
        t.left(120)

# Fonction fleur

# Fonction qui dessine une fleur complète.
# nb_petales = nombre de pétales
# taille = taille des pétales
def fleur(nb_petales, taille):

    # Répète le dessin du pétale autant de fois que nécessaire.
    for i in range(nb_petales):

        # Choisit une couleur dans la liste.
        # L'opérateur % permet de recommencer au début de la liste
        # lorsque toutes les couleurs ont été utilisées.
        t.color(couleurs[i % len(couleurs)])

        # Dessine un pétale.
        petale(taille)

        # Tourne la tortue pour placer le pétale suivant.
        # 360 représente un tour complet.
        t.left(360 / nb_petales)

# Dessin principal

# La variable rayon prend successivement les valeurs :
# 20, 40, 60, 80 et 100
for rayon in range(20, 120, 20):

    # Dessine une fleur de 12 pétales.
    # Les fleurs deviennent progressivement plus grandes.
    fleur(12, rayon)

# Dessin du centre de la fleur

# Soulève le stylo pour se déplacer sans dessiner.
t.penup()

# Déplace la tortue près du centre de la fleur.
t.goto(0, -15)

# Repose le stylo pour recommencer à dessiner.
t.pendown()

# Choisit la couleur blanche.
t.color("white")

# Commence une forme remplie.
t.begin_fill()

# Dessine un cercle de rayon 15.
# Ce cercle représente le cœur de la fleur.
t.circle(10)

# Remplit le cercle avec la couleur blanche.
t.end_fill()

# Fin du programme

# Cache la tortue pour afficher uniquement le dessin.
t.hideturtle()

# Laisse la fenêtre ouverte à la fin du programme.
turtle.done()