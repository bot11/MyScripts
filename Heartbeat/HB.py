__author__ = 'bot11'

import HBExceptions
import re

configfile = 'config.txt'
hosts = {}


def readconfig():
    try:
        f = open(configfile, 'r')
    except (IOError, OSError), err:
        print HBExceptions.file_not_found(err)

    for line in f:
        if re.match('^\s?#', line):
            continue
        else:
            temp = line.split(';')
            hosts[temp[0]] = temp[1]+";"+temp[2]
    f.close()


if __name__ == 'main':
    readconfig()