import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import MainWndow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWndow()
    MainWindow.show()
    sys.exit(app.exec_())