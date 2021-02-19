from .exceptions import GameOver


def try_game_function(eggs):
    def wrapper():
        try:
            eggs()
        except GameOver as go:
            pass
        except KeyboardInterrupt:
            pass
        finally:
            "Good bye!"
    return wrapper

@try_game_function
def play():
    pass


if __name__ == '__main__':
    play()