import sys
import pygame


def check_events(ship):
    # Responds to key presses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship right by one.
                ship.move_right = True

        elif event.type == pygame.KEYUP:
            # if the key is released it will stop the movement.
            if event.key == pygame.K_RIGHT:
                ship.move_right = False


def update_screen(settings, screen, ship):
    """
    Update the images on the screen and flip to the new screen.
    :param settings: alien invasion settings.
    :param screen: pygame screen.
    :param ship: alien invasion ship.
    :return: displays all.
    """

    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    ship.blitme()

    # make the most recent drawn screen visible.
    pygame.display.flip()
