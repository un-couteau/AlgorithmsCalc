import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from Algorithms import Algorithms


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычислить")

        # Создаем вертикальный контейнер для размещения виджетов
        layout = QVBoxLayout()

        variables_layout = QHBoxLayout()
        variables_label_layout = QVBoxLayout()
        variables_text_layout = QVBoxLayout()

        choose_algorithms = QHBoxLayout()

        # Создаем две кнопки для выбора
        linear = QPushButton("Линейный")
        branching = QPushButton("Разветленный")

        choose_algorithms.addWidget(linear)
        choose_algorithms.addWidget(branching)

        # Создаем поле для изображения
        pixmap = QPixmap("Images/linear.png")
        pixmap_label = QLabel("fff")
        pixmap_label.setPixmap(pixmap)

        # Создаем поле для вывода результата
        self.result_label = QLabel("Результат: ")

        # Создаем три поля для ввода переменных
        variable1_label = QLabel("Variable x: ")
        variable2_label = QLabel("Variable y: ")
        variable3_label = QLabel("Variable z: ")
        variable2 = QLineEdit("1")
        variable3 = QLineEdit("2")
        variable1 = QLineEdit("3")

        variables_label_layout.addWidget(variable1_label)
        variables_label_layout.addWidget(variable2_label)
        variables_label_layout.addWidget(variable3_label)
        variables_text_layout.addWidget(variable2)
        variables_text_layout.addWidget(variable3)
        variables_text_layout.addWidget(variable1)
        variables_layout.addLayout(variables_label_layout)
        variables_layout.addLayout(variables_text_layout)

        # Добавляем все элементы в вертикальный контейнер
        layout.addLayout(choose_algorithms)
        layout.addWidget(pixmap_label)
        layout.addLayout(variables_layout)
        layout.addWidget(self.result_label)

        # Создаем горизонтальный контейнер для размещения изображения и вертикального контейнера
        hbox = QHBoxLayout()
        hbox.addLayout(layout)

        # Создаем основной виджет и устанавливаем горизонтальный контейнер в качестве макета
        widget = QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)

        linear.clicked.connect(self.get_result_of_linear_algorithm(float(variable1.text()), float(variable2.text()), float(variable3.text())))

    def get_result_of_linear_algorithm(self, x: float, y: float, z: float):
        try:
            res = Algorithms()
            self.result_label.setText("Результат: " + str(res.linear_algoritm(x, y, z)))
        except ValueError:
            self.result_label.setText(str("Ошибка: введите число"))


    # def get_result_of_branching_algorithm(self, x, y, z):
    #     res = Algorithms()
    #     self.result_label.setText(str(res.branching_algorithm(x, y, z)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec_())
