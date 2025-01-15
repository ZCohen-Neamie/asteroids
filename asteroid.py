from circleshape import CircleShape
from constants import *
import pygame 
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        fast_rotated_vector1 = self.velocity.rotate(random_angle) * 1.2 
        fast_rotated_vector2 = self.velocity.rotate(-1 * random_angle) * 1.2 
        new_radius = self.radius - ASTEROID_MIN_RADIUS 
        asteroid_1 = Asteroid(*self.position, new_radius)
        asteroid_1.velocity = fast_rotated_vector1 
        asteroid_2 = Asteroid(*self.position, new_radius)
        asteroid_2.velocity = fast_rotated_vector2

