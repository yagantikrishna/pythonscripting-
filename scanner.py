from socket import *
from termcolor import colored
from argparse import ArgumentParser
from threading import *

def connScan(tgthost, tgtport):
    try:
        sock =socket(AF_INET, SOCK_STREAM)
        sock.connect((tgthost,tgtport))
        print('[+] %d/tcp Open' %tgtport)
    except:
        print('[-] %d/tcp closed' %tgtport)

    finally:
        sock.close()

def portScan(tgthost, tgtports):
    
    try:
        tgtIP = gethostbyname(tgthost)
    except:
        print('Unknown Host %s' %tgthost)
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan results for: ' + tgtName[0])
    except:
        print('[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(2)
    for tgtport in tgtports:
        t = Thread(target=connScan, args=(tgthost, int(tgtport)))
        t.start()


def main():
    parser = ArgumentParser('Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_argument('-H', dest='tgthost', type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtport', type=str, help='specify target ports separated by comma')
    args= parser.parse_args()
    tgthost = args.tgthost
    tgtports = str(args.tgtport).split(',')
    if (tgthost==None) | (tgtports[0] ==None):
        print(parser.usage)
        exit(0)
    portScan(tgthost,tgtports)

if __name__ == '__main__':
    main()
