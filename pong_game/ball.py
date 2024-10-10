import pygame
import random


class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.direction = pygame.math.Vector2(random.uniform(-3, 3), random.uniform(-3, 3)).normalize()

    def move(self):

        self.x += self.speed * self.direction.x
        self.y += self.speed * self.direction.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, screen):
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.direction.y *= -1

        if self.x + self.radius >= screen.get_width():
            self.x = screen.get_width() // 2
            self.y = screen.get_height() // 2
            self.direction = pygame.math.Vector2(random.uniform(1.5, 4) * random.choice([-1, 1]),
                                                 random.uniform(1.5, 4)*random.choice([-1, 1])).normalize()
            return "right"
        elif self.x - self.radius <= 0:
            self.x = screen.get_width() // 2
            self.y = screen.get_height() // 2
            self.direction = pygame.math.Vector2(random.uniform(1.5, 4) * random.choice([-1, 1]),
                                                 random.uniform(1.5, 4)*random.choice([-1, 1])).normalize()
            return "left"
        return None

    def check_collision_with_paddle(self, paddle):
        if self.x - self.radius <= paddle.x + paddle.width and self.x + self.radius >= paddle.x:
            if paddle.y <= self.y <= paddle.y + paddle.height:
                self.direction.x *= -1
                return True
        return False
