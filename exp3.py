# Importe la bibliothèque Turtle qui permet de dessiner.
import turtle

# Crée la tortue qui va faire le dessin.
t = turtle.Turtle()

# Met la vitesse du dessin au maximum.
t.speed(0)

# Change la couleur de fond de la fenêtre.
turtle.bgcolor("navy")

# Tourne la tortue vers le haut.
# Sans cette ligne, elle regarderait vers la droite.
t.left(90)

# Soulève le stylo pour déplacer la tortue sans dessiner.
t.penup()

# Déplace la tortue en bas de la fenêtre.
# C'est ici que commencera le tronc de l'arbre.
t.goto(0, -250)

# Repose le stylo pour pouvoir dessiner.
t.pendown()

# Liste des couleurs utilisées dans l'arbre.
couleurs = ["brown", "green", "lime"]

# Fonction qui dessine l'arbre.
# longueur = taille de la branche.
# niveau = nombre de divisions de l'arbre.
def arbre(longueur, niveau):

    # Si le niveau arrive à 0,
    # on arrête de créer des branches.
    if niveau == 0:
        return

    # Choisit une couleur dans la liste.
    t.color(couleurs[niveau % len(couleurs)])

    # Dessine une branche vers l'avant.
    t.forward(longueur)

    # Tourne à gauche pour créer une branche.
    t.left(35)

    # Dessine une branche plus petite.
    arbre(longueur * 0.75, niveau - 1)

    # Tourne à droite pour créer l'autre branche.
    t.right(70)

    # Dessine encore une branche plus petite.
    arbre(longueur * 0.75, niveau - 1)

    # Remet la tortue dans sa direction de départ.
    t.left(35)

    # Revient en arrière jusqu'au début de la branche.
    t.backward(longueur)

# Lance le dessin de l'arbre.
# Tronc de 120 pixels et niveau 8.
arbre(120, 8)

# Cache la tortue quand le dessin est terminé.
t.hideturtle()

# Garde la fenêtre ouverte.
turtle.done()