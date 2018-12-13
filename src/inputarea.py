# -*- coding: utf-8 -*-
# author: BAO Yukun
# python version: Python 3.6.5

import pygame
import time
from textgenerator import TextGeneratorFromFile


class InputArea():
    '''
    animation for input area
    '''
    def __init__(self, path):
        self.textGenerator = TextGeneratorFromFile(path, 60)
        self.text = self.textGenerator.getText()
        # logical part
        self.time = time.time()  # start time
        self.words = 0  # Nb of words passed by
        self.speed = 0  # typing speed
        self.flag = True  # record if right for every letter in a word
        self.wordsCorr = 0  # Nb of correct words passed by
        # graphical part
        self.pos = 0  # input pos in text
        self.wordsPage = 0  # Nb of words passed by in single page
        self.vMargin = 10  # vertical margin
        self.hMargin = 10  # horizontal margin
        self.paddingX = 10  # padding at left top corner
        self.paddingY = 50  # padding at left top corner
        # width for whiteSpace
        self.space = pygame.font.Font(None, 36).size(' ')[0]
        # maximum width
        self.surface = pygame.display.get_surface()
        max_width, _ = self.surface.get_size()
        self.max_width = max_width - self.hMargin
        self.update()

    # def update(self):
    #     '''
    #     only available for a single line
    #     '''
    #     self.speed = self.words/(time.time()-self.time+1e-6)*60
    #     self.image = pygame.font.Font(None, 36).render(self.text, 1, (0, 0, 0))
    #     self.highlight = pygame.font.Font(None, 36).render(
    #         self.text[:self.pos], 1, (255, 255, 255))
    #     self.image.blit(self.highlight, (0, 0))
    #     self.rect = self.image.get_rect()
    #     self.rect.center = pygame.display.get_surface().get_rect().center

    def update(self):
        '''
        render multiple lines of words
        '''
        self.speed = self.words/(time.time()-self.time+1e-6)*60

        words = self.text.split(' ')
        global x, y
        x, y = self.paddingX, self.paddingY
        count = 0

        def renderWord(wordText, color, highlight):
            global x, y
            word_surface = pygame.font.Font(
                None, 36).render(wordText, 1, color)
            word_width, word_height = word_surface.get_size()
            word_height += self.vMargin
            if x + word_width >= self.max_width:
                x = self.paddingX
                y += word_height
            if highlight is not None:
                word_surface.blit(highlight, (0, 0))
            self.surface.blit(word_surface, (x, y))
            x += word_width + self.space

        # typed characters
        for i in range(self.wordsPage):
            renderWord(words[i], (255, 255, 255), None)
            count += len(words[i])+1
        
        # words being typed
        highlight = pygame.font.Font(None, 36).render(
            words[self.wordsPage][:self.pos-count], 1, (255, 255, 255))
        renderWord(words[self.wordsPage], (0, 0, 0), highlight)

        # words not been typed
        for i in range(1+self.wordsPage, len(words)):
            renderWord(words[i], (0, 0, 0), None)

    def getSpeed(self):
        return self.speed

    def getWords(self):
        return self.words

    def getCorrWords(self):
        return self.wordsCorr

    def countWords(self):
        self.words += 1
        self.wordsPage += 1
        if self.flag:
            self.wordsCorr += 1
        self.flag = True

    def keyin(self, key):
        if self.text[self.pos] == " ":
            self.countWords()
        elif key != self.text[self.pos]:
            self.flag = False

        self.pos += 1
        if len(self.text) == self.pos:
            self.pos = 0
            self.text = self.textGenerator.getText()
            self.countWords()
            self.wordsPage = 0
