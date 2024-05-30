import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLineEdit, QTextBrowser, QVBoxLayout


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()

        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append(f"{text} = <b>{eval(text)}</b>")
            self.lineedit.clear()
        except:
            self.browser.append(f"<font color=red>{text} is invalid!</font>")
            self.lineedit.clear()


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec())
