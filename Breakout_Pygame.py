import pygame


pygame.init()

# Definir a classe de blocos pra quebrar

# Definição da tela
size = (578, 540)  # Podemos alterar
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - Pygame Edition")

# Definindo os audios


# game loop
game_loop = True
game_clock = pygame.time.Clock()

azul = (66, 72, 200)
verde = (72, 160, 72)
amarelo =(162, 162, 42)
amarelo_escuro = (180, 122, 48)
laranja = (198, 108, 58)
vermelho = (200, 72, 72)
black = (0, 0, 0)

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
player_1 = pygame.image.load("Sprites/paddle.png")
player_1_x = 269
player_1_move_right = False
player_1_move_left = False
wall = wall()
wall.create_wall()

back = pygame.image.load("Sprites/fundo_atari.png")

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
           
        # Player right movement
        if player_1_move_right:
            player_1_x -= 10
        else:
            player_1_x += 0

        # Player left movement
        if player_1_move_right:
            player_1_x += 10
        else:
            player_1_x += 0   
        
        screen.blit(back, (0,60))
        screen.blit(player_1, (player_1_x, 496))
        
    pygame.display.flip()
    game_clock.tick(45)

pygame.quit()
