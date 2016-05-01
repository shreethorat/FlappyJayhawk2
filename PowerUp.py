import pygame
from random import randint


class PowerUp(pygame.sprite.Sprite):
    
    POWERUP_DURATION = 5#5seconds
    
    def __init__(self, color, pos, radius, width, image, effectname):
        #--------------when the PowerUp is floating in the air
        #circular aura
        self.color = color
        self.x = pos[0]#x coord for center
        self.y = pos[1]#y coord for center
        self.x = 600
        self.y = randint(0 + radius, 500 - radius)
        self.radius = radius
        self.width = width

        #power up image
        self.scale = ((int)(self.radius * 1.4), (int)(self.radius * 1.4))
        self.PowerUp_image = image
        self.PowerUp_image = self.PowerUp_image.convert_alpha()
        self.PowerUp_image = pygame.transform.scale(self.PowerUp_image, self.scale)
        self.image_x = self.x - self.scale[0] / 2
        self.image_y = self.y - self.scale[1] / 2

        #--------------when the PowerUp has been picked up
        #power up effect name to refer to
        self.effectname = effectname

        #power up duration bar length: represented as a 200px bar that, over POWERUP_DURATION, will reduce to 0px
        self.PowerUp_duration_bar_length = 200
        self.duration_remaining = 300#5 seconds * 60 FPS = 300 frame duration

    def scroll(self):
        self.x -= 1
        self.image_x -= 1
        
        if(self.x <= -600):
            return False
        return True

    @property
    def circle_color(self):
        return self.color
    @property
    def circle_pos(self):
        return (self.x, self.y)
    @property
    def circle_radius(self):
        return self.radius
    @property
    def circle_width(self):
        return self.width

    @property
    def image(self):
        return self.PowerUp_image
    @property
    def image_rect(self):
        return pygame.Rect(self.image_x, self.image_y, 25, 25)

    def update_duration(self):       
        self.duration_remaining -= 1
        if(self.duration_remaining % 3 == 0 or self.duration_remaining % 3 == 1):
            self.PowerUp_duration_bar_length -= 1

    @property
    def duration_bar_length(self):
        return self.PowerUp_duration_bar_length
    @property
    def duration_expired(self):
        return (self.duration_remaining <= 0)

    
    def effect( self ):
        """Some description that tells you it's abstract,
        often listing the methods you're expected to supply."""
        raise NotImplementedError( "Should have implemented this" )
