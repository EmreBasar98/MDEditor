from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout,QVBoxLayout, QPlainTextEdit, QLabel,QGridLayout, QTextEdit
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

    
        self.bgColor = "255,255,255"
        self.textColor = "white"

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.inputeditor = QPlainTextEdit(self)
        self.inputStyle = """ color: {color:s};background: rgba({bg:s},20%);"""    
        self.setElemFont(self.inputeditor)
        self.setElemStyle(self.inputeditor, self.inputStyle.format(color = self.textColor, bg = self.bgColor))
        self.layout.addWidget(self.inputeditor, 0, 1)


        self.outBox = QTextEdit(self)
        self.outStyle = """ color: {color:s};background: rgba({bg:s},20%);"""    
        self.setElemFont(self.outBox)
        self.setElemStyle(self.outBox, self.outStyle.format(color = self.textColor, bg = self.bgColor))
        self.outBox.setReadOnly(True)
        self.layout.addWidget(self.outBox, 0, 2)


        self.inputeditor.textChanged.connect(self.toOut) 
        self.setWindowStyle()
                        
    def toOut(self):
        self.outBox.setMarkdown(self.inputeditor.toPlainText())


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