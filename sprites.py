from settings import *
import random as rand
import pygame as pg
import os
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(os.path.dirname(
            os.path.abspath(__file__)) + '\\Flappy-Img', 'fish r1.png'))
        self.image = pg.transform.scale(self.image, (50, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.mask = pg.mask.from_surface(self.image)

    def update(self) -> None:
        self.acc = vec(0, 0)
        if self.vel.y < 10:
            self.acc.y += GRAVITY

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.vel.y >= -10:
            self.acc.y -= PLAYER_ACC

        # Equations of motion
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # End game if player hits ground
        if self.pos.y - 10 == 0:
            self.show_go_screen()

        self.rect.midbottom = self.pos


class Pipe(pg.sprite.Sprite):
    def __init__(self, x: float = 50, y: float = 0, w: float = 50, h: float = 50) -> None:
        pg.sprite.Sprite.__init__(self)
        #self.image = pg.Surface((50,HEIGHT/2))
        self.image = pg.image.load(os.path.join(os.path.dirname(
            os.path.abspath(__file__)) + '\\Flappy-Img', 'pipe.png')).convert_alpha()
        ratio = round(rand.uniform(1.5, 6),1)
        self.image = pg.transform.scale(self.image, (65, HEIGHT))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH+50, HEIGHT/ratio)
                                #round(rand.uniform(1.5, 6),1)
        self.vel = vec(2.6, 0)
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.pos -= self.vel
        self.rect.center = self.pos
