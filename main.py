import random
import argparse

from exercises import VowelGroupQuiz, ConsonantGroupQuiz, SymbolQuiz
from kana import Kana, Hiragana


class App:

    def __init__(
            self,
            kana: Kana,
            infiniteLoop: bool,
            vowelGroupQuiz: bool,
            consonantGroupQuiz: bool,
            symbolQuiz: bool
    ):

        self.kana = kana
        self.infiniteLoop = infiniteLoop
        self.vowelGroupQuiz = vowelGroupQuiz
        self.consonantGroupQuiz = consonantGroupQuiz
        self.symbolQuiz = symbolQuiz

    def run(self):
        keepGoing = True
        while keepGoing:

            exercises = []
            if self.vowelGroupQuiz:
                for vowel in self.kana.getVowels():
                    exercises.append(VowelGroupQuiz(self.kana, vowel))

            if self.consonantGroupQuiz:
                for consonant in self.kana.getConsonants():
                    exercises.append(ConsonantGroupQuiz(self.kana, consonant))

            if self.symbolQuiz:
                exercises.append(SymbolQuiz(self.kana))

            random.shuffle(exercises)
            for exercise in exercises:
                exercise.run()
                print()

            keepGoing = self.infiniteLoop

        print('\nGreat, you have finished your all of your exercises!')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        prog='kana-trainer',
        description='Practice Hiragana & Katakana on your command line when you have some spare minutes.'
    )

    argparser.add_argument(
        '-v',
        '--vowel',
        help="Adds the vowel group quiz to your exercises.",
        action="store_true"
    )

    argparser.add_argument(
        '-c',
        '--consonant',
        help="Adds the consonant group quiz to your exercises.",
        action="store_true"
    )

    argparser.add_argument(
        '-s',
        '--symbol',
        help="Adds the symbol quiz to your exercises.",
        action="store_true"
    )

    argparser.add_argument(
        '-i',
        '--infinite',
        help="Keeps repeating your selected exercises in an infinite loop.",
        action="store_true"
    )

    args = argparser.parse_args()

    hiragana = Hiragana()
    if args.vowel == False and args.consonant == False and args.consonant == False:
        hiragana.print()
        exit(0)

    app = App(
        kana=hiragana,
        infiniteLoop=args.infinite,
        vowelGroupQuiz=args.vowel,
        consonantGroupQuiz=args.consonant,
        symbolQuiz=args.symbol
    )
    app.run()