import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(900)
        return banner
    except:
        return

def main():
    ip = input("[+] Enter the ip: ")
    for port in range(1,100):
     banner = retBanner(ip,port)
     if banner:
        print('[+]' + ip + ' ' + str(port) + ': ' + str(banner))
main()