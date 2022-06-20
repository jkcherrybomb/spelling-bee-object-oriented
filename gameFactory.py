from game import Game
import typing

class GameFactory:
    games: typing.Dict[int, Game] = {}
    def newGame(self, numOfLetters: int) -> Game:
        game = Game(len(self.games)+1, numOfLetters)
        self.games[game.gameId] = game
        return game
