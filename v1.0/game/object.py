import pyglet
from .igra import *
from .screen import *

class Object(pyglet.sprite.Sprite):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
        self.tip = "Object"
        self.game = game

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if(window.height <= self.y):
            self.brisanje()
        if(self.y+self.height <= 0):
            self.brisanje()
        
        
    def brisanje(self):
       # print("brisem se!!!!")
        if(self.tip=='Meteor'):
            #print(meteorji_list)
            try:
                self.game.meteorji_list.remove(self)
            except ValueError:
                pass
                
        if(self.tip=='Metek'):
            try:
                self.game.metek_list.remove(self)
            except ValueError:
                pass
            
