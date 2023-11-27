import pygame

class Square:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.abs_x = x * width
        self.abs_y = y * height

        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)

        self.color = "dark" if (x + y) % 2 else "light"
        self.draw_color = (53, 53, 53) if self.color == "dark" else (220, 208, 194)
        self.highlight_color = (100, 249, 83) if self.color == "light" else (0, 228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x, self.abs_y, self.width, self.height
        )

    def get_coord(self):
        columns = "abcdefgh"
        return columns[self.x] + str(self.y + 1)
    
    def draw(self, display):
        pygame.darw.rect(display, self.highlight_color if self.highlight else self.draw_color, self.rect)

        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
            