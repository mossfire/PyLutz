'''
#Работа с сервисом погоды OWM
from pyowm.owm import OWM
owm=OWM('FreeApiKey') # TODO: hide FreeApiKey: 0468445dd48b09d6e3b247de97195500
weather_mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moscow,RU')
'''


#работа с QT
from PyQt5.QtCore import QWaitCondition
import pyowm
import PyQt5
from PyQt5 import QtWidgets
import sys
app=QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Liilith SaqAta')
window.resize(250,100)
label=QtWidgets.QLabel('<center> <b>It is a good day to Die</b></center>')
btnQuit=QtWidgets.QPushButton('&Close')
btnBeep=QtWidgets.QPushButton('&Beep')
vbox=QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
vbox.addWidget(btnBeep)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
btnBeep.clicked.connect(app.beep)

window.show()
sys.exit(app.exec_())

