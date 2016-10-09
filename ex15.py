#! /usr/bin/python

# ejercicio 15 pag 54

from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r: " % filename
print txt.read()

print "[*] Closed: %s" % txt.closed
print "[*] cerrando..."
txt.close()
print "[*] Closed: %s" % txt.closed


print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print "[*] Closed: %s" % txt_again.closed
print "[*] cerrando..."
txt_again.close()
print "[*] Closed: %s" % txt_again.closed
