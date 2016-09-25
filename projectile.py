# Projectile File
import pygame as PG
from os import path

Vector = PG.math.Vector2

class Projectiles(PG.sprite.Sprite):

    def __init__(self, direction, x, y, Group):
        img_dir = path.join(path.dirname(__file__), 'img')
        PG.sprite.Sprite.__init__(self)
        self.image = PG.image.load(path.join(img_dir, "Egg.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x+20, y+30)
        self.Position = Vector(x+20, y+30)
        self.Speed = 10
        self.displaySelf = True
        if direction == "Up":
            self.Velocity = Vector(0, -self.Speed)
        elif direction == "Down":
            self.Velocity = Vector(0, self.Speed)
        elif direction == "Left":
            self.Velocity = Vector(-self.Speed, 0)
        elif direction == "Right":
            self.Velocity = Vector(self.Speed, 0)
        Group.add(self)

    def update(self):
        self.Position += self.Velocity
        self.rect.center = self.Position
        if self.Position.x < 0 or self.Position.x > 1200 or self.Position.y < 0 or self.Position.y > 700:
            self.kill()

       
