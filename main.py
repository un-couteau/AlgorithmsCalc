import sys

from PyQt5.QtWidgets import QApplication

from src.frontend.userInterface import MainWindow
from src.backend.algorithms import Algorithms


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
