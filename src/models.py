from random import randint
from .exceptions import EnemyDown


class Enemy(object):
    '''Class enemy ...'''

    def __init__(self, level):  #Done
        self.level = level
        self.lives = level

    def select_attack(self):    #Done
        return randint(1, 3)

    def decrease_lives(self):
        if self.lives == 0:
            raise EnemyDown
        else:
            self.lives -= 1
            return 1


class Player(object):
    '''Class player ...'''

    score = 0
    allowed_attacks = None

    def __init__(self, name):
        self.name = name
        self.lives = None

    def _fight(attack, defense):
        return 0, -1, 1

    def decrease_lives(self):
        if self.lives == 0:
            raise EnemyDown
        else:
            self.lives -= 1
            return 1

    def attack(self, enemy_obj):
        # дописать
        result_fight = self._fight()
        if result_fight == 0:
            return "It's a draw!"
        elif result_fight == 1:
            enemy_obj.decrease_lives()
            return "You attacked successfully!"
        elif result_fight == -1:
            return "You missed!"

    def defence(self, enemy_obj):
        # дописать
        result_fight = self._fight()
        if result_fight == 0:
            return "It's a draw!"
        elif result_fight == 1:
            enemy_obj.decrease_lives()
            return "You attacked successfully!"
        elif result_fight == -1:
            return "You missed!"
