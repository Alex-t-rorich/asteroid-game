import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

  def draw(self, screen):
      pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

  def update(self, dt):
      self.position += self.velocity * dt

  def split(self):
      # Remove this asteroid
      self.kill()

      # Check if the asteroid is larger than the minimum size
      if self.radius <= ASTEROID_MIN_RADIUS:
          return  # No further splitting if the asteroid is at the minimum size

      # Generate a random angle between 20 and 50 degrees
      random_angle = random.uniform(20, 50)

      # Create two new velocity vectors by rotating the current velocity
      velocity1 = self.velocity.rotate(random_angle) * 1.2
      velocity2 = self.velocity.rotate(-random_angle) * 1.2

      # Compute the new radius for the smaller asteroids
      new_radius = self.radius - ASTEROID_MIN_RADIUS

      # Create two new smaller asteroids at the same position
      asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

      # Set the velocities of the new asteroids
      asteroid1.velocity = velocity1
      asteroid2.velocity = velocity2

