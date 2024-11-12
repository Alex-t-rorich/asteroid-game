import pygame

from constants import *

def main():
    pygame.init()

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    # print(f"ASTEROID_MIN_RADIUS: {ASTEROID_MIN_RADIUS}")
    # print(f"ASTEROID_KINDS: {ASTEROID_KINDS}")
    # print(f"ASTEROID_SPAWN_RATE: {ASTEROID_SPAWN_RATE}")
    # print(f"ASTEROID_MAX_RADIUS: {ASTEROID_MAX_RADIUS}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))
        
        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
