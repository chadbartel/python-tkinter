from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.reportEmailDict = {}
        self.lineCount = 0
        self.stringVarsA = []
        self.stringVarsB = []
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.masterFrame = Frame(self)
        self.frame1 = Frame(self.masterFrame)
        self.frame2 = Frame(self.masterFrame)
        self.frame3 = Frame(self.masterFrame)
        self.frame4 = Frame(self.masterFrame)

        self.addReportButton = Button(self.frame2,
                                      text="Add",
                                      command=self.addLine)
        self.deleteReportButton = Button(self.frame2,
                                         text="Delete",
                                         command=self.deleteLine)
        self.runButton = Button(self.frame4,
                                text="Print",
                                command=self.printStuff)

        self.masterFrame.grid(row=0, column=0)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=2, column=0)
        self.frame3.grid(row=3, column=0)
        self.frame4.grid(row=2, column=1)

        self.addReportButton.grid(row=0, column=0)
        self.deleteReportButton.grid(row=0, column=1)
        self.runButton.grid(row=0, column=2)

    def addLine(self):
        self.lineCount += 1

        self.newReportFrame = Frame(self.frame3)
        self.newReportFrame.pack()

        self.label1 = Label(self.newReportFrame,
                            text="A")
        self.label2 = Label(self.newReportFrame,
                            text="B")
        self.label3 = Label(self.newReportFrame,
                            text=self.lineCount)

        self.entry1Var = StringVar()
        self.entry1 = Entry(self.newReportFrame,
                            textvariable=self.entry1Var)
        self.entry2Var = StringVar()
        self.entry2 = Entry(self.newReportFrame,
                            textvariable=self.entry2Var)

        self.label3.grid(row=0, column=0)
        self.label1.grid(row=0, column=1)
        self.entry1.grid(row=0, column=2)
        self.label2.grid(row=0, column=3)
        self.entry2.grid(row=0, column=4)

        self.stringVarsA.insert(self.lineCount, self.entry1Var)
        self.stringVarsB.insert(self.lineCount, self.entry2Var)

    def reduceCount(self):
        self.lineCount -= 1
        self.stringVarsA.remove(self.stringVarsA[self.lineCount])
        self.stringVarsB.remove(self.stringVarsB[self.lineCount])

    def printStuff(self):
        for i in range(self.lineCount):
            print(self.stringVarsA[i], ", ", self.stringVarsB[i])
            print(self.stringVarsA[i].get(), ", ", self.stringVarsB[i].get())
        print(list(self.stringVarsA))
        print(list(self.stringVarsB))

    def deleteLine(self):
        for child in self.frame3.pack_slaves():
            child.destroy()

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    root.mainloop()