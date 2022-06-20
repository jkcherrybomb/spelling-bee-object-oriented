from enum import Enum

class Comm(Enum):
    correctWord = 0
    invalidLetter = 1
    usedWord = 2
    tooShort = 3
    invalidWord = 4
    noMain = 5