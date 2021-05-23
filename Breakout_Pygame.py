import pygame
from time import sleep

pygame.init()

MAX_BLOCOS = 84
blocks_gone = 0
lifes = 5

azul = (66, 72, 200)
verde = (72, 160, 72)
amarelo =(162, 162, 42)
amarelo_escuro = (180, 122, 48)
laranja = (198, 108, 58)
vermelho = (200, 72, 72)
black = (0, 0, 0)
gray = (142, 142, 142)

# Sound
bounce = pygame.mixer.Sound("bounce.wav")

# Definição da tela
size = (578, 540) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - Pygame Edition")

score_font = pygame.font.Font('Sprites/PressStart2P.ttf', 44)
score_text = score_font.render('5', True, gray, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (289, 36)

game_over = pygame.font.Font('Sprites/PressStart2P.ttf', 44)
game_over = score_font.render('GAME OVER', True, gray, black)
game_over_rect = score_text.get_rect()
game_over_rect.center = (120, 270)

# Defining colors


#blocos
class wall():
    def __init__(self):
        self.width = (size[0] - 88) // 14
        self.height = 20

    
    def create_wall(self):
        self.blocos = []
        bloco_individual = []
        for linha in range(6):
            linha_blocos = []
            for col in range(14):
                bloco_x = 44+ self.width* col
                bloco_y = 164 + self.height * linha
                rect = pygame.Rect(bloco_x, bloco_y, self.width, self.height)

                #força do bloco
                if linha < 1:
                    level = 1
                elif linha < 2:
                    level = 2
                elif linha < 3:
                    level = 3
                elif linha < 4:
                    level  = 4
                elif linha < 5:
                    level = 5
                elif linha < 6:
                    level = 6
                bloco_individual = [rect, level]
                linha_blocos.append(bloco_individual)
            self.blocos.append(linha_blocos)


    def draw_wall(self):
        for linha in self.blocos:
            for bloco in linha:
                if bloco[1] == 1:
                    cor_bloco = vermelho
                elif bloco[1] == 2:
                    cor_bloco = laranja
                elif bloco[1] == 3:
                    cor_bloco = amarelo_escuro
                elif bloco[1] == 4:
                    cor_bloco = amarelo
                elif bloco[1] == 5:
                    cor_bloco = verde
                elif bloco[1] == 6:
                    cor_bloco = azul
                pygame.draw.rect(screen, cor_bloco, bloco[0])

               
# player
player = pygame.image.load("Sprites/paddle.png")
player_x = 269
player_move_right = False
player_move_left = False

# Ball
ball = pygame.image.load("Sprites/Ball.png")
ball_x = 284
ball_y = 284
ball_dx = 2.5
ball_dy = 2.5

wall = wall()
wall.create_wall()

back = pygame.image.load("Sprites/fundo_atari.png")

game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move_left = True
            if event.key == pygame.K_RIGHT:
                player_move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_move_left = False
            if event.key == pygame.K_RIGHT:
                player_move_right = False

    if lifes > 0:            
        screen.fill(black)

        ball_x += ball_dx
        ball_y += ball_dy
        # Player right movement
        if player_move_right:
            player_x += 10
        else:
            player_x += 0

        # Player left movement
        if player_move_left:
            player_x -= 10
        else:
            player_x += 0   

        # Players colision
        if player_x > 474:  # Right wall
            player_x = 474

        if player_x < 44:  # Left wall
            player_x = 44

        # Ball colision
        if ball_x > 524:  # Right wall
            if ball_y < 500:
                ball_x = 524
                ball_dx *= -1
                bounce.play()
        if ball_x < 44:  # Left wall
            if ball_y < 500:
                ball_x = 44
                ball_dx *= -1
                bounce.play()
        if ball_y < 104: # Upper wall
            ball_y = 104
            ball_dy *= -1
            bounce.play()
        if ball_y > 540:
            lifes -= 1
            ball_x = 284
            ball_y = 284
            ball_dx = 2.5
            ball_dy = 2.5
            bounce.play()
        if 496 > ball_y > 486:
            if ball_x + 10 > player_x:
                if player_x + 60 > ball_x: 
                    if player_x + 50 >  ball_x > player_x + 10:
                        ball_dx *= 1.05
                        bounce.play()
                    else:
                        ball_dx *= -1.05
                        bounce.play()
                    ball_y = 486
                    ball_dy *= -1
                    bounce.play()
        for row in wall.blocos:
            for item in row:
                if item[0][1] + 20  > ball_y > item[0][1]:
                    if ball_x + 10 > item[0][0]:
                        if item[0][0] + item[0][2] > ball_x:  
                            ball_dy *= -1
                            item[0] = (0,0,0,0)
                            bounce.play()
                            blocks_gone += 1
                        
        if blocks_gone == MAX_BLOCOS:
            blocks_gone = 0
            ball_x = 284
            ball_y = 284
            wall.create_wall()
            sleep(2)

        score_text = score_font.render(str(lifes), True, gray, black)
    
        screen.blit(back, (0,60))
        screen.blit(player, (player_x, 496))
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(score_text, score_text_rect)
            
        wall.draw_wall()
    else:
        screen.fill(black)
        screen.blit(game_over, game_over_rect)
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
