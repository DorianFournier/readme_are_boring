# This Python file uses the following encoding: utf-8
import sys
#from PySide2.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QFileDialog
#permet de charger le fichier .ui
from PyQt5 import uic

class window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(r'/home/dorian/GitProjects/readme_are_boring/readme_generator/readme_generator.ui', self)

        self.lineEdit = self.findChild(QLineEdit, 'titleEdit')
        self.subLineEdit = self.findChild(QLineEdit, 'subtitle_edit')

        self.openFileNameDialog()

        self.buttonBox.accepted.connect(self.validate)
        self.show()

    def openFileNameDialog(self):
         options = QFileDialog.Options()
         options |= QFileDialog.DontUseNativeDialog
         fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
         if fileName:
             print(fileName)

    def validate(self):
        print(self.lineEdit.text())
        with open('readme.md', 'w') as f:
            # empty ?
            if self.lineEdit.text():
                f.write('# '+self.lineEdit.text()+'\n')
            if self.subLineEdit.text():
                f.write('## '+self.subLineEdit.text())

if __name__ == "__main__":
    app = QApplication([])
    window = window()
    window.show()
    sys.exit(window.exec_())
    #sys.exit(app.exec_())
