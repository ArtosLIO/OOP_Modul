from os import system
import configparser
from src.exceptions import GameOver, EnemyDown, GameExit
from src.models import Player, Enemy, Score
from src.settings import CollectionComands, ConstValue, GameValue


def try_game_function(eggs):
    def wrapper():
        try:
            eggs()
        except KeyboardInterrupt:
            pass
        except GameExit:
            pass
        finally:
            print("\nGood bye!")
    return wrapper


def check_value(val):
    try:
        if 0 < int(val) < 4:
            return 0
        else:
            return 1
    except:
        return 1


def game(name_player):
    player = Player(name_player)
    enemy = Enemy(GameValue.LEVEL)
    while True:
        system('CLS')
        print("\tWelcome to the game {}".format(name_player))
        if GameValue.TOP_SCORE:
            print("Your were top score {}".format(GameValue.TOP_SCORE))
        print(f"Score {player.score}\t\tLives {player.lives}\t\tLevel {GameValue.LEVEL}")

        try:
            while True:
                attack_player = input("""1 - Wizard
2 - Warrior
3 - Robber
Enter value from 1 to 3 for choose a hero to attack: """)
                if check_value(attack_player):
                    print(ConstValue.ENTER_ERROR.value)
                    continue
                result_attack = player.attack(enemy, attack_player)
                print(result_attack, end='\n\n')
                break
            while True:
                defence_player = input("""
Enter value from 1 to 3 for choose a hero to defence: """)
                if check_value(defence_player):
                    print(ConstValue.ENTER_ERROR.value)
                    continue
                result_defence = player.defence(enemy, defence_player)
                print(result_defence)
                break
            input()
        except EnemyDown:
            player.score += 5
            GameValue.set_level()
            input("Enemy defeated. Your level up.")
            enemy = Enemy(GameValue.LEVEL)
            continue
        except GameOver:
            break


def validate_player(name_player):
    conf = configparser.RawConfigParser()
    conf.read("score.txt")
    if conf.has_option("ScorePlayers", name_player):
        GameValue.set_validate()
        score = conf["ScorePlayers"][name_player]
        GameValue.set_top_score(score)


@try_game_function
def play():
    system('CLS')
    while True:
        print("The name must be no more than 20 characters.")
        name_player = input("Enter your name: ").lower()
        system('CLS')
        if not name_player or len(name_player) > 20:
            print(ConstValue.ENTER_ERROR.value)
            continue
        validate_player(name_player)
        break

    while True:
        start = input("Enter your command: ")
        system('CLS')
        if start.lower() == 'start':
            game(name_player)
        elif start.lower() == 'exit':
            raise GameExit
        elif start.lower() in ConstValue.SHOW_SCORE.value:
            Score()
        elif start.lower() == 'help':
            print('\t\tHELP')
            CollectionComands.help()
        else:
            print(ConstValue.ENTER_ERROR.value)
            print("Enter command 'help'")
        input()
        system('CLS')


if __name__ == '__main__':
    play()