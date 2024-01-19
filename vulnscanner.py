import socket
import os
import sys

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(900)
        return banner.decode('utf-8')
    except:
        return
    
def checkVulns(banner, filename):
    f=open(filename, "r")
    for line in f.readlines():
        if line.strip('\n') in banner:
            print(f'[+]' + 'Server is vulnerable ' + banner.strip("\n") + "\n")
            

   


def main():
   if len(sys.argv) == 2:
        filename =sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] file doesnt exist!')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] Access Denied!')
            exit(0)

   else:
        print('[-]Usage: '+ str(sys.argv[0]) + 'vuln file name')
        exit(0)
              
   portlist = [21,22,23,25,80,443,445,636,990]
   for x in range(71,73):
        ip="192.168.1." + str(x)
        for port in portlist:
            banner =retBanner(ip,port)
            if banner:
                print('[+] ' + ip + '/'+ str(port) + ': ' + str(banner))
                checkVulns(banner, filename)

main()
