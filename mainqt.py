from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout,QVBoxLayout, QPlainTextEdit, QLabel,QGridLayout, QTextEdit, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import sys
from BlurWindow.blurWindow import blur

#source ../env/Scripts/activate
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.title = "MDEditor"
        self.bgColor = "0,0,0"
        self.textColor = "white"
        self.transparency = "20"
        self.darkTheme = True

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.prepareInputBox()
        self.prepareOutputBox()

        self.declareConnections()

        self.setWindowStyle()
                        
    def toOut(self):
        self.outBox.setMarkdown(self.inputeditor.toPlainText())

    def prepareInputBox(self):
        self.inputeditor = QTextEdit(self)
        self.inputStyle = """ color: {color:s};background: rgba({bg:s},{t:s}%);padding-left:25px;padding-right:25px;padding-top:35px"""  
        self.setElemFont(self.inputeditor)
        self.setElemStyle(self.inputeditor, self.inputStyle.format(color = self.textColor, bg = self.bgColor, t = self.transparency))
        self.layout.addWidget(self.inputeditor, 0, 1)

    def prepareOutputBox(self):
        self.outBox = QTextEdit(self)
        self.outStyle = """ color: {color:s};background: rgba({bg:s},{t:s}%);padding-left:25px;padding-right:25;padding-top:35px"""    
        self.setElemFont(self.outBox)
        self.setElemStyle(self.outBox, self.outStyle.format(color = self.textColor, bg = self.bgColor, t = self.transparency))
        self.outBox.setReadOnly(True)
        self.layout.addWidget(self.outBox, 0, 2)

    def declareConnections(self):
        self.inputeditor.textChanged.connect(self.toOut) 

    def setElemFont(self, elem, f = None):
        if f is None:
            f = QtGui.QFont('Arial', 10)
        elem.setFont(f)

        
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

class WrapperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = MainWindow()
        self.resize(1500, 900)
        self.setCentralWidget(self.editor)

        self.setWindowTitle(" ")
        self.darkTheme = True
        self.blurEditor()

        self.icon = QPixmap(32,32)

        self.icon.fill( Qt.transparent );
        self.setWindowIcon(QIcon( self.icon));

    def blurEditor(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        hWnd = self.winId()
        blur(hWnd,Dark=self.darkTheme)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = WrapperWindow()
    mw.show()
    sys.exit(app.exec_())