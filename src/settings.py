from enum import Enum


class ConstValue(Enum):
    SHOW_SCORE = ['show score', 'show', 'score']
    ENTER_ERROR = "Incorrect input value. Repeat enter."


class GameValue(object):
    LEVEL = 1
    VALIDATE = 0
    TOP_SCORE = 0

    @classmethod
    def set_level(cls):
        cls.LEVEL += 1

    @classmethod
    def set_validate(cls):
        cls.VALIDATE = 1

    @classmethod
    def set_top_score(cls, score):
        cls.TOP_SCORE = score


class CollectionComands(object):
    __COMANDS = {'start': "To begine the game.",
                 'show scores': "Show the top ten score of the players.",
                 'exit': "Quit the game."}

    @classmethod
    def help(cls):
        for key, string in cls.__COMANDS.items():
            print(f"{key.upper()}: {string}")