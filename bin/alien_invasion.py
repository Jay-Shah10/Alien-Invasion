import os
import sys
import pygame

from bin.settings import Settings
from bin.ship import Ship
from bin import game_function as gf


def run_game():
    # init of pygame.

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship.
    ship = Ship(setting=settings, screen=screen)

    # Strating the main loop.
    while True:
        # Watch for mouse and key events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)


run_game()
