

class GameOver(Exception):
    '''This is exception ...'''
    def save(self, score):
        with open('../score.txt', 'a') as file_score:
            file_score.write(score)


class EnemyDown(Exception):
    def best_ten_gamer(self):
        pass