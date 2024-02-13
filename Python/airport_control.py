# Imports
import pygame
import random
from plane_class import Plane

# Constants
WALLPAPER = "perfect_background.jpg"
WALLPAPER_WIDTH = 800
WALLPAPER_HEIGHT = 800
LEFT = 1
REFRESH_RATE = 50
MAX_VELOCITY = 10
MAX_SHIFT = 40


def main():

    """ Launching the 'main' function will return the game"""

    #  General variables for PyGame
    size = (WALLPAPER_WIDTH, WALLPAPER_HEIGHT)
    wallpaper = pygame.image.load(WALLPAPER)
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Airplane_control")
    screen.blit(wallpaper, (0, 0))
    clock = pygame.time.Clock()

    #  Variables for the while loop

    planes_list = pygame.sprite.Group()  # Detecting collided planes
    new_planes_list = pygame.sprite.Group()  # Collecting surviving plane
    lst_all_moves = 0  # Counter for  all airplanes' moves in order to know if the limit has been reached
    lst_moves = []  # A list of moves that refreshes every time a left click on the mouse is executed
    commands = 0  # Counter for all the commands being ordered in the following if statements inside the while loop
    finish = False  # Boolean value in order to stop the game as needed

    while not finish:

        # Stop the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            # Add a plane each time user clicks on the left button of the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:

                lst_moves.clear()  # Refreshing the list in order to track the first position of each plane
                x, y = pygame.mouse.get_pos()
                plane = Plane(x, y)  # x and y are the first position of the plane
                vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)  # Each plane velocity is different and random
                vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)  # Each plane velocity is different and random
                plane.update_velocity(vx, vy)

                planes_list.add(plane)  # Adding the created plane object to the list containing plane's objects
        # update planes locations, bounce from edges

        i = 0  # Counter for tracking the first position of each plane, starting from the first plane

        for plane in planes_list:
            plane.update_location()
            x, y = plane.get_location()
            tmp = [x, y]  # Creating this variable in order to append both x and y at the same time as current position
            lst_moves.append(tmp)
            lst_all_moves += 1

            vx, vy = plane.get_velocity()

            #  Stopping the game if we reach 1000 moves by all planes in the screen
            if lst_all_moves >= 1000:
                finish = True
                print(f"Game over, you reached {lst_all_moves} moves, beyond the limit, with {commands}"
                      f" manual commands.")
                break

            #  Commands for each special behavior of the plane
            if tmp[0] <= 0 or tmp[0] >= WALLPAPER_WIDTH:
                vx *= -1  # Opposite velocity
                commands += 1
            if tmp[1] <= 0 or tmp[1] >= WALLPAPER_HEIGHT:
                vy *= -1  # Opposite velocity
                commands += 1
            if abs(tmp[0] - lst_moves[i][0]) >= MAX_SHIFT:
                vx *= -1  # Opposite velocity
                commands += 1
            if abs(tmp[1] - lst_moves[i][1]) >= MAX_SHIFT:
                vy *= -1  # Opposite velocity
                commands += 1

            plane.update_velocity(vx, vy)
            i += 1

        # Find which planes collide and should be removed
        new_planes_list.empty()  # If we don't empty this list, collided planes will stay on the screen
        for plane in planes_list:
            planes_hit_list = pygame.sprite.spritecollide(plane, planes_list, False)
            if len(planes_hit_list) == 1:  # planes collides only with itself
                new_planes_list.add(plane)  # Since we only want planes that don't collide with any other
                # planes but themselves
            elif len(planes_hit_list) > 1:
                finish = True
                print(f"Game over, a collision occurred. So far you reached {lst_all_moves} moves with {commands}"
                      f" manual commands. ")
                break

        # copying the surviving planes to the planes_list that about to be represented on the screen
        planes_list.empty()  # If we don't empty this list, collided planes will stay on the screen
        for plane in new_planes_list:
            planes_list.add(plane)  # adding the surviving planes on the screen

        # update screen with surviving balls
        screen.blit(wallpaper, (0, 0))  # If we don't blit the wallpaper, then signatures of the planes
        # will be left on the screen
        planes_list.draw(screen)  # Drawing the surviving planes on the screen

        pygame.display.flip()
        clock.tick(REFRESH_RATE)
    pygame.quit()


if __name__ == '__main__':
    main()
