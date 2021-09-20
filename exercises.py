import os
import random
from subprocess import call
from time import sleep

from kana import Kana, Symbol, Consonant, Vowel


class Exercise:

    def run(self):
        input('[Next Exercise]')
        self.clearConsole()

    def symbolsContainSyllabary(self, syllabary: str, symbols: [Symbol]) -> bool:
        for symbol in symbols:
            if syllabary == symbol.syllabary:
                return True

        return False

    def clearConsole(self):
        _ = call('clear' if os.name == 'posix' else 'cls')
        
    def printQuizTitle(self):
        pass


class CompletionExercise(Exercise):

    def __init__(self, kana: Kana):
        self.kana = kana

    def buildFoundList(self, requiredSymbols, foundSyllabaries):
        syllabaries = '\t'.join(
            [symbol.syllabary if symbol.syllabary in foundSyllabaries else '' for symbol in requiredSymbols])

        symbols = '\t'.join(
            [symbol.symbol if symbol.syllabary in foundSyllabaries else '' for symbol in requiredSymbols])

        return f'{syllabaries}\t|', f'{symbols}'


class VowelGroupQuiz(CompletionExercise):

    def __init__(self, kana: Kana, vowel: Vowel):
        super(VowelGroupQuiz, self).__init__(kana)
        self.__vowel = vowel

    def run(self):
        symbols = self.kana.getSymbolsForVowel(self.__vowel)
        found = set()

        self.clearConsole()
        while len(found) < len(symbols):
            self.printQuizTitle()
            syllabariesList, symbolslist = self.buildFoundList(symbols, found)
            prompt = f'{symbolslist}\n{syllabariesList} {self.__vowel.value} >'
            answer = input(prompt).lower()

            if self.symbolsContainSyllabary(answer, symbols):
                found.add(answer)

            self.clearConsole()

        syllabariesList, symbolslist = self.buildFoundList(symbols, found)
        self.printQuizTitle()
        print(f'{symbolslist}\n{syllabariesList}')
        print('Great you finished that group')

        super(VowelGroupQuiz, self).run()

    def printQuizTitle(self):
        super(VowelGroupQuiz, self).printQuizTitle()
        print('=====================Vowel Group Quiz======================')
        print(f'Write all syllabary in the upcomming vowel groups of {self.kana.getName()}')

        print('')
        


class ConsonantGroupQuiz(CompletionExercise):
    
    def __init__(self, kana: Kana, consonant: Consonant):
        super(ConsonantGroupQuiz, self).__init__(kana)
        self.__consonant = consonant

    def run(self):
        symbols = self.kana.getSymbolsForConsonant(self.__consonant)
        found = set()

        self.clearConsole()
        while len(found) < len(symbols):
            self.printQuizTitle()
            syllabariesList, symbolslist = self.buildFoundList(symbols, found)
            prompt = f'{symbolslist}\n{syllabariesList} {self.__consonant.value} >>'
            answer = input(prompt).lower()

            if self.symbolsContainSyllabary(answer, symbols):
                found.add(answer)

            self.clearConsole()

        syllabariesList, symbolslist = self.buildFoundList(symbols, found)
        self.printQuizTitle()
        print(f'{symbolslist}\n{syllabariesList}')
        print('Great you finished that group')

        super(ConsonantGroupQuiz, self).run()
        
    def printQuizTitle(self):
        super(ConsonantGroupQuiz, self).printQuizTitle()
        print('====================Consonant Group QUIZ===================')
        print(f'Write all syllabary in the upcomming consonant groups of {self.kana.getName()}')

        print('')


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
                answer = input(f'[{i + 1}|{self.sampleSize}]: {symbol.symbol} >>')

        super(SymbolQuiz, self).run()
