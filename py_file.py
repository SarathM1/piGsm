# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_file.ui'
#
# Created: Thu Apr 28 23:15:22 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 291))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 60, 201, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.call_number = QtGui.QLineEdit(self.gridLayoutWidget)
        self.call_number.setMaxLength(10)
        self.call_number.setObjectName(_fromUtf8("call_number"))
        self.gridLayout.addWidget(self.call_number, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.call_attendButton = QtGui.QPushButton(self.tab)
        self.call_attendButton.setGeometry(QtCore.QRect(90, 160, 85, 27))
        self.call_attendButton.setObjectName(_fromUtf8("call_attendButton"))
        self.call_endButton = QtGui.QPushButton(self.tab)
        self.call_endButton.setGeometry(QtCore.QRect(190, 160, 85, 27))
        self.call_endButton.setObjectName(_fromUtf8("call_endButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 251, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sms_number = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.sms_number.setMaxLength(10)
        self.sms_number.setObjectName(_fromUtf8("sms_number"))
        self.gridLayout_2.addWidget(self.sms_number, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.sms_button = QtGui.QPushButton(self.tab_2)
        self.sms_button.setGeometry(QtCore.QRect(260, 200, 71, 27))
        self.sms_button.setObjectName(_fromUtf8("sms_button"))
        self.sms_text = QtGui.QTextEdit(self.tab_2)
        self.sms_text.setGeometry(QtCore.QRect(80, 100, 251, 78))
        self.sms_text.setObjectName(_fromUtf8("sms_text"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 70, 221, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.settings_port = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.settings_port.setObjectName(_fromUtf8("settings_port"))
        self.horizontalLayout.addWidget(self.settings_port)
        self.settings_okButton = QtGui.QPushButton(self.tab_3)
        self.settings_okButton.setGeometry(QtCore.QRect(260, 170, 51, 27))
        self.settings_okButton.setObjectName(_fromUtf8("settings_okButton"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PiGSM", None))
        self.label.setText(_translate("Dialog", "Number", None))
        self.call_attendButton.setText(_translate("Dialog", "Call", None))
        self.call_endButton.setText(_translate("Dialog", "End", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Call", None))
        self.label_2.setText(_translate("Dialog", "Number", None))
        self.sms_button.setText(_translate("Dialog", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "SMS", None))
        self.label_3.setText(_translate("Dialog", "PORT:", None))
        self.settings_okButton.setText(_translate("Dialog", "Ok", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Port", None))

