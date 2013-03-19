import pyglet
from .import physObj

class Meteor(physObj.PhysObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tip = "Meteor"

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        super().collision(other)

    def zabij(self):
        super().zabij()
        
    
