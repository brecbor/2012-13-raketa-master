import pyglet
#import random
#from pyglet.window import key
#from game import object, physObj, meteor, neMeteor, raketa, metek, menu, gumb
from game.seznami import *
from game.screen import *
#from game import gameover
from game.igra import *


#krneki=menu.MenuEnd()

#options_menu = menu.Menu()

@window.event
def on_draw():
    window.clear()
    play.draw()
    #menu1.draw()
    #print(gameover.game_over)
    

@window.event
def on_mouse_press(x, y, button, modifiers):
    play.mouse_press(x, y)
    

def update(dt):
    play.update(dt)
             
def dodaj(dt):
    play.dodaj()


if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    #dodaj(0)
    #pyglet.clock.schedule_once(dodaj, 1)
    #play = Game()
    pyglet.app.run()
    

