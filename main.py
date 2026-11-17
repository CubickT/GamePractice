import pygame

from Player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Bob is killing again")
clock = pygame.time.Clock()
running = True
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    
    keys = pygame.key.get_pressed()
    player.player_loop(keys, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()