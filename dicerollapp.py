__author__ = 'cbartel'

# import relevant modules - random, tkinter
from random import randint
from tkinter import *
from tkinter import ttk

class Application(Frame):

# initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# create widgets in separate function
    def createWidgets(self):

        # create 3 frames
        self.buttonFrameFrame = Frame(self)
        self.labelComboFrame = Frame(self.buttonFrameFrame)
        self.resultsFrame = Frame(self)

        # create 3 labels
        self.rollLabel = Label(self.labelComboFrame,
                               text="Roll ")
        self.dLabel = Label(self.labelComboFrame,
                            text=" d ")
        self.resultsVar = StringVar()
        self.resultsVar.set("Roll the dice!")
        self.resultsLabel = Label(self.labelComboFrame,
                                  text="See results here!",
                                  width=11,
                                  height=5,
                                  textvariable=self.resultsVar)

        # create 2 combo boxes
        self.numDiceVar = IntVar()
        self.numDiceCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=2,
                                         textvariable=self.numDiceVar)
        self.numDiceCombo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.numDiceCombo.current(0)
        self.dieSizeVar = IntVar()
        self.dieSizeCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=2,
                                         textvariable=self.dieSizeVar)
        self.dieSizeCombo["values"] = (4, 6, 8, 10, 12, 20, 100)
        self.dieSizeCombo.current(5)

        # create one button to roll the dice
        self.rollButton = Button(self.buttonFrameFrame,
                                 text="Roll!",
                                 command=self.diceRolls(self.dieSizeVar.get(),
                                                        self.numDiceVar.get()))

        # arrange each widget in the window
        self.rollLabel.pack(side="left")
        self.numDiceCombo.pack(side="left")
        self.dLabel.pack(side="left")
        self.dieSizeCombo.pack(side="left")
        self.labelComboFrame.pack(side="top")
        self.rollButton.pack(fill="both")
        self.buttonFrameFrame.pack(side="left")
        self.resultsLabel.pack(side="top")
        self.resultsFrame.pack(side="left")

# create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self, dieSize, diceNum):
        # roll 'diceNum' dice of size 'dieSize'
        rollDict = {}
        for i in range(diceNum):
            rollDict[i] = self.rollDie(dieSize)
        self.resultsVar.set(self.dictToString(rollDict) + "\n")
        print(self.resultsVar.get())

    def dictToString(self, dict):
        results = ""
        results.join('Roll {}: {}\n'.format(k, v) for k, v in sorted(dict.items()))
        return results

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    root.mainloop()
