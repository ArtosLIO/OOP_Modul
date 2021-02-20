import configparser
from src.settings import GameValue


class GameOver(Exception):
    '''This is exception game over ...'''

    @staticmethod
    def __init__(name, score):
        conf = configparser.RawConfigParser()
        conf.read("score.txt")
        if GameValue.VALIDATE:
            score_player = int(conf["ScorePlayers"][name])
            if score > score_player:
                conf.set("ScorePlayers", name, score)
                with open('score.txt', 'w') as file_score:
                    conf.write(file_score)
        else:
            conf.set("ScorePlayers", name, score)
            with open('score.txt', 'w') as file_score:
                conf.write(file_score)


class EnemyDown(Exception):
    '''Your enemy down'''
    pass


class GameExit(Exception):
    '''Quick program'''
    pass