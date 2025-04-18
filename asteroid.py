import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20,50)
        split1 = pygame.Vector2(self.velocity).rotate(angle)
        split2 = pygame.Vector2(self.velocity).rotate(-angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = split1
        asteroid2.velocity = split2
        #asteroid1.velocity = velocity1
        #asteroid2.velocity = velocity2
    
    def update(self, dt):
        self.position += self.velocity * dt