from trivia import Game


class TriviaTest: # a few tests for specific methods in trivia.py

    def test_trivia(self):
        game = Game()
        game.add('Chet')
        assert len(game.players) == 2
    
    def gameIsPlayable(self):
        game = Game()
        game.add('Pat')
        game.add('Sue')
        assert self.is_playable() == True

    def gameIsNotPlayable(self):
        game = Game()
        game.add('Pat')
        assert self.is_playable() == False
    
    def testCreateQ(self):
        game = Game()
        q = game.create_rock_question("Rock?")
        assert q == "Rock Question"

    