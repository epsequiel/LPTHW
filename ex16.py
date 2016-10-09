#! /usr/bin/python

# Ejercicio 16 pag 58

from sys import argv

script, filename = argv

print "We aregoing to erase %r." % filename
print "If you don't want that, hit Ctrl-C now."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening file %s..." % filename

target = open(filename, 'r')

print "Antes de borrar vamos a leer el contenido para salvarlo."

backup = target.read()

target.close()
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")


print "Now I'm going to write these lines to the file."


target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

#print "El fichero quedo asi:"
#print target.read()

print "Ahora voy a escribir lo que salvamos del fichero original."
target.write(backup)

target.close()
target = open(filename, 'r')
print "El fichero quedo asi:"
print target.read()

target.close()

