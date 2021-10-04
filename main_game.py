import pygame
import sys
import random
import json
import intropage

pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappybird")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.TTF", 40)


# for score display

def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(200, 100))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        score_surface = game_font.render(f"Score: {int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(200, 100))
        screen.blit(score_surface, score_rect)
        highscore_surface = game_font.render(f"Highscore: {int(highscore)}", True, (255, 255, 255))
        highscore_rect = highscore_surface.get_rect(center=(200, 550))
        screen.blit(highscore_surface, highscore_rect)

#for updating score
def update_score(score, highscore):
    if score > highscore:
        highscore = score


    return highscore


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
            hit_sound.play()
            return False

    if bird_rect.top < -100 or bird_rect.bottom >= 600:
        hit_sound.play()
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

#to update score when bird passes pipe
def pipe_scorecheck():
    global score, can_score
    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and can_score:
                score_sound.play()
                score += 1
                can_score = False
            if pipe.centerx < 0:
                can_score = True

class Resetbutton():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):
        action =False
        #get mosue position
        pos=pygame.mouse.get_pos()

        #check if mouse is over the button

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True



        #draw button
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):
        action =False
        #get mouse position
        pos=pygame.mouse.get_pos()

        #check if mouse is over the button

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True



        #draw button
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action



# for introloop
def intro_loop():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and intro_active == True:


                    game_loop()
        screen.blit(intro_image, (0, 0))
        font = pygame.font.Font("FlappyBirdy.ttf", 100)
        text_font = pygame.font.Font("FlappyBirdy.ttf", 50)
        title = font.render("Flappy Bird", True, (250, 250, 250))
        text = text_font.render("Press space to play", True, (250, 250, 250))
        highscore_surface = game_font.render(f"Highscore: {int(highscore)}", True, (255, 255, 255))
        highscore_rect = highscore_surface.get_rect(center=(200, 550))

        screen.blit(highscore_surface, highscore_rect)
        screen.blit(title, (72, 200))
        screen.blit(introbird_mid, (200, 350))
        screen.blit(text, (90, 600))

        pygame.display.update()
        clock.tick(120)



#for highscore database

try:
    with open('High_score.txt') as score_files:
        data = json.load(score_files)
except:
    data = {"high": 0}

highscore=data['high']

# Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
can_score = True
intro_active = True

# introimage
intro_image = pygame.image.load("background-night.png").convert()
intro_image = pygame.transform.scale(intro_image, (400, 700))
introbird_mid = pygame.image.load("bluebird-midflap.png").convert_alpha()

# For background image
bg_surface = pygame.image.load('background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (400, 700))

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

#gameover
game_over_surface = pygame.image.load("gameover.png").convert_alpha()

game_over_rect = game_over_surface.get_rect(center=(200, 300))

#for sound
flap_sound=pygame.mixer.Sound('flap.wav')
hit_sound=pygame.mixer.Sound("hit.wav")
score_sound=pygame.mixer.Sound("score.wav")

#for button

button_img=pygame.image.load("quit.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (50, 50))
button=Button(100,400,button_img)

reset_button=pygame.image.load("restart.png").convert_alpha()
#back_button = pygame.transform.scale(back_button, (73, 73))
resetbutton=Resetbutton(220,400,reset_button)

# gameloop


def game_loop():
    global game_active
    global pipe_list
    global bird_movement
    global bird_surface
    global bird_rect
    global floor_x_pos
    global bird_index
    global score
    global highscore
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data['high']=highscore
                with open('High_score.txt','w') as score_file:
                    json.dump(data,score_file)

                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active == True:
                    bird_movement = 0
                    bird_movement -= 8
                    flap_sound.play()

            #if event.type == pygame.KEYDOWN:
                 #if event.key == pygame.K_SPACE and game_active == False:
                    #game_active = True
                    #pipe_list.clear()
                    #bird_rect.center = (100, 350)
                    #bird_movement = 0
                    #score = 0


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
            pipe_scorecheck()
            score_display("main_game")
        else:
            # score
            highscore = update_score(score, highscore)
            screen.blit(game_over_surface, game_over_rect)
            score_display("game_over")
            if button.draw()==True:
                data['high'] = highscore
                with open('High_score.txt', 'w') as score_file:
                    json.dump(data, score_file)

                pygame.quit()
                sys.exit()
            if resetbutton.draw()==True:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 350)
                bird_movement = 0
                score = 0



        # floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -400:
            floor_x_pos = 0
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
