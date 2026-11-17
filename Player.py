import pygame
from pygame.math import Vector2

move_keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

class Player:

    def __init__(self):
        self.x = 400
        self.y = 300
        self.size = 50

        self.velocity = Vector2(0,0)
        self.speed = 5

    def draw_player(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.size, self.size))

    def check_buttons(self, keys):

        if not any(keys[key] for key in move_keys):
            self.velocity = Vector2(0,0)
            return

        if keys[pygame.K_w]: self.velocity.y -= 1
        if keys[pygame.K_s]: self.velocity.y += 1
        if keys[pygame.K_a]: self.velocity.x -= 1
        if keys[pygame.K_d]: self.velocity.x += 1

    def move(self):
        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize() * self.speed
            self.x += self.velocity.x
            self.y += self.velocity.y

    def player_loop(self, keys, screen):
        self.check_buttons(keys)
        self.move()
        self.draw_player(screen)