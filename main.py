import pygame
from constants import * 

def main():
    pygame.init()           # Initialise tous les modules de Pygame nécessaires.
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # to get a new GUI window
    
    # --- Initialisation pour la gestion du temps et du FPS (Frames Per Second) ---    dt = 0
    Clock = pygame.time.Clock()  # Crée un objet Clock pour aider à gérer le temps et le framerate du jeu

    # Gestion des événements (pour pouvoir fermer la fenêtre)
    while True:              
        for event in pygame.event.get():  # Pour chaque événement dans la liste des événements
            if event.type == pygame.QUIT:  # Si ce type d'événement est "fermeture de fenêtre"
                return                  # Alors on sort de la fonction
        dt = (Clock.tick(60) / 1000)    # --- Calcul du Delta Time et régulation du Framerate --- Clock.tick(60) : Limite le jeu à un maximum de 60 images par seconde (FPS). / 1000       : Convertit le temps (en millisecondes) en secondes pour faciliter les calculs de mouvement
   

        # Efface l'écran en le remplissant de noir à chaque nouvelle frame
        screen.fill("black") 

        # Rafraîchir l'écran pour afficher tout ce qui a été dessiné
        pygame.display.flip()

# Point d'entrée du programme
if __name__ == "__main__":      # Cette condition assure que main() est appelée seulement si le script est exécuté directement
    main()

