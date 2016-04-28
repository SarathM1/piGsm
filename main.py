from PyQt4 import QtGui  # , QtCore
from py_file import Ui_Dialog
import sys
import time
import serial

PORT = '/dev/ttyUSB0'       # Default value


class VoiceCall:
    def __init__(self, port):
        self.port = port

    def dialNumber(self, number='9496354518'):
        self.number = number
        self.ser = serial.Serial(self.port)
        self.ser.write('ATZ\r')
        # ATZ : Restore profile ##
        time.sleep(1)
        self.ser.write('ATD ' + self.number + ';\r')
        # ATD : Dial command ##
        # semicolon : voice call ##
        time.sleep(1)
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)
        time.sleep(1)
        time.sleep(1)

    def endCall(self):
        self.ser = serial.Serial(self.port)
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CHUP\r')
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)


class TextMessage:
    def __init__(self, port):
        self.port = port

    def sendMessage(self, text, number='9496354518'):
        self.number = number
        self.text = text
        self.ser = serial.Serial(self.port)
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.number + '''"\r''')
        time.sleep(1)
        self.ser.write(self.text + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)


class Gui(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(2)
        self.port = PORT
        self.ui.settings_okButton.pressed.connect(self.updatePort)
        self.ui.call_attendButton.pressed.connect(self.makeCall)
        self.ui.call_endButton.pressed.connect(self.endCall)
        self.ui.sms_button.pressed.connect(self.sendSms)
        self.call = VoiceCall(self.port)
        self.sms = TextMessage(self.port)

    def updatePort(self):
        self.port = str(self.ui.settings_port.text())
        print "Port updated to: ", self.port

    def sendSms(self):
        try:
            number = self.ui.call_number.text()
            number = str(number)
            text = self.ui.sms_text.toPlainText()
            self.sms.sendMessage(text, number)

        except Exception, e:
            self.ui.call_number.clear()
            print e

    def makeCall(self):
        try:
            number = self.ui.call_number.text()
            number = str(number)

            self.call.dialNumber(number)

        except Exception, e:
            self.ui.call_number.clear()
            print e

    def endCall(self):
        self.call.endCall()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    # app.aboutToQuit.connect(ex.flags.closeSocket)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
