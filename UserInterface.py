import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from Algorithms import Algorithms

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычислить")
        self.layout = QVBoxLayout()
        self.choose_algorithms = QHBoxLayout()
        self.label = QVBoxLayout()
        self.text = QVBoxLayout()
        self.variables = QHBoxLayout()

        self.linear = QPushButton("Линейный")
        self.branching = QPushButton("Разветленный")

        self.pixmap = QPixmap("Images/linear.png")
        self.pixmap_label = QLabel("fff")
        self.pixmap_label.setPixmap(self.pixmap)

        self.x_label = QLabel("x:")
        self.x_text = QLineEdit()

        self.y_label = QLabel("y:")
        self.y_text = QLineEdit()

        self.z_label = QLabel("z")
        self.z_text = QLineEdit()

        self.result_label = QLabel("Результат:")

        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate_result)

        self.choose_algorithms.addWidget(self.linear)
        self.choose_algorithms.addWidget(self.branching)

        self.layout.addLayout(self.choose_algorithms)
        self.layout.addWidget(self.pixmap_label)
        self.label.addWidget(self.x_label)
        self.label.addWidget(self.y_label)
        self.label.addWidget(self.z_label)
        self.text.addWidget(self.x_text)
        self.text.addWidget(self.y_text)
        self.text.addWidget(self.z_text)
        self.variables.addLayout(self.label)
        self.variables.addLayout(self.text)

        self.layout.addLayout(self.variables)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.calculate_button)

        self.setLayout(self.layout)

    def calculate_result(self):
        x = float(self.x_text.text())
        y = float(self.y_text.text())
        z = float(self.z_text.text())

        result = Algorithms()

        self.result_label.setText("Результат: " + str(result.linear_algoritm(x, y, z)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
