from game import Game
from game import PlayerGameState
from comms import Comm
class Player:
    game: Game
    state: PlayerGameState

    def __init__(self, playerId: int):
        self.playerId = playerId
    
    def joinGame(self, game: Game) -> None:
        self.game = game
        self.state = game.addPlayer(self.playerId)
    
    def submitWord(self, word: str) -> Comm:
        info, self.state = self.game.submitWord(self.playerId, word)
        return info

    def resetGame(self):
        self.state = self.game.resetLetters(self.playerId)
