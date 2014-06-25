import ConfigParser

filename = 'test.ini'
parser = ConfigParser.SafeConfigParser()
parser.read([filename])

hosts = []
try:
    hosts = parser.sections()
except ConfigParser.DuplicateSectionError, err:
    print "Duplicate configuration error", err

for host in hosts:
    try:
        username = parser.get(host, 'username')
        password = parser.get(host, 'password')
        print "host= %s, username = %s, password = %s" % (host, username, password)
    except ValueError, err:
        print "Error while parsing", err