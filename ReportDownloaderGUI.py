from pyautogui import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
from datetime import date

# activate the failsafe just in case.
# move your cursor to the top left of the screen
# to deactivate the program
FAILSAFE = True
PAUSE = 2.5


class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.reportEmailDict = {}
        self.screenshotPath = ""
        self.stringVarsA = []
        self.stringVarsB = []
        self.lineCount = 0
        self.pack()
        self.createWidgets()

# create the widgets
    def createWidgets(self):
        # add frames
        self.masterFrame = Frame(self)
        self.frame1 = Frame(self.masterFrame)
        self.frame5 = Frame(self.masterFrame)
        self.frame2 = Frame(self.masterFrame)
        self.frame4 = Frame(self.masterFrame)
        self.frame3 = Frame(self.masterFrame)


# create menubutton for File, Help, About
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar,
                             tearoff=0)
        self.filemenu.add_command(label="Save Profile",
                                  command=self.saveProfile)
        self.filemenu.add_command(label="Load Profile",
                                  command=self.loadProfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",
                                  command=root.destroy)
        self.menubar.add_cascade(label="File",
                                 menu=self.filemenu)
        self.menubar.add_command(label="About",
                                 command=self.about)
        self.menubar.add_command(label="Help",
                                 command=self.help)
        root.config(menu=self.menubar)

# add label
        self.screenshotLabel = Label(self.frame1,
                                     text="Path to screenshots: ")

# add checkbutton for including date on filenames
        self.checkVar = IntVar()
        self.checkButton = Checkbutton(self.frame2,
                                  text="Include date on filename(s)?",
                                  variable=self.checkVar)

# add screenshot path entry widget
        self.screenshotEntryVar = StringVar()
        self.screenshotEntry = Entry(self.frame1,
                                     textvariable=self.screenshotEntryVar)
        self.screenshotEntryVar.set("C:\\docs\\pics\\")

# text widget to display live updates
        self.liveText = Text(self.frame5,
                             wrap=WORD,
                             width=40,
                             height=20)
        self.liveText.insert(END,
                             "This is where you'll see the live activity feed from the program.\n")

# create scrollbars for text widget and attach
        self.scrollY = Scrollbar(self.frame5)
        self.liveText.config(yscrollcommand=self.scrollY.set)
        self.scrollY.config(command=self.liveText.yview)

# add buttons
        # add button to create attachment lines
        self.addReportButton = Button(self.frame2,
                                      text="Add Report",
                                      command=self.addReportLine)
        # delete button to delete lines
        self.deleteReportButton = Button(self.frame2,
                                         text="Delete Report",
                                         command=self.deleteReportLine)
        # create button to run the search and download on what is in the entry fields
        self.runButton = Button(self.frame2,
                                text="Run",
                                command=self.findAndSaveAttachment)

# frame each widget in the grid
        self.masterFrame.grid(row=0, column=0)
        self.frame1.grid(row=0, column=0)
        self.frame5.grid(row=1, column=0)
        self.frame2.grid(row=2, column=0)
        self.frame4.grid(row=2, column=1)
        self.frame3.grid(row=3, column=0)

        self.screenshotLabel.grid(row=0, column=0)
        self.checkButton.grid(row=0, column=0)

        self.screenshotEntry.grid(row=0, column=1)

        self.liveText.grid(row=0, column=0)
        self.scrollY.grid(row=0, column=1, sticky=N+S)

        self.addReportButton.grid(row=0, column=1)
        self.deleteReportButton.grid(row=0, column=2)
        self.runButton.grid(row=0, column=3)

# add new line to window to search and dl another file
    def addReportLine(self):
        # increase our count of the number of lines on the GUI
        self.lineCount += 1

        # update live feed
        self.liveText.insert(END, "New report line added.\n")

        # create frame to house the newly added widgets
        self.newReportFrame = Frame(self.frame3)

        # create label to indicate what entry widget is used for
        self.label1 = Label(self.newReportFrame,
                            text="Email subject screenshot: ")

        # create entry widget to take user input for filename and extension
        self.entry1Var = StringVar()
        self.entry1 = Entry(self.newReportFrame,
                            textvariable=self.entry1Var)
        self.entry1Var.set("Enter screenshot filename and extension here")
        # save dynamically generated stringvar to a list
        self.stringVarsA.insert(self.lineCount, self.entry1Var)

        # create entry widget to take user input for full save path and new file name
        self.label2 = Label(self.newReportFrame,
                            text="Report save path: ")

        # create entry widget to take save path and new file name
        self.entry2Var = StringVar()
        self.entry2 = Entry(self.newReportFrame,
                            textvariable=self.entry2Var)
        self.entry2Var.set("Enter full save path and new file name")
        # save dynamically generated stringvar to a list
        self.stringVarsB.insert(self.lineCount, self.entry2Var)

        # arrange each widget in the grid
        self.newReportFrame.grid(row=self.lineCount, column=0)

        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)

        self.label2.grid(row=0, column=2)
        self.entry2.grid(row=0, column=3)

# delete the last row in the widget
    def deleteReportLine(self):
        # the line count should never be < 0
        if self.lineCount <= 0:
            self.lineCount = 0
            # update live feed
            self.liveText.insert(END, "Nothing to delete!\n")
        else:
            # remove corresponding stringvars from each list to avoid memory leak
            self.stringVarsA.remove(self.stringVarsA[self.lineCount - 1])
            self.stringVarsB.remove(self.stringVarsB[self.lineCount - 1])
            # if there is a frame whose row equals the line count, then delete it
            for child in self.frame3.grid_slaves():
                if int(child.grid_info()["row"]) == self.lineCount:
                    child.destroy()
            # update the line count
            self.lineCount -= 1
            # update live feed
            self.liveText.insert(END, "Report line deleted.\n")

# build dictionary containing screenshots images and corresponding file paths
    def createDictionary(self):
        # create temp lists to store the values of stringvars in each list
        listA = []
        listB = []
        # first, get each value of the item from the stringvar lists
        for a in self.stringVarsA:
            listA.append(a.get())
        for b in self.stringVarsB:
            listB.append(b.get())
        # then, zip each key-value pair in a dict method and return it
        self.reportEmailDict = dict(zip(listA, listB))
        return self.reportEmailDict

# save all settings, filenames, file paths, etc to a text file
    def saveProfile(self):
        return None

# load all settings, filenames, file paths, etc from a text file
    def loadProfile(self):
        return None

# find and save email attachment using key-value pair
    def findAndSaveAttachment(self):
        self.createDictionary()
        for k, v in self.reportEmailDict.items():
            print(k, v)
        return None

# change filename of attachment before saving using key-value pair
    def changeFileName(self, k, v):
        return None

# create 2 messageboxes for about/help
    def about(self):
        messagebox.showinfo("About",
                            "Written by: Chad Bartel\n" +
                            "Using Python ver " + sys.version)

    def help(self):
        messagebox.showinfo("Help",
                            "Gonna add something here.")

# run the application
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from email")
    root.mainloop()
