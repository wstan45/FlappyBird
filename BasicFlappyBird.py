import pygame
import random

'''
class Apple:

    def __init__(self):
        self.x = 400
        self.y = 200

    def set_pos(self, x, y):
        self.x = x
        self.y = y

'''
class Bird:
    def __init__(self, surface):
        self.y = 300
        self.x = 100
        self.surface = surface
        self.gravity = 2
        self.velocity = 0
        self.lift = 30
    def show(self):
        pygame.draw.ellipse(self.surface, (255,255,255), (self.x, self.y, 25,25))
        
    def update(self):
        
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

        if self.y < 0 :
            self.y = 0
        
        if self.y > 575:
            self.velocity = 0
            self.y = 575
        
    def up(self):
        self.velocity -= self.lift

class Pipe:
    def __init__(self, surface):
        self.top = random.randint(0, 300)
        self.bottom = random.randint(0, 300)
        self.x = 800-20
        self.w = 20
        self.surface = surface
        self.speed = 5

    def show(self):
        pygame.draw.rect(self.surface, (255,255,255), (self.x, 0, self.w, self.top))
        pygame.draw.rect(self.surface, (255,255,255), (self.x, 600-self.bottom,
                                                       self.w, self.bottom))
        
        
    def update(self):
        self.x -= self.speed

    def offscreen(self):
        if self.x < -self.w:
            return True
        return False

    def hits(self, bird):
        if bird.y < self.top or bird.y > (600-self.bottom):
            if bird.x > self.x and bird.x < (self.x + self.w):
                return True
        return False
            
#setup
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
crashed = False

frameCount = 0
#initialise objects
bird = Bird(gameDisplay)
p1 = Pipe(gameDisplay)
pipes = []
pipes.append(p1)
while not crashed:
    
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.up()

    if frameCount == 30:
        frameCount = 0
        newpipe = Pipe(gameDisplay)
        pipes.append(newpipe)
        
    #draw shit
    gameDisplay.fill((0,0,0))
    bird.show()

    for i in range (len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()

        #if pipes[i].hits(bird):
            

        if pipes[i].offscreen():
            pipes.pop(i)

    bird.update()

    frameCount += 1
    pygame.display.update()
    clock.tick(30)

pygame.quit()













