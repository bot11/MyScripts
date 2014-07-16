__author__ = 'bot11'

f = open("input.txt", "r")
for line in f.readlines():
    line.strip('\r\n')
    user, friend = line.split(",")
    friend.rstrip( )
    print "(%s, %s)" % (user, friend)
f.close()
