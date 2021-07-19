import os
import pygame
from pygame.locals import *

#===============================================================
#                          Screen
HEIGHT = 600
LENGTH = 1000
screen = pygame.display.set_mode((LENGTH,HEIGHT))
#===============================================================
#                          Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_path = os.getcwd() + '\\sprites'

        self.images = {'walk_bottom' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_00.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_01.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_02.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_03.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_04.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_05.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_06.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_07.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_08.png')),
                                        pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_bottom\\sprite_09.png'))
                        ),
                        'walk_top' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_00.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_01.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_02.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_03.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_04.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_05.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_06.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_07.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_08.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_top\\sprite_09.png'))
                                    ),
                        'walk_left' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_00.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_01.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_02.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_03.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_04.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_05.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_06.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_07.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_08.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_09.png'))
                        ),
                        'walk_right' : (pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_00.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_01.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_02.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_03.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_04.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_05.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_06.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_07.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_08.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite_link_walk_left\\sprite_09.png'),True,False))
                        ),
                        'stay_bottom' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_bottom_00.png')),
                                         pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_bottom_00.png'))
                        ),
                        'stay_top' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_top.png')),
                                      pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_top.png'))
                        ),
                        'stay_left' : (pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_left_00.png')),
                                       pygame.transform.scale2x(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_left_00.png'))
                        ),
                        'stay_right' : (pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_left_00.png'),True,False)),
                                        pygame.transform.scale2x(pygame.transform.flip(pygame.image.load(self.sprite_path + '\\sprite link\\sprite_stay_left_00.png'),True,False))
                        )
                        }

        self.speed = 15

        self.current_image = 0

        self.move_diretion = 'stay_bottom'

        self.image = self.images[self.move_diretion][self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[1] = 276
        self.rect[0] = 476

    def move_player(self):
        self.current_image = (self.current_image + 1) % len(self.images[self.move_diretion])
        self.image = self.images[self.move_diretion][self.current_image]

        if self.move_diretion == 'walk_bottom':
            self.rect[1] += self.speed

        elif self.move_diretion == 'walk_top':
            self.rect[1] -= self.speed

        elif self.move_diretion == 'walk_left':
            self.rect[0] -= self.speed

        elif self.move_diretion == 'walk_right':
            self.rect[0] += self.speed

        if self.rect.bottom > 599:
            self.rect[1] = 552

        if self.rect.top < 0:
            self.rect[1] = 0

        if self.rect.left < 0:
            self.rect[0] = 0

        if self.rect.right > 999:
            self.rect[0] = 952

    def update(self):
        self.move_player()

Link = Player()
Player_group = pygame.sprite.Group()
Player_group.add(Link)
#===============================================================
pygame.init()

Clock = pygame.time.Clock()
#===============================================================
#                        Main Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                Link.move_diretion = 'walk_bottom'

            elif event.key == K_UP:
                Link.move_diretion = 'walk_top'

            elif event.key == K_LEFT:
                Link.move_diretion = 'walk_left'

            elif event.key == K_RIGHT:
                Link.move_diretion = 'walk_right'

        elif event.type == KEYUP:
            if Link.move_diretion == 'walk_bottom' and event.key == K_DOWN:
                Link.move_diretion = 'stay_bottom'

            elif Link.move_diretion == 'walk_top' and event.key == K_UP:
                Link.move_diretion = 'stay_top'

            elif Link.move_diretion == 'walk_left' and event.key == K_LEFT:
                Link.move_diretion = 'stay_left'

            elif Link.move_diretion == 'walk_right' and event.key == K_RIGHT:
                Link.move_diretion = 'stay_right'

    screen.fill((0,0,0))

#===============================================================
                      # Show Player Borders
    # pygame.draw.rect(screen,(255,0,0),(Link.rect.left,Link.rect.top,48,48),1)
#===============================================================

    Player_group.draw(screen)
    Player_group.update()

    pygame.display.update()

    Clock.tick(10)
#===============================================================