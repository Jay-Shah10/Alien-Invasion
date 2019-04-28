import os
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf



def run_game():
    # init of pygame.

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship.
    ship = Ship(setting=settings, screen=screen)
    # Bullet Group.
    bullets = Group()

    # Strating the main loop.
    while True:
        # Watch for mouse and key events.
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, bullets)


run_game()
