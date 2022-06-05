from tkinter import *
from tkinter import font , filedialog
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
from tkinter import messagebox as mbox
from ctypes import windll
from BlurWindow.blurWindow import blur

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def onInputChange(self , event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0" , END)))

    def openfile(self):
        openfilename = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"),
                                                                    ("Text File", "*.txt"), 
                                                                    ("All Files", "*.*")))
        if openfilename:
            try:
                self.inputeditor.delete(1.0, END)
                self.inputeditor.insert(END , open(openfilename).read())
            except:
                print("Cannot Open File!")

    def savefile(self):
        filedata = self.inputeditor.get("1.0" , END)
        savefilename = filedialog.asksaveasfilename(filetypes = (("Markdown File", "*.md"),
                                                                  ("Text File", "*.txt")) , title="Save Markdown File")
        if savefilename:
            try:
                f = open(savefilename , "w")
                f.write(filedata)
            except:
                mbox.showerror("Error Saving File" , "Oops!, The File : {} can not be saved!".format(savefilename))

    def init_window(self):
        self.master.title("MarkDown Editor")
        self.pack(fill=BOTH, expand=1)

        self.inputeditor = Text(self, width="1")
        self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
        self.inputeditor.configure(font=("Arial", 11))

        self.outputbox = HTMLLabel(self, width="1", background="white")
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        self.outputbox.fit_height()
        self.inputeditor.bind("<<Modified>>", self.onInputChange)

        self.mainmenu = Menu(self)
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save as", command=self.savefile)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.mainmenu)
        self.master.wm_attributes("-alpha", 0.7)

root = Tk()
root.geometry("1500x900")
app = Window(root)
app.mainloop()