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


vermelho = (255, 0, 0)
verde = (0, 255, 0)
laranja = (255, 165, 0)
amarelo = (255, 255, 0)

#blocos
class wall():
    def __init__(self):
        self.width = size[0] // 14
        self.height = 50

    def create_wall(self):
        self.blocos = []
        bloco_individual = []

        for linha in range(8):
            linha_blocos = []

            for col in range(14):
                bloco_x = self.width * col
                bloco_y = self.height * linha
                rect = pygame.Rect(bloco_x, bloco_y, self.width, self.height)

                #força do bloco
                if linha < 2:
                    strength = 4
                elif linha < 4:
                    strength = 3
                elif linha < 6:
                    strength = 2
                elif linha < 8:
                    strength = 1

                bloco_individual = [rect, strength]

                linha_blocos.append(bloco_individual)
            self.blocos.append(linha_blocos)

    def draw_wall(self):
        for linha in self.blocos:
            for bloco in linha:
                if bloco[1] == 4:
                    cor_bloco = vermelho
                elif bloco[1] == 3:
                    cor_bloco = laranja
                elif bloco[1] == 2:
                    cor_bloco = verde
                elif bloco[1] == 1:
                    cor_bloco = amarelo
                pygame.draw.rect(screen, cor_bloco, bloco[0])
                pygame.draw.rect(screen, COLOR_BLACK, bloco[0], 10)

wall = wall()
wall.create_wall()


while game_loop:
    wall.draw_wall()
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
