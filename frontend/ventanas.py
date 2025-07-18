from sys import __excepthook__, exit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout

class VentanaPrincipal(QWidget):
    senal_tipo_numero = pyqtSignal(str, str)
    
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(500, 80, 400, 600)
        self.setWindowTitle('APPBinario')
        self.label = QLabel('Ingrese su número a transformar: ', self)
        self.input_num = QLineEdit('', self)
        self.input_num.returnPressed.connect(self.boton_presionado)
        self.selector_numero = QComboBox(self)
        self.selector_numero.addItems(['Decimal', 'Binario', 'Hexadecimal'])
        self.boton_seleccionar = QPushButton('Seleccionar', self)
        self.boton_seleccionar.clicked.connect(self.boton_presionado)
        
        hbox_ledit = QHBoxLayout()
        hbox_cbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        
        hbox_ledit.addStretch(1)
        hbox_ledit.addWidget(self.label)
        hbox_ledit.addWidget(self.input_num)
        hbox_ledit.addStretch(1)
        
        hbox_cbox.addStretch(1)
        hbox_cbox.addWidget(self.selector_numero)
        hbox_cbox.addWidget(self.boton_seleccionar)
        hbox_cbox.addStretch(1)

        self.vbox.addLayout(hbox_ledit)
        self.vbox.addLayout(hbox_cbox)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)
    
    def boton_presionado(self) -> None:
        texto = self.selector_numero.currentText()
        num = self.input_num.text()
        self.senal_tipo_numero.emit(texto, num)
    
    def mostrar_resultado(self, resultado: tuple) -> None:
        self.resultado_1 = QLabel(f'{resultado[0]}', self)
        self.resultado_2 = QLabel(f'{resultado[1]}', self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.resultado_1)
        hbox.addStretch(1)
        hbox.addWidget(self.resultado_2)
        hbox.addStretch(1)
        
        
        self.vbox.addLayout(hbox)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    __excepthook__ = hook

    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    exit(app.exec())