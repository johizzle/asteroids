import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        # Use the position property or method from CircleShape
        position = (self.position.x, self.position.y)  # Or however it's stored
        pygame.draw.circle(screen, "white", position, self.radius, width=2)

    def update(self, dt):
        # Get the current position, add velocity * dt to it
        self.position += self.velocity * dt  # If position is a vector
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20,50)

        a = self.velocity.rotate(rand_angle)
        b = self.velocity.rotate(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2