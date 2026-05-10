import pygame
class RandomBrain:
    def decision(self,game):
        import random
        val = random.randint(0,100)
        if val < 3:
            return True
        return False

class InputBrain:
    def decision(self,game):
        for event in game.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return False

class NeuronBrain:
    def __init__(self,nn,bird):
        self.nn = nn
        self.bird = bird

    def decision(self,game):  
        differenceY = game.nextPipe.posY - self.bird.posY
        inputs = [ differenceY, game.nextPipe.posX, game.speed ]  
        outputs = self.nn.forward(inputs)
        
        if outputs[0] > 0.5:
            return True
        return False

