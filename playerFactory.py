from player import Player
import typing

class PlayerFactory:
    players: typing.Dict[int, Player] = {}
    def newPlayer(self) -> Player:
        player = Player(len(self.players)+1)
        self.players[player.playerId] = player
        return player
