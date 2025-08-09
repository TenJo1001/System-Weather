from PyQt6.QtWidgets import QApplication, QLabel , QVBoxLayout, QWidget, QPushButton , QLineEdit
import sys

def greet():
    name = name_input.text()
    greet_label.setText(f"Hello {name}!")
app = QApplication(sys.argv)
Window = QWidget()
Window.setWindowTitle("First System")

name_input = QLineEdit()
name_input.setPlaceholderText("Input name")
greet_button = QPushButton("Click")
greet_button.clicked.connect(greet)

greet_label = QLabel("")


layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(greet_button)
layout.addWidget(greet_label)



Window.setLayout(layout)
Window.show()
sys.exit(app.exec())
