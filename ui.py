import pygame

import config as cfg

battlePage = pygame.Surface((cfg.WINDOW_W, cfg.WINDOW_H))
battlePage.fill(cfg.WHITE)

def draw_ui(surface):
    """
    Draw all static UI elements to the given surface.
    """
    # Example: Draw a background
    surface.fill((cfg.LGREY))