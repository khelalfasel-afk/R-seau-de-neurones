import pygame

class FlappyView:

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

    def draw(self):
        # Fond
        self.screen.fill((135, 206, 235))  # bleu ciel

        # Dessiner les pipes
        for pipe in self.game.pipes:
            pygame.draw.rect(self.screen, (0, 255, 0),
                (pipe.posX, 0, pipe.width, pipe.posY))

            pygame.draw.rect(self.screen, (0, 255, 0),
                (pipe.posX,
                 pipe.posY + pipe.gap,
                 pipe.width,
                 self.height))

        # Dessiner les birds
        for bird in self.game.birds:
            if bird.isAlive:
                pygame.draw.rect(self.screen, bird.color,
                    (bird.posX, bird.posY, bird.width, bird.height))

        # Update écran
        pygame.display.flip()

    def tick(self):
        self.clock.tick(60)  # 60 FPS