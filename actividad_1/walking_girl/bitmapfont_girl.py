import pygame
import os

from walking_girl.config import cfg_item

class BitmapFont_Girl:

    def __init__(self):
        self.__image = pygame.image.load(os.path.join(*cfg_item("girl", "path"))).convert_alpha()

        self.sprites = dict()

        columns = cfg_item("girl", "columns")
        sprite_size = cfg_item("girl", "sprite_size")

        for i in range(cfg_item("girl", "total_sprites")):
            left = sprite_size[0] * ((i % columns))
            top = sprite_size[1] * int((i / columns))
            self.sprites[i] = pygame.Rect(left, top, sprite_size[0], sprite_size[1])

    def render(self, surface_dst, pos, sprite):
        surface_dst.blit(self.__image, pos, self.sprites[sprite])
        pygame.display.update()

