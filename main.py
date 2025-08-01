import backend.backend as back
from frontend.ventanas import VentanaPrincipal
from sys import __excepthook__, exit
from PyQt5.QtWidgets import QApplication

class AppBinario:
    def __init__(self) -> None:
        self.front = VentanaPrincipal()
        self.back = back.Transformador()
    
    def conectar(self) -> None:
        self.front.senal_tipo_numero.connect(self.back.selector)
        self.back.senal_resultado.connect(self.front.mostrar_resultado)
        self.back.senal_error.connect(self.front.mostrar_error)

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    __excepthook__ = hook

    app = QApplication([])
    
    app_bin = AppBinario()
    app_bin.conectar()
    app_bin.front.show()

    exit(app.exec())