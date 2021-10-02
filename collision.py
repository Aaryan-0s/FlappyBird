import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappybird")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# for moving floor
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 600))
    screen.blit(floor_surface, (floor_x_pos + 400, 600))



# function for pipe
def create_pipe():
    global bottom_pipe
    global top_pipe
    random_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(500, random_pos - 200))
    return bottom_pipe, top_pipe


# function to move pipes

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes


# functions to draw pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 500:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

# for collosion
def collision_check(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):

            return False

    if bird_rect.top < -100 or bird_rect.bottom >= 600:
        return False

    return True


# for rated  bird
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


# for bird animation
def bird_animation():
    new_bird = bird_frame[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect



# Game variables
gravity = 0.25
bird_movement = 0
game_active = True


# for floor surface
floor_surface = pygame.image.load("base.png").convert()
floor_surface = pygame.transform.scale(floor_surface, (400, 100))
floor_x_pos = 0


# for bird
bird_down = pygame.image.load("bluebird-downflap.png").convert_alpha()
bird_up = pygame.image.load("bluebird-upflap.png").convert_alpha()
bird_mid = pygame.image.load("bluebird-midflap.png").convert_alpha()
bird_frame = [bird_down, bird_up, bird_mid]
bird_index = 0
bird_surface = bird_frame[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 512))
bird_flap = pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap, 200)


# for pipes
pipe_surface = pygame.image.load("pipe-green.png")
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 500, 300]

# For background image
bg_surface = pygame.image.load('background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (400, 700))

def game_loop():
    global game_active
    global pipe_list
    global bird_movement
    global bird_surface
    global bird_rect
    global floor_x_pos
    global bird_index
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active == True:
                    bird_movement = 0
                    bird_movement -= 8

            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())

            if event.type == bird_flap:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                bird_surface, bird_rect = bird_animation()


        screen.blit(bg_surface, (0, 0))

        if game_active:
            # pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # birds

            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird, bird_rect)
            game_active = collision_check(pipe_list)
        else:
            print("collision")

        # floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -400:
            floor_x_pos = 0
        pygame.display.update()
        clock.tick(60)

game_loop()
