import pygame,os
import settings
from PowerUp import *
class bullet_time(PowerUp):
    SCREEN = pygame.display.set_mode((600,500))
    def __init__(self):
        super(bullet_time, self).__init__((0,255,0), (0,0), 20, 0,
                                               pygame.image.load(os.path.join('.', 'images', 'jayhawk.png')),
                                               'bullet_time')

    def effect(self):
        """Press and hold up to slow down time"""
        #print 'MATRIX EXISTS'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            settings.FPS -= 1
            if(settings.FPS < 15):
                settings.FPS = 15
        else:
            settings.FPS += 3
            if(settings.FPS > 60):
                settings.FPS = 60

    def effect_expire(self):
        pass
