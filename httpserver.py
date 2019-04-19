
# coding:utf-8
#环境：python2.7
import socket
 
from multiprocessing import Process
 
 
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    client_socket, client_address = server_socket.accept()
    while True:
        request_data = client_socket.recv(10240)
        print("request data:", request_data)
        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: received\r\n"
        response_body = "<h1>Python HTTP Test</h1>"
        response = response_start_line + response_headers + "\r\n" + response_body
 
        # 向客户端返回响应数据
        client_socket.send(bytes(response))