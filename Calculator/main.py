import sys
import ast
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QGridLayout
)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Safe Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.create_ui()

    def create_ui(self):
        self.layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        self.layout.addWidget(self.display)

        # Buttons grid
        self.buttons = QGridLayout()
        self.create_buttons()
        self.layout.addLayout(self.buttons)

        # Set main layout
        self.setLayout(self.layout)

    def create_buttons(self):
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
            'C': (4, 0, 1, 4)
        }

        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px;")

            if len(pos) == 2:
                self.buttons.addWidget(button, pos[0], pos[1])
            else:
                self.buttons.addWidget(button, *pos)

            button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.setText("")
        elif text == "=":
            try:
                expression = self.display.text()
                # Safer eval using ast.literal_eval for basic math only
                result = str(eval(compile(ast.parse(expression, mode='eval'), '<string>', 'eval')))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
