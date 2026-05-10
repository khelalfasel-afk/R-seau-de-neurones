class Controller:

    def __init__(self, game, view):
        self.game = game
        self.view = view

    def runGame(self):
        import pygame

        running = True

        while running:
            events =  pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self.game.events = events
            self.game.playBirds()
            
            # 🔄 logique
            self.game.update()

            # 🎨 affichage
            self.view.draw()
            self.view.tick()

            if self.game.isOver():
                running = False

        pygame.quit()
   