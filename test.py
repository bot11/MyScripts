import ConfigParser

filename = 'test.ini'
parser = ConfigParser.SafeConfigParser()
parser.read([filename])

for section in parser.sections():
    try:
        host = section
        username = parser.get(section, 'username')
        password = parser.get(section, 'password')
        print "host= %s, username = %s, password = %s" % (host, username, password)
    except ValueError, err:
        print "Error while parsing", err