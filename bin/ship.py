import os
import pygame


class Ship():
    def __init__(self, setting, screen):
        """
        Constructor.
        Init the ship and set its starting position.
        :param setting: Setting page.
        :param screen: Game screen.
        """

        self.screen = screen
        self.setting = setting

        # Load the ship image and get its rectangle.
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'ship.png')
        )
        self.rect = self.image.get_rect()  # gets the rect of an image.
        self.screen_rect = screen.get_rect()  # screens rect.

        # Start each new ship at the bottom center of the Screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        self.move_right = False  # Movement Flag.
        self.move_left = False  # Left movement flag.

    def update(self):
        """
        Updates the ship's position.
        :return: Ship's location.
        """
        # Updating the ship's center value, not the rect.
        if self.move_right and self.rect.right < self.screen_rect.right:  # Stops the ship when hit right wall.
            self.center += self.setting.ship_speed_factor

        elif self.move_left and self.rect.left > 0:  # stops ship when it hits the left wall.
            self.center -= self.setting.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """
        Draws the ship at its current location.
        :return: ship's location.
        """
        self.screen.blit(self.image, self.rect)
