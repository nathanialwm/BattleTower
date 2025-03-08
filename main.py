import pygame
import sys

import config as cfg
import ui

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((cfg.WINDOW_W, cfg.WINDOW_H))
pygame.display.set_caption(cfg.TITLE)

# Set up clock
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    screen.blit(ui.battlePage, (0, 0))

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()