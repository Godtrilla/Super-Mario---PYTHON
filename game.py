import time as time
from time import sleep

import pygame
import itertools
from pygame.locals import *

class Goomba:
    def __init__(self, x, y):
        self.model = Model
        self.x = x
        self.width = 37
        self.height = 45
        self.speed = 5
        self.direction = 1
        self.y = y
        self.vert_vel = 12
        self.frames = 0
        self.type = "goomba"
        self.goombaImage = pygame.image.load("goomba.png")
        self.px = self.x
        self.py = self.y

    def getOutofTube(self, t):
        marioRight = self.x + self.width
        marioLeft = self.x
        tubeRight = t.x + t.width
        tubeLeft = t.x
        if marioRight >= tubeLeft and self.px + self.width <= tubeLeft:
            self.x = t.x - self.width
            self.direction = -1
        if marioLeft <= tubeRight and self.px >= tubeRight:
            self.x = tubeRight
            self.direction = 1


    def update(self):
        self.coordinateSave()
        self.y = 345
        self.x += self.speed * self.direction

    def coordinateSave(self):
        self.px = self.x
        self.py = self.y





class Firball:
    def __init__(self, x, y):
        self.model = Model()
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = 3
        self.height = 47
        self.width = 47
        self.type = "fireball"
        self.fireImage = pygame.image.load("fireball.png")

    def coordinateSave(self):
        self.px = self.x
        self.py = self.y

    def update(self):
        self.coordinateSave()
        if self.model.mario.flip == True:
            self.direction = -3
        self.x += self.speed * self.direction
        self.y += self.speed * 2




class Tube:
    def __init__(self, x, y):
        self.model = Model
        self.x = x
        self.y = y
        self.height = 400
        self.width = 55
        self.type = "tube"
        self.tubeImage = pygame.image.load("tube.png")

    def update(self):
        return 0

class Mario:
    def __init__(self, x, y):
        self.view = View
        self.x = x
        self.y = y
        self.width = 60
        self.height = 95
        self.marioImageNum = 0
        self.vert_vel = 12
        self.frames = 0
        self.marioOffset = self.x
        self.flip = False
        self.type = "mario"
        self.fromes = 0
        self.mario_images = []
        self.mario_images.append(pygame.image.load("mario1.png"))
        self.mario_images.append(pygame.image.load("mario2.png"))
        self.mario_images.append(pygame.image.load("mario3.png"))
        self.mario_images.append(pygame.image.load("mario4.png"))
        self.mario_images.append(pygame.image.load("mario5.png"))

    def getOutofTube(self,t):
        marioRight = self.x + self.width
        marioLeft = self.x
        tubeRight = t.x + t.width
        tubeLeft = t.x
        marioToes = self.y + self.height
        tubeTop = t.y
        if marioRight >= tubeLeft and self.px + self.width <= tubeLeft:
            self.x = t.x - self.width
        if marioLeft <= tubeRight and self.px >= tubeRight:
                self.x = tubeRight
        if marioToes >= tubeTop and self.py + self.height <= tubeTop:
                    self.y = t.y - self.height
                    self.vert_vel = 0
                    self.frames = 0


    def update(self):
        self.vert_vel += 6
        self.y += self.vert_vel
        self.marioImageNum += 1
        self.frames += 1
        if self.marioImageNum > 4:
            self.marioImageNum = 0
        if self.y > 390 - self.height:
            self.vert_vel = 0
            self.y = 390 - self.height
            self.frames = 0
        if self.y < 0:
            self.y = 0

    def jump(self):
        self.vert_vel = -20

    def coordinateSave(self):
        self.px = self.x
        self.py = self.y

 #   def draw(self):
  #      self.view.screen.blit(self.mario_images[self.marioImageNum],(self.x, self.y))


