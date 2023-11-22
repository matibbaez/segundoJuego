import pygame
from config import *

def get_animations():
    sheet = pygame.image.load("./src/assets/images/Boy.png").convert_alpha()
    sheet = pygame.transform.scale(sheet, (200, 250))
    rows = 5
    cols = 4
    cont_cols = 0
    animation_list = []
    for row in range(rows):
        animation_row = []
        for _ in range(cols):
            animation_row.append(sheet.subsurface(
                (cont_cols * WIDHT_PLAYER, row * HEIGHT_PLAYER, WIDHT_PLAYER, HEIGHT_PLAYER)))
            cont_cols += 1
        cont_cols = 0
        animation_list.append(animation_row)
    return animation_list