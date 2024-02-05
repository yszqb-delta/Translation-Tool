from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import DrissionPage
import pyperclip
import keyboard
import math
import time
import sys

page = DrissionPage.ChromiumPage()
page.get("https://fanyi.youdao.com/index.html#/")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 693)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 111))
        self.widget.setStyleSheet(".QWidget{\n"
                                  "    background-color:qlineargradient(spread:pad,  x1:0, x2:0.25, y1:0, y2:1,\n"
                                  "                                     stop: 0 rgba(175, 255, 184,225),\n"
                                  "                                     stop: 0.75 rgba(169, 255, 236,200),\n"
                                  "                                     stop: 1 rgba(255,255,255,0));\n"
                                  "    border-radius:20px;\n"
                                  "    color:rgb(255,255,255)\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 0, 311, 71))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_T = QtWidgets.QLabel(self.widget)
        self.label_T.setGeometry(QtCore.QRect(20, 70, 221, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_T.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_T.setFont(font)
        self.label_T.setObjectName("label_T")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(".QPushButton{\n"
                                      "    bakground-color:rgba(255,255,0,0);\n"
                                      "    border-radius:20px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 401, 551))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(".QListWidget{background:transparent}\n"
                                      "QListView {border:transparent}\n"
                                      ".QListWidget{\n"
                                      "    color:rgb(255, 85, 0);\n"
                                      "    font-size:30px;\n"
                                      "}")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.move(0, 250)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " ( ゜- ゜)つロ"))
        self.label.setText(_translate("MainWindow", "yszqb - delta"))
        self.label_T.setText(_translate("MainWindow", "Translation Tool"))
        self.pushButton.setText(_translate("MainWindow", "Close"))

    def show_(self, txt):
        txt_list = []
        for i in range(math.ceil(len(txt) / 12)):
            txt_list.append(txt[:12])
            txt = txt[12:]
        for txt in txt_list:
            self.listWidget.addItem(txt)


def show_(txt):
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    ui.show_(str(txt))
    app.exec()


def get(sentences):
    if sentences != "":
        txt_list = []
        for str_ in sentences.split('.'):
            str_ = str_.replace('\n', '')
            if '?' in str_:
                txt_list.extend(str_.split('?'))
            elif '!' in str_:
                txt_list.extend(str_.split('!'))
            else:
                txt_list.append(str_)
        txt_list = txt_list[:-1]
        if len(txt_list) == 0:
            txt_list.append(sentences)
        txt_list2 = []
        for i in txt_list:
            page.ele('#js_fanyi_input').input(str(i))
            ele = page.ele(".tgt color_text_1")
            while True:
                if ele:
                    break
                time.sleep(0.25)
            txt_list2.append(ele.html[83:-7] + ' ')
            time.sleep(1)
            page.ele(".clearBtn icon_clear").click()
        txt = ""
        for i in txt_list2:
            txt += i
        txt_list.clear()
        txt_list2.clear()
        show_(txt)


def on_key(event):
    if event.name == 'alt':
        get(pyperclip.paste())
    elif event.name == 'end':
        keyboard.unhook_all()
        sys.exit()


keyboard.on_press(on_key)
keyboard.wait()
