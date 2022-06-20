import typing
import random
from dictionary import Dictionary
from comms import Comm

class PlayerGameState:
    score: int = 0
    wordsUsed: typing.Set[str] = set()
    letters: typing.List[str] = []
    main_letter: str = ""

class Game:
    numOfLetters: int = 0
    states: typing.Dict[int, PlayerGameState] = {}

    def __init__(self, gameId: int, numOfLetters: int):
        self.gameId = gameId
        self.numOfLetters = numOfLetters
        self.dictionary = Dictionary()

    
    def addPlayer(self, playerId: int) -> PlayerGameState:
        playerState = PlayerGameState()
        playerState.letters, playerState.main_letter, playerState.score = self.newLetters(playerId)
        self.states[playerId] = playerState
        return playerState

    def resetLetters(self, playerId: int) -> PlayerGameState:
        return self.addPlayer(playerId)

    def validateLetters(self, letters: typing.List[str]) -> bool:
        number_of_possible_words: int = 0
        all_letters_in_word: int = False
        for entry in self.dictionary.words:
            if set(entry).issubset(set(letters)):
                number_of_possible_words += 1
            if set(entry) == set(letters):
                all_letters_in_word = True
                #print(entry)
        if number_of_possible_words < 10:
            return False
        if not all_letters_in_word:
            return False
        return True

    def newLetters(self, playerId: int) -> typing.Tuple[typing.List[str], str, int]:
        while True:
            letters = random.sample(range(97, 121), self.numOfLetters)
            letters = set(map(chr, letters))
            main_letter = random.sample(letters, 1)[0]
            if self.validateLetters(letters):
                #print(main_letter)
                return (list(letters), str(main_letter), 0)
            
    def submitWord(self, playerId: int, word: str) -> typing.Tuple[Comm, PlayerGameState]:
        state = self.states[playerId]
        info = self.validateWord(word, state.letters, state.main_letter, state.wordsUsed)
        if info == Comm.correctWord:
            state.score += len(word)
            if set(word) == set(state.letters):
                state.score += 7
            state.wordsUsed.add(word)
        return (info, state)

    def validateWord(self, word: str, availableLetters: typing.List[str], mainLetter: str, wordsUsed: typing.Set[str]) -> Comm:
        usedAvailableLetters: bool = True
        usedMainLetter: bool = False
        #print(type(mainLetter))
        #print(mainLetter)
        #print(type(word[0]))
        #print(word[0])
        for i in range(len(word)):
            if word[i] not in availableLetters:
                usedAvailableLetters = False
                break
            if word[i] == mainLetter:
                usedMainLetter = True
        if not usedAvailableLetters:
            return Comm.invalidLetter
        if not usedMainLetter:
            return Comm.noMain
        newWord = word not in wordsUsed
        if len(word) < 4: 
            return Comm.tooShort
        if not newWord:
            return Comm.usedWord
        if not self.dictionary.check_word(word):
            return Comm.invalidWord
        return Comm.correctWord 