from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame 

def main(): 
    pygame.init() 
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)   
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2 
    player = Player(x, y) 

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updatables.update(dt)
        for sprite in asteroids: 
            if sprite.check_collision(player):
                print("Game over!")
                return 
            
        for sprite in drawables: 
            sprite.draw(screen) 
        pygame.display.flip()

        dt = clock.tick(60) / 1000 

        

if __name__ == "__main__": 
    main() 
