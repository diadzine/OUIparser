from pyparsing import *


hexint = Word(hexnums,exact=2)
macAddressPrefix = Combine(hexint + ('-'+hexint)*2)
vendorName = Word(alphanums)
definition = macAddressPrefix("macPrefix") + "(hex)" + vendorName("vendor")

file = open('oui.txt', 'r')
it = file.readlines()

for line in it:
    for statement in definition.searchString(line):
        print statement.macPrefix,'->',statement.vendor
        print

file.close()
