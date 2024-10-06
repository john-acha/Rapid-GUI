import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QDoubleSpinBox, QComboBox, QLineEdit, QGridLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        principal_label = QLabel("Principal:")
        self.principal_spinbox = QDoubleSpinBox()
        self.principal_spinbox.setRange(1, 1000000000)
        self.principal_spinbox.setValue(1000)
        self.principal_spinbox.setPrefix("$")

        rate_label = QLabel("Rate:")
        self.rate_spinbox = QDoubleSpinBox()
        self.rate_spinbox.setRange(1, 100)
        self.rate_spinbox.setValue(5)
        self.rate_spinbox.setSuffix("%")

        years_label = QLabel("Years:")
        self.years_combobox = QComboBox()
        self.years_combobox.addItem("1 year")
        self.years_combobox.addItems([f"{x} years" for x in range(2, 26)])

        amount_label = QLabel("Amount:")
        self.amount_edit = QLineEdit()
        self.amount_edit.setReadOnly(True)

        grid_layout = QGridLayout()
        grid_layout.addWidget(principal_label, 0, 0)
        grid_layout.addWidget(self.principal_spinbox, 0, 1)
        grid_layout.addWidget(rate_label, 1, 0)
        grid_layout.addWidget(self.rate_spinbox, 1, 1)
        grid_layout.addWidget(years_label, 2, 0)
        grid_layout.addWidget(self.years_combobox, 2, 1)
        grid_layout.addWidget(amount_label, 3, 0)
        grid_layout.addWidget(self.amount_edit, 3, 1)
        self.setLayout(grid_layout)

        self.principal_spinbox.valueChanged.connect(self.update_ui)
        self.rate_spinbox.valueChanged.connect(self.update_ui)
        self.years_combobox.currentIndexChanged.connect(self.update_ui)

        self.setWindowTitle("Interest")
        self.update_ui()

    def update_ui(self):
        """Calculates compound interest."""
        principal = self.principal_spinbox.value()
        rate = self.rate_spinbox.value()
        years = self.years_combobox.currentIndex() + 1
        amount = principal * ((1 + (rate/100.0))**years)
        self.amount_edit.setText(f"${amount:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
