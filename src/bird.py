import time
import random
class Bird:
    
    def __init__(self, brain=None):
        self.gravity = 400
        self.posX = 50
        self.posY = 50
        self.width = 20
        self.height = 20
        self.dv = 0
        self.jumpForce = 200
        self.time  = time.time()
        self.isAlive = True
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.brain = brain

    def update(self):
        current_time = time.time()
        dt = current_time - self.time
        self.dv += self.gravity * dt
        self.posY += self.dv * dt
        self.time = current_time

    def jump(self):
        self.dv = -self.jumpForce
    
    def decision(self,game):
        if self.brain.decision(game):
            self.jump()
    
    