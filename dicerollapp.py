__author__ = 'cbartel'

# import relevant modules - random, tkinter
from random import randint
from tkinter import *
from tkinter import ttk

# initialize app
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# create widgets in separate function
    def createWidgets(self):

        # create frame to house label and combobox
        self.labelComboFrame = Frame(self)

        # create 3 labels
        self.rollLabel = Label(self.labelComboFrame,
                               text="Roll ")
        self.dLabel = Label(self.labelComboFrame,
                            text=" d ")
        self.resultsVar = StringVar()
        self.resultsLabel = Label(self,
                                  text="See results here!",
                                  textvariable=self.resultsVar)

        # create 2 combo boxes
        self.numDiceVar = IntVar()
        self.numDiceVar.set(0)
        self.numDiceCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=2,
                                         textvariable=self.numDiceVar)
        self.numDiceCombo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.numDiceCombo.current(0)
        self.dieSizeVar = IntVar()
        self.dieSizeVar.set(0)
        self.dieSizeCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=2,
                                         textvariable=self.dieSizeVar)
        self.dieSizeCombo["values"] = (4, 6, 8, 10, 12, 20, 100)
        self.dieSizeCombo.current(5)

        # create one button to roll the dice
        self.rollButton = Button(self,
                                 text="Roll!",
                                 command=self.diceRolls(self.dieSizeVar,
                                                        self.numDiceVar))

        # TODO: arrange each widget in the window
        self.rollLabel.pack(side="left")
        self.numDiceCombo.pack(side="left")
        self.dLabel.pack(side="left")
        self.dieSizeCombo.pack(side="left")
        self.labelComboFrame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.rollButton.grid(row=2, column=1, columnspan=2, pady=5)
        self.resultsLabel.grid(row=0, column=4, rowspan=3)

# create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self, dieSize, diceNum):
        # roll 'diceNum' dice of size 'dieSize'
        rollDict = {}
        rollTotal = 0
        for i in range(diceNum):
            rollDict[i] = self.rollDie(dieSize)
            rollTotal += rollDict[i]
        self.resultsVar.set(self.dictToString(rollDict) + "\nTotal = " + rollTotal)

    def dictToString(self, dict):
        results = ""
        results.join('Roll {}: {}\n'.format(k, v) for k, v in sorted(dict.items()))
        return results

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
