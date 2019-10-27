#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5的实现基本网络通信
# @创建者: huguanghui
# @日期: 2019/10/27

from GUI import Ui_Main
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import socket

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main.Ui_MainWindow()
        self.ui.setupUi(self)

    def ui_init(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()