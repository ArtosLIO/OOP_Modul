from random import randint
import configparser
from src.exceptions import EnemyDown, GameOver


class Enemy(object):    # Done
    '''Class enemy ...'''

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
        return 1    # check decrease lives done


class Player(object):
    '''Class player ...'''

    score = 0
    lives = 3
    allowed_attacks = (1, 2, 3)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif (attack == 1 and defense == 2)\
                or (attack == 2 and defense == 3)\
                or (attack == 3 and defense == 1):
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print("You defeated.")
            raise GameOver(self.name, self.score)
        return 1

    def attack(self, enemy_obj, attack_player):
        defence_enemy = enemy_obj.select_attack()
        result_fight = self.fight(attack_player, defence_enemy)
        if result_fight == 0:
            return "It's a draw!"
        elif result_fight == 1:
            enemy_obj.decrease_lives()
            self.score += 1
            return "You attacked successfully!"
        elif result_fight == -1:
            self.decrease_lives()
            return "You missed!"

    def defence(self, enemy_obj, defence_player):
        attack_enemy = enemy_obj.select_attack()
        result_fight = self.fight(attack_enemy, defence_player)
        if result_fight == 0:
            return "It's a draw!"
        elif result_fight == 1:
            self.decrease_lives()
            return "You missed!"
        elif result_fight == -1:
            enemy_obj.decrease_lives()
            self.score += 1
            return "You defenced successfully!"


class Score(object):
    '''Class Score ...'''

    TopScore = []

    def __init__(self):
        conf = configparser.RawConfigParser()
        conf.read("score.txt")
        list_players = conf.options("ScorePlayers")
        for player in list_players:
            score = conf["ScorePlayers"][player]
            self.TopScore.append([player, int(score)])
        sorted_list = sorted(self.TopScore, key=lambda row: row[1], reverse=True)
        for sl in sorted_list[:3]:
            print("*"*34 + '\n*' + ' '*32 + '*')
            print('*' + ' '*4 + "{: <20}{: >4}".format(sl[0], sl[1]) + ' '*4 + '*')
            print('*' + ' ' * 32 + '*')
        print("*"*34, end='\n\n')
        for sl in sorted_list[3:10]:
            print("\t{:*<20}{: >4}".format(sl[0], sl[1]))