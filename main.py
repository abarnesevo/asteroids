import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    play = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        
        for draw_me in drawable:
            draw_me.draw(screen)
        
        for ast in asteroids:
            for shot in shots:
                if ast.collision_check(shot) == True:
                    shot.kill()
                    ast.split()
        
        for ast in asteroids:
            if ast.collision_check(player) == True:
                print("Game over!")
                play = False
        
        pygame.display.flip()

if __name__ == "__main__": 
    main()

