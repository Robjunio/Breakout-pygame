import pygame


pygame.init()

# Definir a classe de blocos pra quebrar


# Definição de cores
#4248C8
#48A048
#A2A22A
#B47A30
#C66C3A
#C84848
#FFF9F9
COLOR_BLACK = (0, 0, 0)

# Definição da tela
size = (1280, 720)  # Podemos alterar
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - Pygame Edition")

# Definindo os audios


# player 1
player_1 = pygame.image.load("Sprites/player_1.png")
player_1_x = 640
player_1_move_right = False
player_1_move_left = False

# Bola
bola = pygame.image.load("Sprites/bola.png")
bola_x = 640
bola_y = 150
bola_dy = 5
bola_dx = 5

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1_move_left = True
            if event.key == pygame.K_RIGHT:
                player_1_move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1_move_left = False
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False

        screen.fill(COLOR_BLACK)
        
        # ball movement
        bola_x = bola_x + bola_dx
        bola_y = bola_y + bola_dy

         # player 1 up movement
        if player_1_move_right:
            player_1_x += 20
        else:
            player_1_x += 0

        # player 1 down movement
        if player_1_move_left:
            player_1_x -= 20
        else:
            player_1_x += 0


        # drawing objects
        screen.blit(bola, (bola_x, bola_y))
        screen.blit(player_1, (player_1_x, 50))
        
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
