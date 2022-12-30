import pygame

from walking_girl.config import cfg_item
from walking_girl.bitmapfont_girl import BitmapFont_Girl

class Scroll_Girl:

    def __init__(self, y_init):
        self.__pos = pygame.math.Vector2(cfg_item("screen_size")[0], y_init)
        self.__bitmapfont = BitmapFont_Girl()
        self.__sprite_in_screen = int(cfg_item("screen_size")[0] / cfg_item("girl", "sprite_size")[0])+1

    def update(self, delta_time):
        self.__pos.x -= cfg_item("scroll", "speed") * delta_time
        if self.__pos.x <= -cfg_item("girl", "sprite_size")[0]:
            self.__pos.x = 0

    def render(self, surface_dst):
        for i in range(self.__sprite_in_screen):
            pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0] * i), self.__pos.y)
            self.__bitmapfont.render(surface_dst, pos, i)
            