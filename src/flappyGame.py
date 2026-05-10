import time
from pipe import Pipe 
class flappyGame:
    
    def __init__(self, birds):
        
        self.birds = birds
        self.pipeGaps = 300 
        self.pipes = []
        pipe = Pipe()
        self.pipes.append(pipe)
        self.score = 0
        self.nextPipe = pipe 
        self.speed = 5
        self.events = None

        for i in range(4):
            pipe = Pipe(pipe.posX + self.pipeGaps)
            self.pipes.append(pipe)


    
    def update(self):

        for bird in self.birds: 
            if bird.isAlive:
                bird.update()

        for pipe in self.pipes:
            pipe.update(self.speed)
        
        for bird in self.birds:

            if bird.posX + bird.width >= self.nextPipe.posX and bird.posX <= self.nextPipe.posX + self.nextPipe.width :
                bird.isAlive = bird.posY > self.nextPipe.posY and bird.posY + bird.height < self.nextPipe.posY + self.nextPipe.gap

            if bird.posY > 500 :
                bird.isAlive = False

        if self.nextPipe.posX + self.nextPipe.width < self.birds[0].posX : 
            self.score += 1
            index = self.pipes.index(self.nextPipe)
            self.nextPipe= self.pipes[index+1]

        if self.score % 10 == 0:
            self.speed += 1
             
        if(self.pipes[0].isOutofBounds()):
            self.pipes.pop(0)
            lastPipe = self.pipes[len(self.pipes)-1]
            self.pipes.append(Pipe(lastPipe.posX + self.pipeGaps))
        

    def isOver(self):
        for bird in self.birds:
            if bird.isAlive:
                return False 
        return True

    def playBirds(self):
        for bird in self.birds:
            if bird.isAlive:
                bird.decision(self) 


    