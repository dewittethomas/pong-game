import pygame, random

class Ball:
    def __init__(self, window_width, window_height, x, y, radius, color):
        self.window_width = window_width
        self.window_height = window_height
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = random.choice([-5, 5])
        self.y_vel = random.choice([-4, 4])
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        self.color = color

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        # Check for collision with top and bottom walls
        if ((self.y - self.radius <= 0) or (self.y + self.radius >= self.window_height)):
            self.y_vel *= -1

    def reset(self):
        self.x = self.window_width // 2
        self.y = self.window_height // 2
        self.x_vel = random.choice([-4, 4])
        self.y_vel = random.choice([-4, 4])

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
