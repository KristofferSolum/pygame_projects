import pygame


class GameOver:
    def __init__(self, player1, player2):
        self.screen = pygame.display.set_mode((1200, 900))
        self.font1 = pygame.font.Font(None, 148)
        self.font2 = pygame.font.Font(None, 74)
        self.player1 = player1
        self.player2 = player2

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill((0, 0, 0))

            text_1 = self.font1.render("Game Over", True, (255, 255, 255))
            self.screen.blit(text_1, (600 - (text_1.get_width()/2), 200))

            if self.player1.score > self.player2.score:
                text_2 = self.font2.render("Player 1 wins!", True, (255, 255, 255))
            elif self.player2.score > self.player1.score:
                text_2 = self.font2.render("Player 2 wins!", True, (255, 255, 255))
            else:
                text_2 = self.font2.render("It's a tie!", True, (255, 255, 255))

            self.screen.blit(text_2, (600 - (text_2.get_width()/2), 400))

            score1 = self.font2.render("Player 1:  " + str(self.player1.score), True, (255, 255, 255))
            score2 = self.font2.render("Player 2:  " + str(self.player2.score), True, (255, 255, 255))
            self.screen.blit(score1, (40, 50))
            self.screen.blit(score2, (1160 - score2.get_width(), 50))

            pygame.display.flip()