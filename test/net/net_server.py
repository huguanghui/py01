#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @文件: net_server.py
# @描述: 基于socket包实现基本的tcp的服务端
# @创建者: huguanghui
# @日期: 2019/10/27

import socket

HOST=''
PORT=5707

def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connect by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def main():
    echo_server()    

if __name__ == "__main__":
    main()