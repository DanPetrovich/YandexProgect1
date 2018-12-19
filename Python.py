import sys
from PythonProgect import *


class MyWin(QtWidgects.QMainWindow):
    def __init__(self,parent-None):
        QtWidgects.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.getResult.clicked.connect(self.getResult)

    def getResult(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
