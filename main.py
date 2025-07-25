import sys
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()           # Initialise tous les modules de Pygame nécessaires.
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # to get a new GUI window
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)              # fabriques un vaisseau spatial en creant une instance (objet) de Player


    # --- Initialisation pour la gestion du temps et du FPS (Frames Per Second) ---    dt = 0
    Clock = pygame.time.Clock()  # Crée un objet Clock pour aider à gérer le temps et le framerate du jeu
    dt = 0                      # Initialize dt before the game loop


    # Gestion des événements (pour pouvoir fermer la fenêtre)
    while True:              
        for event in pygame.event.get():  # Pour chaque événement dans la liste des événements
            if event.type == pygame.QUIT:  # Si ce type d'événement est "fermeture de fenêtre"
                return                  # Alors on sort de la fonction
   
        # Met à jour la position/rotation du vaisseau
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for shot in shots:
            if asteroid.collides_with(shot):
                shot.kill()
                asteroid.split()

        # Efface l'écran en le remplissant de noir à chaque nouvelle frame
        screen.fill("black") 

        # Dessine le vaisseau a sa nouvelle position (appelle la méthode draw pour que le vaisseau (player) soit rafraîchi constamment sur l'écran)
        for obj in drawable:
            obj.draw(screen)

        # Affiche tout a l'ecran (Rafraîchir l'écran pour afficher tout ce qui a été dessiné)
        pygame.display.flip()

        dt = (Clock.tick(60) / 1000)    # --- Calcul du Delta Time et régulation du Framerate --- Clock.tick(60) : Limite le jeu à un maximum de 60 images par seconde (FPS). / 1000       : Convertit le temps (en millisecondes) en secondes pour faciliter les calculs de mouvement

# Point d'entrée du programme
if __name__ == "__main__":      # Cette condition assure que main() est appelée seulement si le script est exécuté directement
    main()

