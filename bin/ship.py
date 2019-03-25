import os
import pygame
from pygame import Surface


class Ship():
    def __init__(self, screen):
        """ init the ship and set its starting position."""

        self.screen = screen

        # Load the ship image and get its rectangle.
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'ship.png')
        )
        # self.rect = Surface.get_rect(self.image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start each new ship at the bottom center of the Screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement Flag.
        self.move_right = False

    def update(self):
        """ Updates the ship's position based on the movement flag."""
        if self.move_right:
            self.rect.centerx += 1

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
