import unittest
import client
import socket


class Test_service(unittest.TestCase):

    def test_1(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('', 8888))
        client_socket.send('message1'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'reply1')
        client_socket.close()

    def test_2(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('', 8888))
        client_socket.send('message2'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'reply2')
        client_socket.close()

if __name__ == '__main__':
    unittest.main()