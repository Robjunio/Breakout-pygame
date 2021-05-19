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
#000

# Definição da tela
size = (1280, 720)  # Podemos alterar
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - Pygame Edition")

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
