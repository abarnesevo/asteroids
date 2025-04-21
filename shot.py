from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_radius = SHOT_RADIUS

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, "white", self.position, self.shot_radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt  
