import os
import random
from subprocess import call
from time import sleep

from kana import Kana, Symbol


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

    def run(self):
        super(VowelGroupQuiz, self).run()

        print('=====================Vowel Group QUIZ======================')
        print(f'Write all syllabary in the upcomming vowel groups of {self.kana.getName()}')

        vowels = self.kana.getVowels()
        vowels = random.sample(vowels, len(vowels))

        for vowel in vowels:
            print('')
            symbols = self.kana.getSymbolsForVowel(vowel)
            found = set()

            while len(found) < len(symbols):
                syllabariesList, symbolslist = self.buildFoundList(symbols, found)
                promt = f'{symbolslist}\n{syllabariesList} {vowel.value} >'
                answer = input(promt).lower()

                self.clearConsole()
                if self.symbolsContainSyllabary(answer, symbols):
                    found.add(answer)

            syllabariesList, symbolslist = self.buildFoundList(symbols, found)
            print(f'\n{symbolslist}\n{syllabariesList}')
            print('Great you finished that group')

            super(VowelGroupQuiz, self).run()


class ConsonantGroupQuiz(CompletionExercise):

    def run(self):
        super(ConsonantGroupQuiz, self).run()

        print('====================Consonant Group QUIZ===================')
        print(f'Write all syllabary in the upcomming consonant groups of {self.kana.getName()}')

        consonants = self.kana.getConsonants()
        consonants = random.sample(consonants, len(consonants))

        for consonant in consonants:
            print('')
            symbols = self.kana.getSymbolsForConsonant(consonant)
            found = set()

            while len(found) < len(symbols):
                syllabariesList, symbolslist = self.buildFoundList(symbols, found)
                promt = f'{symbolslist}\n{syllabariesList} {consonant.value} >>'
                answer = input(promt).lower()

                if self.symbolsContainSyllabary(answer, symbols):
                    found.add(answer)

            syllabariesList, symbolslist = self.buildFoundList(symbols, found)
            print(f'\n{symbolslist}\n{syllabariesList}')
            print('Great you finished that group')

            super(ConsonantGroupQuiz, self).run()


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
