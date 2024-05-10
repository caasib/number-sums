import pygame

class Cell:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
    
    def draw(self, screen, font):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.rect.inflate(-4, -4))
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)