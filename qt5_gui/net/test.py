#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: test.py
# @描述: 基于Pyqt5的实现基本网络通信
# @创建者: huguanghui
# @日期: 2019/10/27

import os
import sys
import socket
import time
import yaml
import struct
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from GUI import Ui_Main
from PyQt5 import QtWidgets,QtCore,QtGui

config_path = os.path.join(os.path.dirname(__file__), 'config.yml')

with open(config_path) as f:
    cont = f.read()

cf = yaml.load(cont, Loader=yaml.FullLoader)

def save_yaml():
    with open(config_path, "w") as f:
        yaml.dump(cf, f)

class RunThread(QtCore.QThread):
	def __init__(self, parent=None):
		super(RunThread, self).__init__(parent)
		self.is_running = True
	
	def run(self):
		while self.is_running == True:
			time.sleep(1)
			print("Timeing...")

	def stop(self):
		self.is_running = False
		print('线程停止中...')
		self.terminate()

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_init()
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ui.pushButton.clicked.connect(self.tcp_connect)
        self.ui.pushButton_2.clicked.connect(self.tcp_disconnect)
        self.ui.pushButton_3.clicked.connect(self.tcp_refresh)

    def ui_init(self):
        # 加载配置
        stip = cf.get('ip')
        if stip != None:
            self.ui.lineEdit.setText(stip)
        stport = cf.get('port')
        if stport != None:
            self.ui.lineEdit_2.setText(stport)
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.lineEdit_4.setReadOnly(True)
        self.ui.lineEdit_5.setReadOnly(True)
        self.ui.lineEdit_6.setReadOnly(True)
        self.ui.lineEdit_7.setReadOnly(True)
        self.ui.lineEdit_8.setReadOnly(True)
        self.ui.lineEdit_9.setReadOnly(True)
        self.ui.lineEdit_10.setReadOnly(True)

    def tcp_connect(self):
        ip = self.ui.lineEdit.text()
        port = self.ui.lineEdit_2.text()
        cf['ip'] = ip
        cf['port'] = port
        save_yaml()
        print('net['+ip+':'+port+']')
        self.sockfd.connect((ip, int(port)))
        # self.run_thread = RunThread(parent=None)
        # self.run_thread.start()

    def tcp_refresh(self):
        # struct Header
        # {
        #     int type;
        #     int seq;
        #     int dataLen;
        # }
        #    char *data;
        ss = struct.pack('iii', 0, 0, 0)
        self.sockfd.sendall(ss)
        data = self.sockfd.recv(1024)
        status, = struct.unpack("i", data)
        print('Recive: ', status)

    def tcp_disconnect(self):
        self.sockfd.close()
        # try:
        #     self.run_thread.stop()
        # except:
        #     pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()