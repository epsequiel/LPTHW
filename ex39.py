#! /usr/bin/python

# Ejercicio 39 pagina 133
# Inicio con los diccionarios

# Mapeo de estados con abreviaciones
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
}

# set de estados y algunas ciudades
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

# Agrego ciudades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print algunas ciudades
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# Print algunos estados
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Hacerlo ahora el estado y luego el dicc de ciudad
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Imprimir todas las abreviaciones de estados
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Imprimir todas las ciudades en el estado
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Ahora ambas al mismo tiempo
print '-' * 10
for state, abbrev in state.items():
    print "%s state is abbreviated %s and has city %s" % (
            state, abbrev, cities[abbrev])

# Obtener una abreviacion de manera segura si no se encuentra
print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Texas not in 'states'"

# Obtener una ciudad con un valor default
city = cities.get('TX', 'Does not exist')
print "The city for the state of 'TX' is: %s" % city

