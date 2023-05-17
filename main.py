import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Пример приложения с радиокнопками')
        self.setGeometry(300, 300, 250, 150)

        # Создаем вертикальный макет
        layout = QVBoxLayout()

        # Создаем радиокнопки
        radio_button1 = QRadioButton('Вариант 1', self)
        radio_button2 = QRadioButton('Вариант 2', self)
        radio_button3 = QRadioButton('Вариант 3', self)

        # Соединяем кнопки с одной группой
        radio_button1.setChecked(True)  # По умолчанию выбран первый вариант
        radio_button1.toggled.connect(self.onRadioButtonClicked)
        radio_button2.toggled.connect(self.onRadioButtonClicked)
        radio_button3.toggled.connect(self.onRadioButtonClicked)

        # Добавляем радиокнопки в макет
        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)
        layout.addWidget(radio_button3)

        # Создаем метку для отображения выбранного варианта
        self.label = QLabel('Вы выбрали Вариант 1', self)

        # Добавляем метку в макет
        layout.addWidget(self.label)

        # Устанавливаем макет в окне
        self.setLayout(layout)

    def onRadioButtonClicked(self):
        selected_radio_button = self.sender()

        if selected_radio_button.isChecked():
            self.label.setText(f'Вы выбрали {selected_radio_button.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
