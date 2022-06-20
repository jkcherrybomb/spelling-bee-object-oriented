import tkinter
from player import Player
from comms import Comm

class Window:
    player: Player
    def __init__(self, player: Player):
        self.window = tkinter.Tk()
        self.window.title("Spelling Bee")
        self.window.columnconfigure(1, weight=5)
        self.player = player
        
        tkinter.Button(self.window, text = "Give me a new set of letters", fg = "purple", command = lambda: self.randLetters()).grid(row = 2, column = 4)

        tkinter.Label(self.window, text = "enter your word").grid(row = 1, column = 0)
        self.inputWord = tkinter.Entry(self.window)
        self.inputWord.grid(row = 1, column = 1)

        tkinter.Button(self.window, text = "submit", fg = "purple", command = lambda: self.check()).grid(row = 2, column = 5)

        self.window.mainloop()

    def check(self) -> None:
        info = self.player.submitWord(self.inputWord.get())
        tkinter.Label(self.window, text = self.textFromComm(info)).grid(row=2, column = 0)
        self.render()
    
    def textFromComm(self, info: Comm) -> str:
        if info == Comm.correctWord: 
            self.printing = tkinter.Label(self.window, text = "Congrats! you're right!             ").grid(row = 2, column = 0)
        if info == Comm.invalidLetter:
            self.printing = tkinter.Label(self.window, text = "You've used a letter outside the set").grid(row = 2, column = 0)
        if info == Comm.usedWord:
            self.printing = tkinter.Label(self.window, text = "You've already used that word       ").grid(row = 2, column = 0)
        if info == Comm.tooShort:
            self.printing = tkinter.Label(self.window, text = "That's too short                    ").grid(row = 2, column = 0)
        if info == Comm.invalidWord:
            self.printing = tkinter.Label(self.window, text = "Sorry! Try again!                   ").grid(row = 2, column = 0)
        if info == Comm.noMain:
            self.printing = tkinter.Label(self.window, text = "You need to use the main letter     ").grid(row = 2, column = 0)
        
        

    def randLetters(self) -> None:
        self.player.resetGame()
        self.render()
    
    def render(self) -> None:
        tkinter.Label(self.window, text = "Your set of letters is:"    ).grid(row = 0, column = 0)
        tkinter.Label(self.window, text = self.player.state.letters    ).grid(row = 0, column = 1)
        tkinter.Label(self.window, text = "Main letter:"               ).grid(row = 0, column = 2)
        tkinter.Label(self.window, text = self.player.state.main_letter).grid(row = 0, column = 3)
        tkinter.Label(self.window, text = "Your score is:"             ).grid(row = 0, column = 4)
        tkinter.Label(self.window, text = self.player.state.score      ).grid(row = 0, column = 5)



"""	
def check():
	word = str(inputword.get())
	if len(word) < 4:
		printing = tkinter.Label(window, text = "that's too short").grid(row = 2, column = 0)
		return 
	for i in word:
		if i not in letters2:
			printing = tkinter.Label(window, text ="You've used a letter outside the set").grid(row = 2, column = 0)
			return 
	if word in dictionary:
		printing = tkinter.Label(window, text = "Congrats! you're right!").grid(row = 2, column = 0)
		global keepscore
		keepscore += len(word)
		displayscore = tkinter.Label(window, text = "Your score is:").grid(row = 0, column = 2)
		currentscore = tkinter.Label(window, text = keepscore).grid(row = 0, column = 3)
	else:
		printing = tkinter.Label(window, text = "Sorry! Try again!").grid(row = 2, column = 0)
	
	

displayreset = tkinter.Button(window, text = "Give me a new set of letters", fg = "purple", command = randletters).grid(row = 2, column = 2)

tkinter.Label(window, text = "enter your word").grid(row = 1, column = 0)
inputword = tkinter.Entry(window)
inputword.grid(row = 1, column = 1)

checkbutton = tkinter.Button(window, text = "submit", fg = "purple", command = check).grid(row = 2, column = 3)

window.mainloop()
"""