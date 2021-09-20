from dataclasses import dataclass
from enum import Enum


class Vowel(Enum):
    A = 'a'
    I = 'i'
    U = 'u'
    E = 'e'
    O = 'o'


class Consonant(Enum):
    NONE = 'NONE'
    K = 'k'
    S = 's'
    T = 't'
    N = 'n'
    H = 'h'
    M = 'm'
    Y = 'y'
    R = 'r'
    W = 'w'
    DOT = '•'


@dataclass(frozen=True)
class Symbol:
    symbol: chr(1)
    syllabary: str
    consonant: Consonant
    vowel: Vowel


class Kana:

    def __init__(self, name: str):
        self.__name = name
        self.__symbols = []
        self.__consonantMap = {consonant: [] for consonant in Consonant}
        self.__vowelMap = {vowel: [] for vowel in Vowel}

    def addSymbol(self, symbol: Symbol):
        self._assertSymbolNotInList(symbol, self.__consonantMap[symbol.consonant])
        self._assertSymbolNotInList(symbol, self.__vowelMap[symbol.vowel])

        self.__symbols.append(symbol)
        self.__consonantMap.get(symbol.consonant).append(symbol)
        self.__vowelMap.get(symbol.vowel).append(symbol)

    def _assertSymbolNotInList(self, symbol: Symbol, list: [Symbol]):
        item: Symbol
        for item in list:
            if item.consonant == symbol.consonant and item.vowel == symbol.vowel:
                raise ValueError(f'Symbol {symbol} already defined in Kana.')

    def getAllSymbols(self) -> [Symbol]:
        return self.__symbols

    def getSymbolsForConsonant(self, consonant: Consonant) -> [Symbol]:
        return self.__consonantMap.get(consonant)

    def getSymbolsForVowel(self, vowel: Vowel) -> [Symbol]:
        return self.__vowelMap.get(vowel)

    def getName(self) -> str:
        return self.__name

    def getConsonants(self) -> [Consonant]:
        return self.__consonantMap.keys()

    def getVowels(self) -> [Vowel]:
        return self.__vowelMap.keys()

    def __repr__(self):
        symbols = ',\n\t'.join([symbol.__repr__() for symbol in self.__symbols])
        return f'{self.__name} [\n\t{symbols}\n]'

    def print(self):
        headers = '\t' + '\t\t'.join([consonant.value for consonant in Consonant])
        print(headers)

        for vowel in Vowel:
            print()
            symbolMap = {consonant: '' for consonant in Consonant}
            syllabaryMap = {consonant: '' for consonant in Consonant}
            for symbol in self.__vowelMap.get(vowel):
                symbolMap[symbol.consonant] = symbol.symbol
                syllabaryMap[symbol.consonant] = symbol.syllabary

            symbolRow = vowel.value + '\t' + '\t\t'.join(
                [symbolMap[consonant] for consonant in Consonant])
            print(symbolRow)

            syllabaryRow = '\t' + '\t\t'.join(
                [syllabaryMap[consonant] for consonant in Consonant])
            print(syllabaryRow)


class Hiragana(Kana):

    def __init__(self):
        super().__init__('Hiragana')

        # None
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.NONE, symbol='あ', syllabary='a'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.NONE, symbol='い', syllabary='i'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.NONE, symbol='う', syllabary='u'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.NONE, symbol='え', syllabary='e'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.NONE, symbol='お', syllabary='o'))

        # K
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.K, symbol='か', syllabary='ka'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.K, symbol='き', syllabary='ki'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.K, symbol='く', syllabary='ku'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.K, symbol='け', syllabary='ke'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.K, symbol='こ', syllabary='ko'))

        # S
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.S, symbol='さ', syllabary='sa'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.S, symbol='し', syllabary='shi'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.S, symbol='す', syllabary='su'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.S, symbol='せ', syllabary='se'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.S, symbol='そ', syllabary='so'))

        # T
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.T, symbol='た', syllabary='ta'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.T, symbol='ち', syllabary='chi'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.T, symbol='つ', syllabary='tsu'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.T, symbol='て', syllabary='te'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.T, symbol='と', syllabary='to'))

        # N
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.N, symbol='な', syllabary='na'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.N, symbol='に', syllabary='ni'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.N, symbol='ぬ', syllabary='nu'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.N, symbol='ね', syllabary='ne'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.N, symbol='の', syllabary='no'))

        # H
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.H, symbol='は', syllabary='ha'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.H, symbol='ひ', syllabary='hi'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.H, symbol='ふ', syllabary='hu'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.H, symbol='へ', syllabary='he'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.H, symbol='ほ', syllabary='ho'))

        # M
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.M, symbol='ま', syllabary='ma'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.M, symbol='み', syllabary='mi'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.M, symbol='む', syllabary='mu'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.M, symbol='め', syllabary='me'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.M, symbol='も', syllabary='mo'))

        # Y
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.Y, symbol='や', syllabary='ya'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.Y, symbol='ゆ', syllabary='yu'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.Y, symbol='よ', syllabary='yo'))

        # R
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.R, symbol='ら', syllabary='ra'))
        self.addSymbol(Symbol(vowel=Vowel.I, consonant=Consonant.R, symbol='り', syllabary='ri'))
        self.addSymbol(Symbol(vowel=Vowel.U, consonant=Consonant.R, symbol='る', syllabary='ru'))
        self.addSymbol(Symbol(vowel=Vowel.E, consonant=Consonant.R, symbol='れ', syllabary='re'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.R, symbol='ろ', syllabary='ro'))

        # W
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.W, symbol='わ', syllabary='wa'))
        self.addSymbol(Symbol(vowel=Vowel.O, consonant=Consonant.W, symbol='を', syllabary='wo'))

        # DOT
        self.addSymbol(Symbol(vowel=Vowel.A, consonant=Consonant.DOT, symbol='ん', syllabary='n/m'))
