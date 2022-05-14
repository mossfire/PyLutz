#работа с OWM сервисом погоды
#import pyowm
import PyQt5
from PyQt5 import QtWidgets
import sys
app=QtWidgets.QApplication(sys.argv)
window = QtWidget.QWidget()
window.setWindowsTitle('Liilith SaqAta')

from pyowm.owm import OWM
owm=OWM('0468445dd48b09d6e3b247de97195500')
weather_mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moscow,RU')
