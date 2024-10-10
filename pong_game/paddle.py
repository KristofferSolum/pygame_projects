import pygame


class Paddle:
    def __init__(self, x, y, width, height, color, speed, player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.player = player

    def move(self):
        if self.player == 1:
            if pygame.key.get_pressed()[pygame.K_DOWN] and self.y + self.height < 900:
                self.y += self.speed
            if pygame.key.get_pressed()[pygame.K_UP] and self.y > 0:
                self.y -= self.speed
        elif self.player == 2:
            if pygame.key.get_pressed()[pygame.K_s] and self.y + self.height < 900:
                self.y += self.speed
            if pygame.key.get_pressed()[pygame.K_w] and self.y > 0:
                self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, ball):
        ball.check_collision_with_paddle(self)

