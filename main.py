import tkinter
import random

from playerFactory import PlayerFactory
from gameFactory import GameFactory
from frontend import Window


"""
window = tkinter.Tk()
window.title("Spelling Bee")
window.columnconfigure(1, weight=3)
"""

gameFactory = GameFactory()
playerFactory = PlayerFactory()

standardGame = gameFactory.newGame(7)
singlePlayer = playerFactory.newPlayer()

singlePlayer.joinGame(standardGame) 

Window(singlePlayer)