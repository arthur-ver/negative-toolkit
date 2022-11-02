import socket


def sendViaUDP(
        color: str,
        ip: str,
        port: int = 100
    ) -> bytes:
    '''
    Switch display color

    :param str color: ("w") white, ("r") red, ("g") green, ("b") blue, ("grid") alignment grid
    :param str ip: UDP server ip
    :param int port: UDP server port
    :return: server respond should be "ok"
    :rtype: bytes
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    s.sendto(bytes(color, "utf-8"), (ip, port))
    data, addr = s.recvfrom(1024)
    s.close()
    return data
