# Importe la bibliothèque Turtle qui permet de réaliser des dessins.
import turtle

# Crée la tortue qui va dessiner la spirale.
t = turtle.Turtle()

# Définit la vitesse maximale du dessin.
t.speed(0)

# Définit la couleur de fond de la fenêtre en noir.
turtle.bgcolor("black")

# Crée une liste contenant les couleurs utilisées pour le dessin.
couleurs = ["cyan", "magenta", "yellow", "orange"]

# Boucle principale répétée 180 fois.
for i in range(180):

    # Change la couleur du trait.
    # Le modulo (%) permet de revenir au début de la liste
    # lorsque toutes les couleurs ont déjà été utilisées.
    t.color(couleurs[i % len(couleurs)])

    # Fait avancer la tortue.
    # La distance parcourue augmente progressivement :
    # 0, 1.5, 3.0, 4.5, 6.0, ...
    t.forward(i * 1.5)

    # Tourne la tortue de 121 degrés vers la gauche.
    t.left(121)

# Maintient la fenêtre ouverte à la fin du programme.
turtle.done()