from trivia import Game


class TriviaTest:

    def test_trivia(self):
        game = Game()
        game.add('Chet')
        assert len(game.players) == 2
