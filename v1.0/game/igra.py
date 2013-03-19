import pyglet
import random
from pyglet.window import key
from .screen import *
from game import menu, raketa, gumb, meteor, gameover
#from v1.0 import main
class Game():

    def start(self):
        self.vy_scale=1.1
        self.dodaj_timerbase = 1
        self.dodaj_timer = self.dodaj_timerbase
        self.dodaj_scale = 0.98
        self.meteorji_list = []
        self.metek_list = []
        self.main_batch = pyglet.graphics.Batch()
        self.menuStart_list = []
        self.menuStart = menu.Menu()
        napis = pyglet.text.Label(text="Ime", font_size=50, x=200, y=350, bold = True, color=(250, 250, 0, 255))
        napis.rotation = 50
        self.menuStart.labels.append(napis)
        tmp = pyglet.resource.image('gumb.png')
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuStart.buttons.append(gumb.Gumb(self, tmp, name = "Start", batch = self.menuStart.buttonsBatch, x = window.width/2, y = window.height/2))
        self.menuStart.buttons.append(gumb.Gumb(self, tmp, name = "Options", batch = self.menuStart.buttonsBatch, x = window.width/2, y = window.height/2 - 80))
        self.menuStart.buttons.append(gumb.Gumb(self, tmp, name = "Exit", batch = self.menuStart.buttonsBatch, x = window.width/2, y = window.height/2 - 160))
        for i in self.menuStart.buttons[:]:
            napis  = pyglet.text.Label(text=i.name, font_size=20, x=i.x, y=i.y, bold = True, color=(0, 0, 255, 255), anchor_x = "center", anchor_y = "center")
            self.menuStart.labels.append(napis)

        self.menuOptions = menu.Menu()
        napis = pyglet.text.Label(text="Options", font_size=50, x=120, y=350, bold = True, color=(250, 250, 0, 255))
        napis.rotation = 50
        self.menuOptions.labels.append(napis)
        tmp = pyglet.resource.image('raketaGumb.png')
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        tmp1 = pyglet.resource.image('gumb.png')
        tmp1.anchor_x = tmp1.width/2
        tmp1.anchor_y = tmp1.height/2
        self.menuOptions.buttons.append(gumb.Gumb(self, tmp, name = "Chose", batch = self.menuOptions.buttonsBatch, x = window.width/2 - tmp.width, y = window.height/2))
        self.menuOptions.buttons.append(gumb.Gumb(self, tmp, name = "Chose", batch = self.menuOptions.buttonsBatch, x = window.width/2 + tmp.width, y = window.height/2))
        self.menuOptions.buttons.append(gumb.Gumb(self, tmp1, name = "Main Menu", batch = self.menuOptions.buttonsBatch, x = window.width/2, y = window.height/2 - 80))
        for i in self.menuOptions.buttons[:]:
            if(i.name!='Chose'):
                napis  = pyglet.text.Label(text=i.name, font_size=20, x=i.x, y=i.y, bold = True, color=(0, 0, 255, 255), anchor_x = "center", anchor_y = "center")
                self.menuOptions.labels.append(napis)


        self.menuPause = menu.Menu()
        napis = pyglet.text.Label(text="Pause", font_size=50, x=150, y=350, bold = True, color=(250, 250, 0, 255))
        napis.rotation = 50
        self.menuPause.labels.append(napis)
        tmp = pyglet.resource.image('gumb.png')
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuPause.buttons.append(gumb.Gumb(self, tmp, name = "Resume", batch = self.menuPause.buttonsBatch, x = window.width/2, y = window.height/2))
        self.menuPause.buttons.append(gumb.Gumb(self, tmp, name = "Restart", batch = self.menuPause.buttonsBatch, x = window.width/2, y = window.height/2 - 80))
        self.menuPause.buttons.append(gumb.Gumb(self, tmp, name = "Main Menu", batch = self.menuPause.buttonsBatch, x = window.width/2, y = window.height/2 - 160))
        for i in self.menuPause.buttons[:]:
            napis  = pyglet.text.Label(text=i.name, font_size=20, x=i.x, y=i.y, bold = True, color=(0, 0, 255, 255), anchor_x = "center", anchor_y = "center")
            self.menuPause.labels.append(napis)

    def myInit(self):
        #pyglet.clock.schedule_once(self.dodaj, 1)
        gameover.start = False
        self.main_batch = pyglet.graphics.Batch()
        #print(self.main_batch)
        self.meteorji_list = []
        self.metek_list = []
        self.menuEnd_list = []       
        self.menuPause_list = []        
        
        self.menuEnd = menu.Menu()
        #menu2 = menu.Menu()
        napis = pyglet.text.Label(text="Game over", font_size=50, x=75, y=350, bold = True, color=(250, 250, 0, 255))
        napis.rotation = 50
        self.menuEnd.labels.append(napis)
        tmp = pyglet.resource.image('gumb.png')
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuEnd.buttons.append(gumb.Gumb(self, tmp, name = "Retry", batch = self.menuEnd.buttonsBatch, x = window.width/2, y = window.height/2))
        self.menuEnd.buttons.append(gumb.Gumb(self, tmp, name = "Main Menu", batch = self.menuEnd.buttonsBatch, x = window.width/2, y = window.height/2 - 80))
        for i in self.menuEnd.buttons[:]:
            napis  = pyglet.text.Label(text=i.name, font_size=20, x=i.x, y=i.y, bold = True, color=(0, 0, 255, 255), anchor_x = "center", anchor_y = "center")
            self.menuEnd.labels.append(napis)

        self.raketa = raketa.Raketa(self, pyglet.resource.image('raketa2.png'), batch=self.main_batch)
        window.push_handlers(self.raketa.key_handler)
        
        gameover.game_over = False
        
    def __init__(self):
        self.start()

    def draw(self):
        if(not gameover.game_over and not gameover.start and not gameover.pause and not gameover.options):
            self.main_batch.draw()
            self.raketa.draw()
        elif(gameover.options):
            self.menuOptions.draw()
            for e in self.menuOptions.labels[:]:
                e.draw()
        elif(gameover.start):
            self.menuStart.draw()
            for e in self.menuStart.labels[:]:
                e.draw()
        elif(gameover.pause):
            self.menuPause.draw()
            for e in self.menuPause.labels[:]:
                e.draw()
        elif(gameover.options):
            self.menuOptions.draw()
            for e in self.menuOptions.labels[:]:
                e.draw()
        else:
            self.menuEnd.draw()
            for e in self.menuEnd.labels[:]:
                e.draw()

    def mouse_press(self, x, y):
        if(gameover.options):
            self.menuOptions.preveriKlike(x, y)
        elif(gameover.start):
            self.menuStart.preveriKlike(x, y)            
        elif(gameover.game_over):
            self.menuEnd.preveriKlike(x, y)
        elif(gameover.pause):
            self.menuPause.preveriKlike(x, y)

    def update(self, dt):        
        if(not gameover.game_over and not gameover.start and not gameover.afterPause and not gameover.pause and not gameover.options):
            self.raketa.update(dt)
            self.dodaj_timer -= dt
            while(self.dodaj_timer <= 0):
                if(self.dodaj_timerbase < 0.01):
                    self.dodaj()
                    self.dodaj_timer += 0.01
                else:
                    self.dodaj()
                    self.dodaj_timerbase = self.dodaj_timerbase * self.dodaj_scale
                    self.dodaj_timer = self.dodaj_timer + self.dodaj_timerbase
            for m in self.meteorji_list[:]:
                m.update(dt)
            for i in self.metek_list[:]:
                i.update(dt)
            for m in self.meteorji_list[:]:
                m.collision(self.raketa)
                for i in self.metek_list[:]:
                    m.collision(i)
        else:
            self.dodaj_timerbase = 1
            self.dodaj_timer = self.dodaj_timerbase    
            if(gameover.pause):
                gameover.timer = gameover.baseTimer
            elif(gameover.afterPause):
                gameover.timer -= dt
                if(gameover.timer<=0):
                    gameover.afterPause = False

    def dodaj(self):
        
        x=random.randint(0,1)
        if(x==1):
            tmp = meteor.Meteor(self, pyglet.resource.image('meteor2.png'), batch = self.main_batch)
        else:
            tmp = meteor.Meteor(self, pyglet.resource.image('meteor1.png'), batch = self.main_batch)
        tmp.x=random.randint(0, window.width-tmp.width)
        tmp.y=window.height
        tmp.vy = random.randint(-150, -50) * self.vy_scale
        self.meteorji_list.append(tmp)
        """
        if(not gameover.game_over and not gameover.start and not gameover.afterPause and not gameover.pause):
            pyglet.clock.schedule_once(self.dodaj, dt/10)
        """
        
            

    
