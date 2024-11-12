import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up clock for FPS control and initialize delta time
    clock = pygame.time.Clock()
    dt = 0

    # Create groups for updatable, drawable objects, asteroids, and shots
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # NEW group for shots

    # Assign containers for the classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)  # NEW: Add shots to drawable and updatable

    # Instantiate the Player object at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Instantiate the AsteroidField for spawning asteroids
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Collision detection between player and asteroids
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                pygame.quit()
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    print("Collision detected between shot and asteroid!")
                    asteroid.split()
                    shot.kill()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
