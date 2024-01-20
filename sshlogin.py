import pexpect

PROMPT =['# ', '>>> ', '> ', '\$ ']

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting  (yes/no/[fingerprint])?'
    connStr = 'ssh ' +  user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] rror connecting')

    if ret ==1:
        child.sendline('yes')
        ret =child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
        if ret == 0:
         print('[-] rror connecting')
         return 
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = input("Enter ip address: ")
    user = input('Enter username: ')
    password = input('Enter password')
    child =connect(user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps')

main()