class Model():
    def __init__(self):
        self.mario = Mario(0, 380)
        self.tube = Tube(300,200)
        self.tube2 = Tube(600,200)
        self.goomba = Goomba(350,450)
        self.goomba2 = Goomba(400,500)
      #  self.fireball = Firball(0,300)

        self.sprites = []
        self.sprites.append(self.mario)
        self.sprites.append(self.tube)
        self.sprites.append(self.tube2)
        self.sprites.append(self.goomba)
        self.sprites.append(self.goomba2)

    def update(self):

        for sprite in self.sprites:
            sprite.update()
            if sprite.type == "tube":
                temp = sprite
                if self.collision(self.mario, temp):
                    self.mario.getOutofTube(temp)
                    print("Collision")
                if self.collision(self.goomba,temp):
                    print("Collision")
                    self.goomba.getOutofTube(temp)
                if self.collision(self.goomba2,temp):
                    print("Collision 2")
                    self.goomba2.getOutofTube(temp)
            if sprite.type == "fireball":
                f = sprite
                if self.collision(f, self.goomba2):
                    print("Collision 22222222")
                    self.goomba2.goombaImage = \
                        pygame.image.load("goomba_fire.png")
                    self.goomba2.x = -5550
                    self.goomba2.height = -5550
                if self.collision(f, self.goomba):
                    self.goomba.goombaImage = \
                        pygame.image.load("goomba_fire.png")
                    self.goomba.x = -5550
                    self.goomba.height = -5550


    def collision(self, a, b):
        marioRight = a.x + a.width
        marioLeft = a.x
        tubeRight = b.x + b.width
        tubeLeft = b.x
        marioHead = a.y
        marioToes = a.y + a.height
        tubeTop = b.y
        tubeBottom = b.y + b.height
        if marioRight < tubeLeft:
            return False
        if marioLeft > tubeRight:
            return False
        if marioToes < tubeTop:
            return False
        if marioHead > tubeBottom:
            return False
        return True

    def Fireball(self, x, y):
        f = Firball(x, y)
        self.sprites.append(f)




class View():
    def __init__(self, model):
        screen_size = (800, 600)
        self.screen = pygame.display.set_mode(screen_size, 32)
        self.model = model
        self.mario_ground = pygame.image.load("mario_ground.png")

    # self.model.rect = self.turtle_image.get_rect()

    def update(self):
        self.screen.fill([0, 200, 100])
        #    self.screen.blit(self.turtle_image, self.model.rect)
       # if self.model.mario.flip == True:
        #    self.screen.blit(pygame.transform.flip(self.model.mario.mario_images[self.model.mario.marioImageNum],
         #                   self.model.mario.x, self.model.mario.y),)
   #     if self.model.mario.flip == False:
        self.screen.blit(self.model.mario.mario_images[self.model.mario.marioImageNum],
                             (self.model.mario.x, self.model.mario.y,
                              self.model.mario.width, self.model.mario.height))
       # self.screen.blit(self.mario_ground, (0, 403))

        for sprite in self.model.sprites:
            if sprite.type == "tube":
                self.screen.blit(sprite.tubeImage,
                                 (sprite.x, sprite.y))
            if sprite.type == "goomba":
                self.screen.blit(sprite.goombaImage,
                                 (sprite.x, sprite.y))
            if sprite.type == "fireball":
                self.screen.blit(sprite.fireImage,
                                 (sprite.x, sprite.y))

        brick_width, brick_height = self.mario_ground.get_width(), \
                                    self.mario_ground.get_height()
        for x, y in itertools.product(range(0, 610 + 1, brick_width),
                                      range(390, 650 + 1, brick_height)):
            self.screen.blit(self.mario_ground, (x, y))




        pygame.display.flip()


class Controller():
    def __init__(self, model):
        self.model = model
        self.keep_going = True

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keep_going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keep_going = False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.model.set_dest(pygame.mouse.get_pos())
        keys = pygame.key.get_pressed()
        self.model.mario.coordinateSave()

        if keys[K_LEFT]:
            self.model.mario.flip = True
            self.model.mario.x -= 8
        if keys[K_RIGHT]:
            self.model.mario.x += 8
        if keys[K_UP]:
            self.model.mario.jump()
        if keys[K_DOWN]:
            self.model.Fireball(self.model.mario.x,self.model.mario.y)


print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
    c.update()
    m.update()
    v.update()
    sleep(0.04)
print("Goodbye")
