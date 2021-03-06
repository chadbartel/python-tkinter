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

        # create frames
        self.buttonFrameFrame = Frame(self)
        self.labelComboFrame = Frame(self.buttonFrameFrame)
        self.listScrollFrame = Frame(self)

        # create labels
        self.rollLabel = Label(self.labelComboFrame,
                               text="Roll ")
        self.dLabel = Label(self.labelComboFrame,
                            text=" d ")

        # create entry widget
        self.numDiceVar = IntVar()
        self.numDiceEntry = Entry(self.labelComboFrame,
                                  width=3,
                                  textvariable=self.numDiceVar)

        self.numDiceEntry.delete(0, END)
        self.numDiceEntry.insert(0, 1)

        # create combo box and link variable
        self.dieSizeVar = IntVar()
        self.dieSizeCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=3,
                                         textvariable=self.dieSizeVar)
        self.dieSizeCombo["values"] = (4, 6, 8, 10, 12, 20, 100)
        self.dieSizeCombo.current(5)

        # create one button to roll the dice
        self.rollButton = Button(self.buttonFrameFrame,
                                 text="Roll!",
                                 command=self.diceRolls)

        # Create a quit button that closes the window
        self.QUIT = Button(self.buttonFrameFrame, text="Quit", command=root.destroy)

        # Create listbox for each roll
        self.resultsList = Listbox(self.listScrollFrame)

        # Create total value to use for summing values if checkbox true
        self.resultSum = int

        # Create scrollbar widget for new text field
        self.scrollbarY = Scrollbar(self.listScrollFrame)
        self.scrollbarX = Scrollbar(self.listScrollFrame, orient=HORIZONTAL)

        # Attach listbox to scrollbar
        self.resultsList.config(yscrollcommand=self.scrollbarY.set,
                                xscrollcommand=self.scrollbarX.set)
        self.scrollbarY.config(command=self.resultsList.yview)
        self.scrollbarX.config(command=self.resultsList.xview)


        # Create checkbox if the user wants to see the total
        self.checkValue = IntVar()
        self.totalCheck = Checkbutton(self.buttonFrameFrame,
                                      variable=self.checkValue,
                                      text="Display total?",
                                      command=self.appendSum)

        # arrange each widget in the window
        self.rollLabel.pack(side="left")
        self.numDiceEntry.pack(side="left")
        self.dLabel.pack(side="left")
        self.dieSizeCombo.pack(side="left")
        self.labelComboFrame.pack(side="top")
        self.totalCheck.pack(fill="both", padx=3, pady=3)
        self.rollButton.pack(fill="both", padx=3, pady=3)
        self.QUIT.pack(fill="both", padx=3, pady=3)
        self.buttonFrameFrame.pack(side="left")
        self.listScrollFrame.pack(side="left")
        self.resultsList.grid(row=0, column=0)
        self.scrollbarY.grid(row=0, column=1, sticky=N+S)
        self.scrollbarX.grid(row=1, column=0, sticky=W+E)

    # create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self):
        try:
            # clear previous value from sum value
            self.resultSum = 0
            # clear previous values from rollList
            self.resultsList.delete(0, END)
            # roll 'diceNum' dice of size 'dieSize'
            dieSize = int(self.dieSizeCombo.get())
            diceNum = int(self.numDiceEntry.get())
            for i in range(diceNum):
                self.resultsList.insert(END, self.rollDie(dieSize))
            self.sumResultsList(self.resultsList)
        except (TypeError, ValueError) as e:
            self.resultsList.insert(END, str(e))

    def sumResultsList(self, rl):
        for i in range(rl.size()):
            self.resultSum += int(rl.get(i))
        if self.checkValue.get():
            self.resultsList.insert(END, "Total = " + str(self.resultSum))
        return self.resultSum

    def appendSum(self):
        if self.checkValue.get():
            if self.resultsList.get(END) == "Total = " + str(self.resultSum):
                pass
            else:
                self.resultsList.insert(END, "Total = " + str(self.resultSum))
        elif not self.checkValue.get():
            if self.resultsList.get(END) == "Total = " + str(self.resultSum):
                self.resultsList.delete(END)

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Roll the dice!")
    root.mainloop()
