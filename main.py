import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Odds and Probability")

# Load Assets
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Quit', True, color)

# Load and scale background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "background-black.png")),
    (WIDTH, HEIGHT)
)


def redraw_window():
    """Draws the game window."""
    win.blit(BG, (0, 0))
    pygame.display.update()


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()


def menu():
    """Displays the menu with a quit button."""
    while True:
        win.fill((255, 255, 255))  # Clear screen
        mouse = pygame.mouse.get_pos()  # Get mouse position

        # Draw button
        if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 140 and HEIGHT / 2 <= mouse[1] <= HEIGHT / 2 + 40:
            pygame.draw.rect(win, color_light, [WIDTH / 2, HEIGHT / 2, 140, 40])
        else:
            pygame.draw.rect(win, color_dark, [WIDTH / 2, HEIGHT / 2, 140, 40])

        # Draw button text
        win.blit(text, (WIDTH / 2 + 50, HEIGHT / 2))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + 140 and HEIGHT / 2 <= mouse[1] <= HEIGHT / 2 + 40:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# Run the game
menu()
main()
