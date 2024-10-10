import pygame


class Timer:
    def __init__(self, screen, game_time, start_time):
        self.screen = screen
        self.font = pygame.font.Font(None, 140)
        self.game_time = game_time
        self.start_time = start_time
        self.seconds_passed = (pygame.time.get_ticks() - self.start_time) // 1000
        self.time_left = self.game_time - self.seconds_passed

    def update(self):
        self.seconds_passed = (pygame.time.get_ticks() - self.start_time) // 1000
        self.time_left = self.game_time - self.seconds_passed
        if self.time_left <= 0:
            return True
        return False


    def draw(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_text = self.font.render(f"{minutes:02}:{seconds:02}", True, (255, 255, 255))
        self.screen.blit(time_text, (self.screen.get_width() // 2 - time_text.get_width() // 2, 50))

