import pygame
from pygame.locals import *
# from pygame.sprite import _Group
from config import *
from sprite_sheet import * 
from player import *
from sprite_sheet import SpriteSheet

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rectangulo:pygame.Rect) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rectangulo[2], rectangulo[3]))
        self.rect = self.image.get_rect(topleft = (rectangulo[0], rectangulo[1]))
        self.image.fill((0, 0, 0))