import typing 

class Dictionary:
    words: typing.Set[str] = {}

    def __init__(self) -> None:
        self.load_words()

    def load_words(self) -> None:
        dfile = open('dictionary.txt')
        dictionary = dfile.readlines()
        dfile.close()
        for i in range(len(dictionary)):
            dictionary[i] = dictionary[i][:-1]
        self.words = set(dictionary)

    def check_word(self, word: str) -> bool:
        return word in self.words