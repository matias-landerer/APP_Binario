from sys import __excepthook__, exit
from PyQt5.QtWidgets import QWidget, QApplication

class VentanaPrincial(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(500, 80, 400, 600)


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    __excepthook__ = hook

    app = QApplication([])
    ventana = VentanaPrincial()
    ventana.show()
    exit(app.exec())