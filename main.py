import pygame
from constants import * 

def main():
    pygame.init() 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # to get a new GUI window
    # Gestion des événements (pour pouvoir fermer la fenêtre)
    while True:
        for event in pygame.event.get():  # Pour chaque événement dans la liste des événements
            if event.type == pygame.QUIT:  # Si ce type d'événement est "fermeture de fenêtre"
                return                     # Alors on sort de la fonction
    
        screen.fill("black") 

        # Rafraîchir l'écran
        pygame.display.flip()

  


if __name__ == "__main__":
    main()

