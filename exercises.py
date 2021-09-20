import random

from kana import Kana, Symbol


class Exercise:

    def run(self):
        pass

    def symbolsContainSyllabary(self, syllabary: str, symbols: [Symbol]) -> bool:
        for symbol in symbols:
            if syllabary == symbol.syllabary:
                return True

        return False


class VowelGroupQuiz(Exercise):

    def __init__(self, kana: Kana):
        self.kana = kana

    def run(self):
        super(VowelGroupQuiz, self).run()

        print('=====================Vowel Group QUIZ======================')
        print(f'Write all syllabary in the upcomming vowel groups {self.kana.getName()}')

        vowels = self.kana.getVowels()
        vowels = random.sample(vowels, len(vowels))

        for vowel in vowels:
            print('')
            symbols = self.kana.getSymbolsForVowel(vowel)
            found = set()

            ljustSize = self.kana.getMaxSyllabaryLength()

            def buildFoundList():
                foundSymbols = ' '.join(
                    [symbol.syllabary.ljust(ljustSize) if symbol.syllabary in found else ''.ljust(ljustSize) for symbol
                     in symbols])
                return f'[{foundSymbols}]'

            while len(found) < len(symbols):
                promt = f'{buildFoundList()} {vowel.value} >'
                answer = input(promt).lower()

                if self.symbolsContainSyllabary(answer, symbols):
                    found.add(answer)

            print(f'\n{buildFoundList()}')
            print('Great you finished that group')


class ConsonantGroupQuiz(Exercise):

    def __init__(self, kana: Kana):
        self.kana = kana

    def run(self):
        super(ConsonantGroupQuiz, self).run()

        print('====================Consonant Group QUIZ===================')
        print(f'Write all syllabary in the upcomming consonant groups {self.kana.getName()}')

        consonants = self.kana.getConsonants()
        consonants = random.sample(consonants, len(consonants))

        for consonant in consonants:
            print('')
            symbols = self.kana.getSymbolsForConsonant(consonant)
            found = set()

            while len(found) < len(symbols):
                answer = input(f'[{len(found)}|{len(symbols)}] {consonant.value} >').lower()

                if self.symbolsContainSyllabary(answer, symbols):
                    found.add(answer)

            print('Great you finished that group')


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