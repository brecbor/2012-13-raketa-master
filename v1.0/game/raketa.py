import pyglet
from pyglet.window import key
from .seznami import *
from . import neMeteor, metek
from .screen import *
from . import gameover


class Raketa(neMeteor.NeMeteor):
    def __init__ (self, game, *args,**kwargs):
        super().__init__(game, *args, **kwargs)
        self.key_handler=key.KeyStateHandler()
        self.vx = 200
        self.scale = 0.99
        self.timer = 0
        self.timer_base = 1/2

        self.tip = 'Raketa'

    def update(self, dt):
        self.timer -= dt
        #self.vx *= self.scale
        if(self.key_handler[key.LEFT]):
            self.x -= self.vx*dt
        if(self.key_handler[key.RIGHT]):
            self.x += self.vx*dt
        if(self.x<=-self.width//2):
            self.x=500-self.width//2
        if(self.x>500-self.width//2):
            self.x=-self.width//2
        if(self.key_handler[key.SPACE]):
            if(self.timer <= 0):
                self.strel()
                self.timer = self.timer_base*self.scale
        if(self.key_handler[key.P]):
                gameover.pause = True  

    def collision(self, other):
        super().collision(other)
        
    def strel(self):
        tmp = metek.Metek(self, pyglet.resource.image('bull2.png'), batch = self.game.main_batch)
        tmp.x = self.x + self.width//2-2
        tmp.y = self.height
        self.game.metek_list.append(tmp)

    def zabij(self):
        gameover.game_over = True
        self.game.metek_list = []
        self.game.meteorji_list = []


                        
