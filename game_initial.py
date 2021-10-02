import pygame
import sys
import random


screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappybird")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# For background Image
bg_surface = pygame.image.load('background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (400, 700))

# for pipes
pipe_surface = pygame.image.load("pipe-green.png")

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

game_loop()