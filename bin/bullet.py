import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    A class manages bullets. These will shoot out of the ship.
    """
    def __init__(self, settings, screen, ship):
        """
        Constructor. Create a bullet
        :param settings: alien invasion settings.
        :param screen: pygame screen.
        :param ship: alien ship.
        """
        super(Bullet, self).__init__()
        self.screen = screen

        # Bullet rect at (0, 0), then correct position.
        self.rect = pygame.Rect(0,0,settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx # center of the ship.
        self.rect.top = ship.rect.top # top of the ship.

        # Bullet's position stored as decimal value.
        self.y = float(ship.rect.y)

        self.color = settings.bullet_color # bullet's color.
        self.speed_factor = settings.bullet_speed_factor # bullet's speed.

    def update(self):
        """
        Move the bullet up the screen.
        :return:
        """
        # update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet.
        :return:
        """
        pygame.draw.rect(Surface=self.screen, color=self.color, Rect=self.rect)

