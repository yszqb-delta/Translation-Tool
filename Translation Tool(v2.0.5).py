import math
import os
import sys
import time

import DrissionPage
import keyboard
import pyperclip
from DrissionPage.common import configs_to_here
from PyQt5 import QtCore, QtGui, QtWidgets

print("请稍等……")

configs_to_here()
page = DrissionPage.ChromiumPage()
page.set.window.hide()
# page.set.window.show()
page.get("https://fanyi.youdao.com/index.html#/")

language = {
    "中文": "zh-CHS",
    "英语": "en",
    "阿拉伯语": "ar",
    "德语": "de",
    "俄语": "ru",
    "法语": "fr",
    "韩语": "ko",
    "荷兰语": "nl",
    "葡萄牙语": "pt",
    "日语": "ja",
    "泰语": "th",
    "西班牙语": "es",
    "意大利语": "it",
    "越南语": "vi",
    "印尼语": "id"
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 773)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.widget.setStyleSheet(".QWidget{\n"
                                  "    background-color:qlineargradient(spread:pad,  x1:0, x2:0, y1:0, y2:1,\n"
                                  "                                     stop: 0 rgba(22, 110, 225,255),\n"
                                  "                                     stop: 1 rgba(255,255,255,10));\n"
                                  "    border-radius:20px;\n"
                                  "    color:rgb(255,255,255)\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(25, 0, 321, 71))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_T = QtWidgets.QLabel(self.widget)
        self.label_T.setGeometry(QtCore.QRect(25, 66, 221, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
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
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(40, 100, 331, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(95, 40, 71, 23))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(5, 10, 125, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(198, 10, 125, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(133, 12, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(5, 40, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 220, 401, 541))
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
        MainWindow.move(30, 100)
        self.pushButton_2.clicked.connect(self.save_)
        self.pushButton_3.clicked.connect(self.rebuild_)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " ( ゜- ゜)つロ"))
        self.label.setText(_translate("MainWindow", "Translation Tools"))
        self.label_T.setText(_translate("MainWindow", "yszqb-delta"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.pushButton_2.setText(_translate("MainWindow", "导出"))
        self.comboBox.setItemText(0, _translate("MainWindow", "英语"))
        self.comboBox.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox.setItemText(2, _translate("MainWindow", "阿拉伯语"))
        self.comboBox.setItemText(3, _translate("MainWindow", "法语"))
        self.comboBox.setItemText(4, _translate("MainWindow", "葡萄牙语"))
        self.comboBox.setItemText(5, _translate("MainWindow", "越南语"))
        self.comboBox.setItemText(6, _translate("MainWindow", "德语"))
        self.comboBox.setItemText(7, _translate("MainWindow", "韩语"))
        self.comboBox.setItemText(8, _translate("MainWindow", "日语"))
        self.comboBox.setItemText(9, _translate("MainWindow", "印尼语"))
        self.comboBox.setItemText(10, _translate("MainWindow", "俄语"))
        self.comboBox.setItemText(11, _translate("MainWindow", "荷兰语"))
        self.comboBox.setItemText(12, _translate("MainWindow", "泰语"))
        self.comboBox.setItemText(13, _translate("MainWindow", "意大利语"))
        self.comboBox.setItemText(14, _translate("MainWindow", "西班牙语"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "中文"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "英语"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "阿拉伯语"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "法语"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "葡萄牙语"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "越南语"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "德语"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "韩语"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "日语"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "印尼语"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "俄语"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "荷兰语"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "泰语"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "意大利语"))
        self.comboBox.setItemText(14, _translate("MainWindow", "西班牙语"))
        self.label_3.setText(_translate("MainWindow", "翻译成"))
        self.pushButton_3.setText(_translate("MainWindow", "重新翻译"))

    def show_(self, txt):
        self.txt = txt
        txt_list = []
        for i in range(math.ceil(len(txt) / 12)):
            txt_list.append(txt[:12])
            txt = txt[12:]
        for txt in txt_list:
            self.listWidget.addItem(txt)

    def save_(self):
        path = os.path.join(os.path.expanduser('~'), "Desktop") + "\翻译结果.txt"
        if not os.path.exists(path):
            whether_have_data = 0
            with open(path, 'w') as f:
                f.write('')
        elif os.path.getsize(path) == 0:
            whether_have_data = 0
        else:
            whether_have_data = 1
        with open(path, 'a') as f:
            if whether_have_data == 0:
                f.write(self.txt)
            else:
                f.write("\n\n" + self.txt)
        self.listWidget.addItem("已保存在桌面")

    def rebuild_(self):
        global MainWindow
        before = self.comboBox.currentText()
        after = self.comboBox_2.currentText()
        if before != after:
            print(before, ' ', after)
            self.change_language(language[before], language[after])
        else:
            self.listWidget.addItem("请更正语言后重试")
        time.sleep(0.75)
        data = pyperclip.paste()
        get(data, 1)

    def change_language(self, language_one="en", language_two="zh-CHS"):
        print(language_one, ' ', language_two)
        page.ele(".lang-container lanFrom-container lang-container1").click(by_js=True)
        page.ele("@data-code=" + language_one).click(by_js=True)
        page.ele(".lang-container lang-container1 lanTo-container").click(by_js=True)
        page.ele("@data-code=" + language_two).click(by_js=True)

    def clear_(self):
        self.listWidget.clear()


ui = None


def show_window(txt):
    global ui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.show_(txt)
    app.exec()


def get(sentences, special=0):
    global ui
    txt_list = []
    if '.' in sentences or '?' in sentences or '!' in sentences:
        for str_ in sentences.split('.'):
            str_ = str_.replace('\n', '')

            if '?' in str_:
                txt_list.extend(str_.split('?'))
            elif '!' in str_:
                txt_list.extend(str_.split('!'))
            else:
                txt_list.append(str_)
    else:
        txt_list.append(sentences)
        txt_list.append(' ')
    txt_list = txt_list[:-1]
    txt_list2 = []
    for i in txt_list:
        page.ele('#js_fanyi_input').input(str(i))
        ele = page.ele(".tgt color_text_1")
        while True:
            if ele:
                break
            time.sleep(0.25)
        txt_list2.append(ele.html[83:-7] + '.')
        time.sleep(1)
        page.ele(".clearBtn icon_clear").click(by_js=True)
    txt = ""
    for i in txt_list2:
        txt += i
    txt_list.clear()
    txt_list2.clear()
    print("翻译后文本:", txt)
    if special == 0:
        show_window(txt)
    else:
        ui.clear_()
        ui.show_(txt)


def on_key(event):
    if event.name == 'alt':
        data = pyperclip.paste()
        print("alt-pass 原文本: ", data)
        get(data)


def change():
    if page.ele(".source").ele(".lang-container lanFrom-container"):
        page.ele(".lang-container lanFrom-container").click(by_js=True)
        page.ele("@data-code=en").click(by_js=True)
        page.ele(".lang-container lang-container1 lanTo-container").click(by_js=True)
        page.ele("@data-code=zh-CHS").click(by_js=True)
    else:
        page.ele(".lang-container lanFrom-container lang-container1").click(by_js=True)
        page.ele("@data-code=en").click(by_js=True)
        page.ele(".lang-container lang-container1 lanTo-container").click(by_js=True)
        page.ele("@data-code=zh-CHS").click(by_js=True)


show_window("请等待程序初始化，阅读完毕请按下'Close'关闭本页面")
change()
show_window("程序初始化完毕，阅读完毕请按下'Close'关闭本页面")
print("可以开始使用")

keyboard.on_press(on_key)
keyboard.wait()
