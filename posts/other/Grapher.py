import pygame
from math import sin, cos, tan


class Grapher:
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display. set_caption("GRAPH")
    def __init__(self, background, width, height):
        self.background = background
        self.width = width
        self.height = height
        self.window = pygame.display. set_mode((self.width, self.height))
        self.window.fill(self.background)
        self.run = True
    def plot(self, x, y):
        originx, originy = self.width // 2, self.height // 2
        data = zip(x, y)
        for i, j in data:
            pygame.draw.circle(self.window, (0, 0, 0), (originx+i*30, originy+j*30), 3)
    def run_(self, x, y):
        self.clock.tick(60)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.plot(x, y)
            pygame.display.update()
        pygame.quit()
def power(x):
    return x ** 2
Grapher((255, 255, 255), 500, 500).run_([i*0.01 for i in range(-10000, 10000)], [power(i*0.01)*-1 for i in range(-10000, 10000)])