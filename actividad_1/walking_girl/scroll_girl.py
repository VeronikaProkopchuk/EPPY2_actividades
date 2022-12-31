import pygame

from walking_girl.config import cfg_item
from walking_girl.bitmapfont_girl import BitmapFont_Girl

class Scroll_Girl:

    def __init__(self, y_init):
        self.__pos = pygame.math.Vector2(cfg_item("screen_size")[0], y_init)
        self.__bitmapfont = BitmapFont_Girl()
        self.__clock = pygame.time.Clock()

    def update(self, delta_time):
        self.__pos.x -= cfg_item("scroll", "speed") * delta_time
        if self.__pos.x <= -cfg_item("girl", "sprite_size")[0]:
            self.__pos.x = 0
            

    def render(self, surface_dst):
        for i in range(len(self.__bitmapfont.sprites)):
            pygame.display.update()
            self.__clock.tick(10)
            pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
            self.__bitmapfont.render(surface_dst, pos, i)


