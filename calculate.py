import sys
from PySide6.QtWidgets import QApplication, QDialog, QTextBrowser, QLineEdit, QVBoxLayout


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_browser = QTextBrowser()
        self.line_edit = QLineEdit("Type an expression and press Enter")
        self.line_edit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.text_browser)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

        self.line_edit.setFocus()
        self.line_edit.returnPressed.connect(self.update_ui)
        self.setWindowTitle("Calculate")

    def update_ui(self):
        expression = self.line_edit.text()
        try:
            self.text_browser.append(f"{expression} = <b>{eval(expression)}</b>")
        except Exception as e:
            self.text_browser.append(f"<font color=red>{expression} is invalid! ({e})</font>")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
