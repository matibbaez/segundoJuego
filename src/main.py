import pygame
from pygame.locals import *
from config import *
from player import Player

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego con clases")
        pygame.display.set_icon(pygame.image.load("./src/assets/images/doux.png"))
        
        # Agrego un grupo de sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = Player([self.all_sprites])
    
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    
            self.draw()
            self.update()
            
        self.close()

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        
    def update(self):
        self.all_sprites.update()
        pygame.display.flip()

    def close(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()


