from PyQt4 import QtGui
from PyQt4.QtCore import QThread, pyqtSignal
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


class Worker(QThread):
    signal = pyqtSignal()
    stop = pyqtSignal()

    def __init__(self, port, parent=None):
        self.port = port
        try:
            self.ser = serial.Serial(self.port)
        except serial.SerialException, e:
            print e

        QThread.__init__(self, parent)
        self.stop.connect(self.quitThread)

    def quitThread(self):
        print "Thread Terminating"
        self.terminate()

    def run(self):
        while(1):
            try:
                x = self.ser.readline()
            except serial.SerialException, e:
                x = None
                print e
                time.sleep(1)

            except AttributeError, e:
                x = None
                print e
                time.sleep(1)

            if x:
                print "Data from Modem: ", x

            if (x == b'RING\r\n'):
                self.signal.emit()


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
        self.ui.tabWidget.setCurrentIndex(3)
        self.port = PORT
        self.ui.settings_okButton.pressed.connect(self.updatePort)
        self.ui.call_attendButton.pressed.connect(self.makeCall)
        self.ui.call_endButton.pressed.connect(self.endCall)
        self.ui.sms_button.pressed.connect(self.sendSms)
        self.ui.incoming_answer.pressed.connect(self.answerCall)
        self.ui.incoming_reject.pressed.connect(self.rejectCall)
        self.call = VoiceCall(self.port)
        self.sms = TextMessage(self.port)
        self.thread = Worker(self.port)
        self.thread.signal.connect(self.recvCall)
        self.thread.start()

    def answerCall(self):
        try:
            ser = serial.Serial(self.port)
            ser.write("ATA\r\n")
            print "Attending Call"
            time.sleep(2)
            self.ui.incoming_warn.clear()
        except Exception, e:
            print "Exception in answerCall: ", e

    def rejectCall(self):
        try:
            ser = serial.Serial(self.port)
            ser.write("ATH\r\n")
            print "Reject Call"
            time.sleep(2)
            self.ui.incoming_warn.clear()
        except Exception, e:
            print "Exception in answerCall: ", e

    def updatePort(self):
        self.port = str(self.ui.settings_port.text())
        print "Port updated to: ", self.port

    def recvCall(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.incoming_warn.setText("Incoming Call")

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

    def closeSocket(self):
        self.thread.stop.emit()
        self.thread.wait()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    app.aboutToQuit.connect(ex.closeSocket)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
