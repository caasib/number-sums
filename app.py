import pygame
from events import Event
from cell import Cell
import random

class App:
    def __init__(self):
        self.size = self.width, self.height = 600, 800
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Number Sums")

        self.font = pygame.font.Font(None, 24)
        self.grid = []
        self.grid_rows = 5
        self.grid_columns = 5
        self.rect_width = (self.width // self.grid_columns)
        self.rect_height = (self.height // self.grid_rows)

        for row in range(self.grid_rows):
            g_row = []
            for col in range(self.grid_columns):
                text = f"{random.randint(1, 20)}"
                x = col * self.rect_width
                y = row * self.rect_height
                g_row.append(Cell(x, y, self.rect_width, self.rect_height, text))
            self.grid.append(g_row)

        self.running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill((255, 255, 255))
        for row in self.grid:
            for cell in row:
                cell.draw(self.screen, self.font)
        
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.run()