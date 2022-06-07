from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout,QVBoxLayout, QPlainTextEdit, QLabel
import sys
from PyQt5.QtCore import Qt 
from BlurWindow.blurWindow import blur
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
from PyQt5 import QtGui

#source ../env/Scripts/activate
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.title = "MarkDown Editor"
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1500, 900)
        hWnd = self.winId()
        blur(hWnd)

        # hbox = QHBoxLayout()
        # self.inputeditor = QPlainTextEdit(self)
        # # self.inputeditor.setFrameShape(QPlainTextEdit.StyledPanel)
        # hbox.addWidget(self.inputeditor)
        # self.outputbox = QLabel(self)
        # self.outputbox.setFrameShape(QFrame.StyledPanel)
        # hbox.addWidget(self.outputbox)
        # # self.inputeditor.bind("<<Modified>>", self.onInputChange)
        # self.setLayout(hbox)
        # self.show()

        self.setLayout(QVBoxLayout())
        self.h_layout = QHBoxLayout()
        self.layout().addLayout(self.h_layout)

        self.inputeditor = QPlainTextEdit(self)
        self.inputeditor.resize(750,500)

        self.inputStyle = """ color: white;background: rgba(0,0,255,20%);"""    
        self.setElemFont(self.inputeditor)
        self.setElemStyle(self.inputeditor, self.inputStyle)
        
        self.setWindowStyle()
                        

    def setElemFont(self, elem):
        font = QtGui.QFont('Arial', 10)
        elem.setFont(font)

    def setElemTextColor(self, elem, clr):
        elem.setStyleSheet("color: "+ clr)
        
    def setElemStyle(self, elem, sh):
        elem.setStyleSheet(sh)


    def setWindowStyle(self):
        self.setStyleSheet(
            """
            *{
                border-radius:1px;
            }
            """ 
        )

    def setElemOpacity(self,elem, val):
        elem.setStyleSheet("background: rgba(0,0,255,"+ str(val) +"%)")

    def onInputChange(self , event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0" , END)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())