from settings import BUFF_SIZE, hostname, port, login_base
from client_socket import ClientSocketJson

if __name__ == "__main__":
    with ClientSocketJson((hostname, port), BUFF_SIZE, login_base) as hack_tool:
        print(hack_tool.bruteforce_password_vulnerability())
