
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time
from playsound import playsound

### Função - Mensagem de erro informação dos minutos
def mens_minutos():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção')
        msg1.setText('Favor o informar tempo em minutos!')
        x = msg1.exec_()

### Função - Cronometro
       
def cronometro():
    try:
        tela.pb_cronometro.setValue(0)
        if tela.ln_tempo.text() == "":
            mens_minutos()
            tela.ln_tempo.setFocus()

        else:

            tempo = int(tela.ln_tempo.text()) * 60 /100

            for x in range(101): 
                time.sleep(tempo)
                tela.pb_cronometro.setValue(x)
            playsound("sino.mp3")
    except:
         mens_minutos()


app=QtWidgets.QApplication([])
tela=uic.loadUi("pomodoro.ui")
tela.setFixedSize(296, 150)
tela.bt_iniciar.clicked.connect(cronometro)
tela.show()
app.exec()