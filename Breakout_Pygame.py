import pygame
from time import sleep

pygame.init()

MAX_BRICKS = 84
blocks_gone = 0
life = 5

BLUE = (66, 72, 200)
GREEN = (72, 160, 72)
YELLOW = (162, 162, 42)
YELLOW2 = (180, 122, 48)
ORANGE = (198, 108, 58)
RED = (200, 72, 72)
black = (0, 0, 0)
gray = (142, 142, 142)

# Sound
bounce = pygame.mixer.Sound("bounce.wav")
lose = pygame.mixer.Sound("lose.wav")

# Screen definition
size = (578, 540) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - Pygame Edition")

score_font = pygame.font.Font('Sprites/PressStart2P.ttf', 44)
score_text = score_font.render('5', True, gray, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (289, 36)

game_over_font = pygame.font.Font('Sprites/PressStart2P.ttf', 44)
game_over = game_over_font.render('GAME OVER', True, gray, black)
game_over_rect = score_text.get_rect()
game_over_rect.center = (120, 270)


# Bricks
class Wall:
    def __init__(self):
        self.bricks = []
        self.width = (size[0] - 88) // 14
        self.height = 20

    def create_wall(self):
        self.bricks = []
        for line in range(6):
            line_bricks = []
            for col in range(14):
                bricks_x = 44 + self.width * col
                bricks_y = 164 + self.height * line
                rect = pygame.Rect(bricks_x, bricks_y, self.width, self.height)

                # Block strength
                if line < 1:
                    level = 1
                elif line < 2:
                    level = 2
                elif line < 3:
                    level = 3
                elif line < 4:
                    level = 4
                elif line < 5:
                    level = 5
                elif line < 6:
                    level = 6
                individual_bricks = [rect, level]
                line_bricks.append(individual_bricks)
            self.bricks.append(line_bricks)

    def draw_wall(self):
        for line in self.bricks:
            for brick in line:
                if brick[1] == 1:
                    color_brick = RED
                elif brick[1] == 2:
                    color_brick = ORANGE
                elif brick[1] == 3:
                    color_brick = YELLOW2
                elif brick[1] == 4:
                    color_brick = YELLOW
                elif brick[1] == 5:
                    color_brick = GREEN
                elif brick[1] == 6:
                    color_brick = BLUE
                pygame.draw.rect(screen, color_brick, brick[0])

               
# Player
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

wall = Wall()
wall.create_wall()

back = pygame.image.load("Sprites/background_atari.png")

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

    if life > 0:
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

        # Players collision
        if player_x > 474:  # Right wall
            player_x = 474

        if player_x < 44:  # Left wall
            player_x = 44

        # Ball collision
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

        if ball_y < 104:  # Upper wall
            ball_y = 104
            ball_dy *= -1
            bounce.play()

        if ball_y > 540:
            life -= 1
            ball_x = 284
            ball_y = 284
            ball_dx = 2.5
            ball_dy = 2.5
            lose.play()

        if 496 > ball_y > 486:
            if ball_x + 10 > player_x:
                if player_x + 60 > ball_x: 
                    if player_x + 50 > ball_x > player_x + 10:
                        ball_dx *= 1.05
                        bounce.play()
                    else:
                        ball_dx *= -1.05
                        bounce.play()
                    ball_y = 486
                    ball_dy *= -1
                    bounce.play()

        for row in wall.bricks:
            for item in row:
                if item[0][1] + 20 > ball_y > item[0][1]:
                    if ball_x + 10 > item[0][0]:
                        if item[0][0] + item[0][2] > ball_x:  
                            ball_dy *= -1
                            item[0] = (0, 0, 0, 0)
                            bounce.play()
                            blocks_gone += 1
                        
        if blocks_gone == MAX_BRICKS:
            blocks_gone = 0
            ball_x = 284
            ball_y = 284
            wall.create_wall()
            sleep(2)

        score_text = score_font.render(str(life), True, gray, black)
    
        screen.blit(back, (0, 60))
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
