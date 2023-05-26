import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton
from PyQt5.QtGui import QPixmap
from src.backend.algorithms import Algorithms

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

        self.pixmap_linear = QPixmap("extras/images/linear.png")
        self.pixmap_label_linear = QLabel("fff")
        self.pixmap_label_linear.setPixmap(self.pixmap_linear)

        self.pixmap_branching = QPixmap("extras/images/branching.png")
        self.pixmap_label_branching = QLabel("fff")
        self.pixmap_label_branching.setPixmap(self.pixmap_branching)
        self.pixmap_label_branching.hide()

        self.x_label = QLabel("x:")
        self.x_text = QLineEdit()

        self.y_label = QLabel("y:")
        self.y_text = QLineEdit()

        self.z_label = QLabel("z:")
        self.z_text = QLineEdit()

        self.result_label = QLabel("Результат:")

        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.get_linear_algorithm_result)

        self.choose_algorithms.addWidget(self.linear)
        self.choose_algorithms.addWidget(self.branching)
        self.branching.clicked.connect(self.set_branching)
        self.linear.clicked.connect(self.set_linear)

        self.layout.addLayout(self.choose_algorithms)
        self.layout.addWidget(self.pixmap_label_linear)
        self.layout.addWidget(self.pixmap_label_branching)
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

    def get_linear_algorithm_result(self):
        try:
            x = float(self.x_text.text())
            y = float(self.y_text.text())
            z = float(self.z_text.text())

            result = Algorithms()

            self.result_label.setText("Результат: " + str(result.linear_algoritm(x, y, z)))
        except ValueError:
            self.result_label.setText("Введите переменные")

    def get_branching_algorithm_result(self):
        try:
            x = float(self.x_text.text())
            y = float(self.y_text.text())
            f = self.on_func_clicked()

            result = Algorithms()
            self.result_label.setText("Результат: " + str(result.branching_algorithm(x, y, f)))
        except ValueError:
            self.result_label.setText("Введите переменные")

    def on_func_clicked(self) -> str:
        if self.func1.isChecked():
            return "cos(x)"
        elif self.func2.isChecked():
            return "sqr(x)"
        elif self.func3.isChecked():
            return "exp(x)"

    def set_linear(self):
        if self.change_algorithm:
            self.pixmap_label_branching.hide()
            self.pixmap_label_linear.show()
            self.choose_func.hide()
            self.func1.hide()
            self.func2.hide()
            self.func3.hide()
            self.z_label.show()
            self.z_text.show()

    def set_branching(self):
        self.change_algorithm = True
        self.pixmap_label_linear.hide()
        self.pixmap_label_branching.show()
        self.choose_func = QLabel("Выбор функции")
        self.z_label.hide()
        self.z_text.hide()

        self.func1 = QRadioButton('cos(x)', self)
        self.func2 = QRadioButton('sqr(x)', self)
        self.func3 = QRadioButton('exp(x)', self)

        self.func1.setChecked(True)
        self.func1.toggled.connect(self.on_func_clicked)
        self.func2.toggled.connect(self.on_func_clicked)
        self.func3.toggled.connect(self.on_func_clicked)

        self.choose_func_layout = QVBoxLayout()
        self.choose_func_layout.addWidget(self.choose_func)
        self.choose_func_layout.addWidget(self.func1)
        self.choose_func_layout.addWidget(self.func2)
        self.choose_func_layout.addWidget(self.func3)
        self.variables.addLayout(self.choose_func_layout)
        self.calculate_button.clicked.connect(self.get_branching_algorithm_result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
