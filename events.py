import pygame

class Event:
    def __init__(self):
        self.exit = False

    def on_mouse_click(self):
        pass

    def on_resize(self):
        pygame.display.flip()

    def on_exit(self):
        self.exit = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.on_mouse_click()
        elif event.type == pygame.VIDEORESIZE:
            self.on_resize()