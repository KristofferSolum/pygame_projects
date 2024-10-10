import pygame


class StartGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))
        self.font = pygame.font.Font(None, 74)
        self.font2 = pygame.font.Font(None, 148)
        self.font3 = pygame.font.Font(None, 48)

    def draw_button(self, x, y, width, height, color, text, text_color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        text = self.font.render(text, True, text_color)
        self.screen.blit(text, (x + width // 2 - text.get_width() // 2, y + height // 2 - text.get_height() // 2))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            self.screen.fill((0, 0, 0))

            text_1 = self.font2.render("Pong", True, (255, 255, 255))
            self.screen.blit(text_1, (600 - (text_1.get_width() / 2), 200))

            text_2 = self.font.render("Two player game", True, (255, 255, 255))
            self.screen.blit(text_2, (600 - (text_2.get_width() / 2), 340))

            text_3 = self.font3.render("Player 1: W (up), S (down)", True, (255, 255, 255))
            self.screen.blit(text_3, (600 - (text_3.get_width() / 2), 430))

            text_4 = self.font3.render("Player 2: Arrow up, Arrow down", True, (255, 255, 255))
            self.screen.blit(text_4, (600 - (text_4.get_width() / 2), 490))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 425 < mouse[0] < 775 and 600 < mouse[1] < 700:
                self.draw_button(425, 600, 350, 100, (0, 255, 0), "Start Game", (0, 0, 0))
                if click[0] == 1:
                    return True
            else:
                self.draw_button(425, 600, 350, 100, (0, 200, 0), "Start Game", (0, 0, 0))

            pygame.display.flip()



