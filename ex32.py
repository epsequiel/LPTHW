#! /usr/bin/python

# Ejercicio 32 pagina 106

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Ciclo sobre una lista
for number in the_count:
    print "This is the count %d" % number

# Mismo tipo de ciclo
for fruit in fruits:
    print "A fruit of type %s" % fruits

# Tambien podemos recorrer listas cuyos elementos son
# de diferente tipo de dato/
# Como no sabemos de antemano el tipo usamos '%r'
for i in change:
    print "I got %r" % i

# Tambien podemos construir listas
elements = []

# Luego usar la funcion ;range'
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

# Ahora imprimo
for i in elements:
    print "Element was: %d" % i
