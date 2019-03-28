import sys
import pygame
from bin.bullet import Bullet


def check_events(settings, screen, ship, bullets):
    """
    checks for pygame events.
    These can be key presses or mouse clicks.
    :param ship: ship object.
    :return: Response to event.
    """
    # Responds to key presses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            # if the key is released it will stop the movement.
            check_keyup_events(event, ship)


def check_keydown_events(event, settings, screen, ship, bullets):
    """
    Responds to key pressing down.
    :param event: pygame event.
    :param ship: ship object
    :return: boolean
    """
    if event.key == pygame.K_RIGHT:
        # move the ship right by one.
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.type == pygame.K_SPACE:
        # Create a new bullet and add to group.
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """
    Responds to key releases.
    :param event: pygame event.
    :param ship: ship object.
    :return: boolean
    """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(settings, screen, ship, bullets):
    """
    Update the images on the screen and flip to the new screen.
    :param settings: alien invasion settings.
    :param screen: pygame screen.
    :param ship: alien invasion ship.
    :return: displays all.
    """

    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()


    # make the most recent drawn screen visible.
    pygame.display.flip()
