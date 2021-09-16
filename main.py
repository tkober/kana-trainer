import random

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
                exercises.append(VowelGroupQuiz(self.kana))

            if self.consonantGroupQuiz:
                exercises.append(ConsonantGroupQuiz(self.kana))

            if self.symbolQuiz:
                exercises.append(SymbolQuiz(self.kana))

            random.shuffle(exercises)
            for exercise in exercises:
                exercise.run()

            keepGoing = self.infiniteLoop


if __name__ == '__main__':

    app = App(
        kana=Hiragana(),
        infiniteLoop=True,
        vowelGroupQuiz=True,
        consonantGroupQuiz=True,
        symbolQuiz=True
    )
    app.run()