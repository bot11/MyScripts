__author__ = 'rb509d'


class Gant:

    def __int__(self, name, libraryname, version, mlicense, url, licenseurl):
        self.name = name
        self.libraryName = libraryname
        self.version = version
        self.mlicense = mlicense
        self.url = url
        self.licenseUrl = licenseurl


def getText(str, line):
    import re
    if str == "licenseUrl":
        match = re.search(str+':\s+"(.*?)"\)', line)
    else:
        match = re.search(str+':\s+"(.*?)",', line)

    if match:
        return match.group(1)
    else:
        return "<na>"


f = open("gant.txt", "r")
for line in f.readlines():
    name = getText("name", line)
    libraryName = getText("libraryName", line)
    version = getText("version", line)
    mlicense = getText("license", line)
    url = getText("url", line)
    licenseUrl = getText("licenseUrl", line)
    print "%s,%s,%s,%s,%s,%s" % (name, libraryName, version,  mlicense, url, licenseUrl)
