import pygame
from circleshape import *


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