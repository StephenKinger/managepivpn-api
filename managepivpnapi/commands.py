import pexpect

class CommandsConfig():
    def __init__(self):
        self.command = 'pivpn'
        self.userFileList = '/etc/openvpn/easy-rsa/keys/index.txt'
    def getUserFileList(self):
        return self.userFileList

class CommandsPiVPN():
    def __init__(self):
        self.conf = CommandsConfig()

    def addUser(self, name, passwd):
        print 'Adding User'
        spawner = pexpect.spawn('sudo bash /opt/pivpn/makeOVPN.sh')
        spawner.expect("Enter a Name for the Client:  ")
        spawner.sendline(name)
        spawner.expect("Enter the password for the client:  ")
        spawner.sendline(passwd)
        spawner.expect("Enter the password again to verify:  ")
        spawner.sendline(passwd)
        spawner.eof()

    def getUserList(self):
        print 'retreiving user list'
        myUserList = []
        with open(self.conf.getUserFileList(), 'r') as user_file:
            line = user_file.readline()
            splitter = line.split('=')
            name = splitter[6].split('\/')[0]
            sate = 'Unknown'
            if line.startswith('V'):
                state = 'Valid'
            elif line.startswith('R'):
                state = 'Revoked'
            id = splitter[0].split('\t')[1];
            myUserList.push({'name' : name, 'state' : state, 'id': id})
        return myUserList