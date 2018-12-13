# -*- coding: utf-8 -*-
# author: BAO Yukun
# python version: Python 3.6.5

import re


class TextGeneratorFromFile():
    '''
    generate text from file
    numWords: number of words at each time
    '''

    def __init__(self, path, numWords):
        self.path = path
        self.pos = 0
        self.numWords = numWords
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = re.findall(r'\w+', f.read())

    def getText(self):
        if self.pos + self.numWords >= len(self.text):
            self.pos = 0
        text = " ".join(self.text[self.pos: self.pos+self.numWords])
        self.pos += self.numWords
        return text
