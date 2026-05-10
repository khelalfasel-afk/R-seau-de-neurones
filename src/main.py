from bird import Bird
from flappyGame import flappyGame
from flappyView import FlappyView
from controller import Controller
from brain import InputBrain
from brain import RandomBrain
from brain import NeuronBrain
from neuralNetwork import NeuralNetwork

def main():
    
    # 🐦 créer les birds (tu peux en mettre plusieurs)
    birds = [Bird(InputBrain())]
    for i in range(10):
        bird = Bird()
        nn = NeuralNetwork(3,[3],1)
        brain = NeuronBrain(nn, bird)
        bird.brain = brain
        birds.append(bird)
        

    # 🎮 créer le jeu
    game = flappyGame(birds)

    # 🖥️ créer la vue
    view = FlappyView(game)

    # 🎯 créer le controller
    controller = Controller(game, view)

    # ▶️ lancer le jeu
    controller.runGame()

    
if __name__ == "__main__":
    main()