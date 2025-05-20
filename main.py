# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:
        #this will check if the user has closed the window and exit 
        #the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        
        screen.fill("black")
        updatable.update(dt)
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()