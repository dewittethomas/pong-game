import pygame

class Paddle:
    def __init__(self, window_width, window_height, x, y, width, height, y_vel, color):
        self.window_width = window_width
        self.window_height = window_height
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.y_vel = y_vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
   
    def move_up(self):
        if (self.rect.top > 0):
            self.rect.y -= self.y_vel

    def move_down(self):
        if (self.rect.bottom < self.window_height):
            self.rect.y += self.y_vel

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)