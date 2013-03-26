import pyglet
from .screen import *
from .gameover import *
from .seznami import *
from . import gumb

class Menu():
    def __init__(self):
        #gameover.game_over=True
        #gumb=gumb.Gumb
        self.buttons = []
        self.buttonsBatch = pyglet.graphics.Batch()
        self.labels = []

    def draw(self):
        self.buttonsBatch.draw()

    def preveriKlike(self, x, y):
        #print("preverjam")
        for i in self.buttons:
            i.klik(x, y)

    def addButton(self):
        pass

        
        


    
    


