#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: net_server.py
# @描述: 基于socket包实现基本的tcp的客户端
# @创建者: huguanghui
# @日期: 2019/10/27

import socket

HOST='192.168.6.91'
PORT=1234

def echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello World!')
        data = s.recv(1024)
        print('Recive: ', data)
        

def main():
    echo_client()

if __name__ == "__main__":
    main()