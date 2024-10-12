import pygame
import os
import random

pygame.init()

WIDTH, HEIGHT =1280, 640
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

FONT = pygame.font.Font("pong\pong.ttf", 54)

BG_GREY = (32,32,32)
FPS = 60

SPEED = 7
BALL_SPEED = 15

SCORE_PLAYER = 0
SCORE_ENNEMY = 0

pong_sound = pygame.mixer.Sound("pong\pong.wav")
score_sound = pygame.mixer.Sound("pong\score.wav")
score_ennemy_sound = pygame.mixer.Sound("pong\score_ennemy.wav")


player = pygame.image.load(os.path.join("pong","pong_player.png"))
ennemy = pygame.image.load(os.path.join("pong","pong_player.png"))
ball = pygame.image.load(os.path.join("pong","ball.png"))


def draw_window(player_sprite,ennemy_sprite,ball_sprite):

    score_text = FONT.render(str(SCORE_PLAYER),True,(255,255,255))
    score_text_en = FONT.render(str(SCORE_ENNEMY),True,(255,255,255))

    score_text_rect = score_text.get_rect()
    score_text_en_rect = score_text_en.get_rect()

    score_text_rect.center = (570, 40)
    score_text_en_rect.center = (720, 40)

    WINDOW.fill(BG_GREY)
    WINDOW.blit(player, (player_sprite.x,player_sprite.y))
    WINDOW.blit(ennemy, (ennemy_sprite.x,ennemy_sprite.y))
    WINDOW.blit(ball, (ball_sprite.x,ball_sprite.y))
    WINDOW.blit(score_text, score_text_rect)
    WINDOW.blit(score_text_en, score_text_en_rect)
    pygame.display.update()

def player_movement(keys_pressed,player_sprite):
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_z]) and player_sprite.y > 1 :
        player_sprite.y -= SPEED
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and player_sprite.y < 639-200:
        player_sprite.y += SPEED

def main():
    global SCORE_PLAYER,SCORE_ENNEMY

    player_sprite = pygame.Rect(50,220,20,200)
    ennemy_sprite = pygame.Rect(1210,220,20,200)
    ball_sprite = pygame.Rect(626,306,30,30)

    BALL_DIR_X = random.randint(5,BALL_SPEED)
    BALL_DIR_Y = BALL_SPEED - BALL_DIR_X

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()                     # Controles du joueur
        player_movement(keys_pressed,player_sprite)
        
        ball_sprite.x += BALL_DIR_X                                 #direction de la balle
        ball_sprite.y += BALL_DIR_Y

        if ball_sprite.y < 1 or ball_sprite.y > 639-30:
            pygame.mixer.Sound.play(pong_sound)   
            if BALL_DIR_Y >= 1 or BALL_DIR_Y <= -1:        #collision avec les bords Y
                BALL_DIR_Y *= -1
            else:
                BALL_DIR_Y +=1
        if ball_sprite.colliderect(player_sprite):
            pygame.mixer.Sound.play(pong_sound) #collision avec les joueurs
            if (ball_sprite.y+14) < player_sprite.y+75:
                BALL_DIR_X *= -1.05 
                BALL_DIR_Y = -2
            elif (ball_sprite.y+14) > player_sprite.y+125:
                BALL_DIR_X *= -1.05 
                BALL_DIR_Y = +2
            else:
                BALL_DIR_X *= -1.05 

        if ball_sprite.colliderect(ennemy_sprite):
            pygame.mixer.Sound.play(pong_sound) #collision avec les joueurs
            if (ball_sprite.y+14) < ennemy_sprite.y+75:
                BALL_DIR_X *= -1.05 
                BALL_DIR_Y = -2
            elif (ball_sprite.y+14) > ennemy_sprite.y+125:
                BALL_DIR_X *= -1.05 
                BALL_DIR_Y = +2
            else:
                BALL_DIR_X *= -1.05 


        if ball_sprite.y < ennemy_sprite.y+randomIa and BALL_DIR_X > 0:    #ia ennemy                   
                ennemy_sprite.y -= SPEED-1
                randomIa = random.randint(50,150)
        if ball_sprite.y > ennemy_sprite.y+randomIa and BALL_DIR_X > 0:
                ennemy_sprite.y += SPEED-1
                randomIa = random.randint(50,150)

        if ennemy_sprite.y >= 639-200:                             #collision avec bords ia
            ennemy_sprite.y = 639-200
        if ennemy_sprite.y <= 1:
            ennemy_sprite.y = 1

        if ball_sprite.x <= 0:
            SCORE_ENNEMY += 1
            pygame.mixer.Sound.play(score_ennemy_sound)
            ball_sprite.x = 626
            ball_sprite.y = 306
            if SCORE_ENNEMY <= 10:
                BALL_DIR_X = random.randint(5,BALL_SPEED)
                BALL_DIR_Y = BALL_SPEED - BALL_DIR_X
            else:
                run = False

        if ball_sprite.x >= 1280:
            SCORE_PLAYER += 1
            pygame.mixer.Sound.play(score_sound)
            ball_sprite.x = 626
            ball_sprite.y = 306
            if SCORE_PLAYER <= 10:
                BALL_DIR_X = random.randint(5,BALL_SPEED)
                BALL_DIR_Y = BALL_SPEED - BALL_DIR_X
            else:
                run = False

        draw_window(player_sprite,ennemy_sprite,ball_sprite)

    pygame.quit()


if __name__ == "__main__":
    main()
