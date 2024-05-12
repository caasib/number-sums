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

        row_sums = [random.randint(1, 30) for x in range(self.grid_rows)]

        for row, row_sum in enumerate(row_sums):
            grid_row = []
            grid_row.append(Cell(0, row * self.rect_height, self.rect_width, self.rect_height, str(row_sum)))
            remaining_sum = row_sum
            cell_values = []

            for _ in range(1, self.grid_columns):
                if remaining_sum <= 0:
                    text = str(random.randint(1, 20))
                    cell_values.append(text)
                else:
                    text = str(random.randint(1, remaining_sum))
                    cell_values.append(text)
                    remaining_sum -= int(text)
            
            random.shuffle(cell_values)

            for col, val in enumerate(cell_values, start=1):
                x = col * self.rect_width
                y = row * self.rect_height
                grid_row.append(Cell(x, y, self.rect_width, self.rect_height, val))
            
            if (row == 0 and row_sum == row_sums[0]):
                grid_row.pop(0)
            
            self.grid.append(grid_row)

        self.running = True
 
    def is_outer_cell(self, row, col):
        return row == 0 or row == self.grid_rows - 1 or col == 0 or col == self.grid_columns - 1
    
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