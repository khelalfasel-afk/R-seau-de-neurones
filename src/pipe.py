import time
import random
class Pipe:
    
    def __init__(self, posX = 300):
        self.posX = posX
        self.posY = random.randint(10, 300)
        self.gap = 150
        self.width = 100
        self.time = time.time()
    
    def update(self,speed):
        current_time = time.time()
        dt = current_time - self.time
        self.posX -= speed * dt
        self.time = current_time

    def isOutofBounds(self):
        return self.posX + self.width < 0