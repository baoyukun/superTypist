# -*- coding: utf-8 -*-
# author: BAO Yukun
# python version: Python 3.6.5

import pygame


class Caption(pygame.sprite.Sprite):
    '''
    realtime display of typing performance
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = "Speed: %.1f/min, correct words: %s/%s" % (0, 0, 0)
        self.update()

    def update(self):
        self.image = pygame.font.Font(None, 26).render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

    def setText(self, speed, words, corrWords):
        self.text = "Speed: %.1f/min, correct words: %s/%s" % (
            speed, corrWords, words)
