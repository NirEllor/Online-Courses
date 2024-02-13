# Imports
import pygame
import random
from shapes import Sticker


#  Constants
WINDOWS_WIDTH = 999
WINDOWS_HEIGHT = 800
WALLPAPER = "sonic_heroes_wallpaper.jpg"
LEFT = 1
REFRESH_RATE = 50
MAX_VELOCITY = 10


#  General variables for PyGame
wallpaper = pygame.image.load(WALLPAPER)
pygame.init()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
screen.blit(wallpaper, (0, 0))
clock = pygame.time.Clock()


#  Variables for the while loop
stickers_list = pygame.sprite.Group()
new_stickers_list = pygame.sprite.Group()

finish = False

#  The main while loop of the game
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            finish = True

        # Add a sticker each time user clicks on the left button of the mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            sticker = Sticker(x, y)

            vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)  # Each sticker velocity is different and random
            vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)  # Each sticker velocity is different and random
            sticker.update_velocity(vx, vy)

            stickers_list.add(sticker)  # Adding the created sticker object to the list containing sticker's objects

    # update stickers locations, bounce from edges
    for sticker in stickers_list:
        sticker.update_location()

        x, y = sticker.get_location()
        vx, vy = sticker.get_velocity()

        if x <= 0 or x >= WINDOWS_WIDTH:
            vx *= -1  # Opposite velocity
            stickers_list.draw(screen)
        if y <= 0 or y >= WINDOWS_HEIGHT:
            vy *= -1  # Opposite velocity

        sticker.update_velocity(vx, vy)

    # Find which stickers collide and should be removed
    new_stickers_list.empty()  # If we don't empty this list, collided stickers will stay on the screen
    for sticker in stickers_list:
        stickers_hit_list = pygame.sprite.spritecollide(sticker, stickers_list, False)
        if len(stickers_hit_list) == 1:  # stickers collides only with itself
            new_stickers_list.add(sticker)  # Since we only want stickers that don't collide with any other
            # stickers but themselves

    # copying the surviving stickers to the stickers_list that about to be represented on the screen
    stickers_list.empty()  # If we don't empty this list, collided stickers will stay on the screen
    for sticker in new_stickers_list:
        stickers_list.add(sticker)  # adding the surviving stickers on the screen

    # update screen with surviving balls
    screen.blit(wallpaper, (0, 0))  # If we don't blit the wallpaper, then signatures of the stickers
    # will be left on the screen
    stickers_list.draw(screen)  # Drawing the surviving stickers on the screen

    pygame.display.flip()
    clock.tick(REFRESH_RATE)
pygame.quit()
