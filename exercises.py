import random

from kana import Kana


class Exercise:

    def run(self):
        pass


class VowelGroupQuiz(Exercise):

    def __init__(self, kana: Kana):
        self.kana = kana

    def run(self):
        super(VowelGroupQuiz, self).run()
        print('TODO: VowelGroupQuiz')


class ConsonantGroupQuiz(Exercise):

    def __init__(self, kana: Kana):
        self.kana = kana

    def run(self):
        super(ConsonantGroupQuiz, self).run()
        print('TODO: ConsonantGroupQuiz')


class SymbolQuiz(Exercise):

    def __init__(self, kana: Kana, sampleSize=20):
        self.kana = kana
        self.sampleSize = sampleSize

    def run(self):
        super(SymbolQuiz, self).run()
        symbols = random.sample(self.kana.getAllSymbols(), self.sampleSize)

        print('========================SYMBOL QUIZ========================')
        print(f'Write the syllabary for the following {self.kana.getName()}')

        for i in range(self.sampleSize):
            symbol = symbols[i]

            answer = ''
            while answer.lower() != symbol.syllabary:
                answer = input(f'[{i + 1}|{self.sampleSize}]: {symbol.symbol} >')