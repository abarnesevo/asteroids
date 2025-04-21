from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, "white", self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(rand_angle)
        new_vector2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        split_ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        split_ast1.velocity = new_vector1 * 1.2
        split_ast2.velocity = new_vector2 * 1.2



