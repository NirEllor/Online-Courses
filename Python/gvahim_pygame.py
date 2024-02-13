import pygame

""" Constants"""
WINDOWS_WIDTH = 990
WINDOWS_HEIGHT = 800
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
WALLPAPER = "sonic_heroes_wallpaper.jpg"
LEFT = 1
SCROLL = 2
RIGHT = 3
SOUND_FILE = "Sonic Heroes - Round Clear.mp3"

""" Initializing"""
pygame.init()
pygame.mixer.init()

"""Defining the objects of the game """
screen = pygame.display.set_mode(size)
wallpaper = pygame.image.load(WALLPAPER)
sprite = pygame.image.load("wikimedia-button.png").convert()

""" Defining outwardly features"""
pygame.display.set_caption("Are you stupid?..")
pygame.mouse.set_visible(True)
pygame.mixer.music.load(SOUND_FILE)

"""" Setting variables for the following while loop + bliting the wallpaper already"""
screen.blit(wallpaper, (0, 0))
x, y = pygame.mouse.get_pos()
events_keyboard = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
finish = False

"""The main while loop"""
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            finish = True
        elif event.type == pygame.KEYDOWN and event.key in events_keyboard:  # Pressing on keyboard's arrows
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y += 1
                screen.blit(sprite, (x, y))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y -= 1
                screen.blit(sprite, (x, y))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                x += 1
                screen.blit(sprite, (x, y))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                x -= 1
                screen.blit(sprite, (x, y))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:  # Left-click on the mouse
            screen.blit(sprite, (x, y))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # click on space
            screen.blit(wallpaper, (0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:  # Right-click on the mouse
            pygame.mixer.music.play()
        pygame.display.flip()  # Screening all the code in the loop
pygame.quit()
