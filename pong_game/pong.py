import pygame
from ball import Ball
from paddle import Paddle
from timer import Timer


class player:
    def __init__(self):
        self.score = 0
        self.paddle = None


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.font1 = pygame.font.Font(None, 74)
        self.font2 = pygame.font.Font(None, 52)
        self.ball = Ball(400, 300, 20, (255, 255, 255), 5)
        self.player1 = player()
        self.player2 = player()
        self.player1.paddle = Paddle(1140, 400, 40, 100, (255, 255, 255), 5, 1)
        self.player2.paddle = Paddle(20, 400, 40, 100, (255, 255, 255), 5, 2)
        self.timer = Timer(self.screen, 30, pygame.time.get_ticks())
        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill((0, 0, 0))

            collision = self.ball.check_collision(self.screen)
            if collision == "left":
                self.player1.paddle.y = 400
                self.player2.paddle.y = 400
                self.player2.score += 1
                self.screen.blit(self.font1.render("Player 2 scores!", True, (255, 255, 255)), (400, 200))
                pygame.display.flip()
                pygame.time.wait(2000)
                self.timer.start_time += 2000
            elif collision == "right":
                self.player1.paddle.y = 400
                self.player2.paddle.y = 400
                self.player1.score += 1
                self.screen.blit(self.font1.render("Player 1 scores!", True, (255, 255, 255)), (400, 200))
                pygame.display.flip()
                pygame.time.wait(2000)
                self.timer.start_time += 2000
            self.player1.paddle.check_collision(self.ball)
            self.player2.paddle.check_collision(self.ball)
            self.ball.move()
            self.ball.draw(self.screen)

            self.player1.paddle.move()
            self.player1.paddle.draw(self.screen)
            self.player2.paddle.move()
            self.player2.paddle.draw(self.screen)

            score1 = self.font2.render("Player 1:  "+str(self.player1.score), True, (255, 255, 255))
            score2 = self.font2.render("Player 2:  "+str(self.player2.score), True, (255, 255, 255))
            self.screen.blit(score1, (40, 50))
            self.screen.blit(score2, (1160 - score2.get_width(), 50))

            if self.timer.time_left <= self.timer.game_time // 2:
                self.ball.speed = 7
            elif self.timer.time_left <= self.timer.game_time // 4:
                self.ball.speed = 8
            elif self.timer.time_left <= self.timer.game_time * 0.75:
                self.ball.speed = 6

            if self.timer.time_left <= 10:
                pygame.draw.rect(self.screen, (255, 0, 0), (self.screen.get_width() // 2 - (325/2), 40, 325, 110))

            self.timer.draw()
            self.game_over = self.timer.update()

            pygame.display.flip()
            self.clock.tick(60)



