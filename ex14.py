#! /usr/bin/python

# Ejercicio 14 pag 50

from sys import argv

script, user_name = argv
prompt = '> '

# -------------------------------------------------------------------------------
# Esto no es parte del ejercicio, es solo practica personal
#
print "[*] Argv: %s, Cant elementos: %d" % (argv, len(argv))
for arg in argv:
    print "[*] Argv[%d] == %s" % (argv.index(arg), arg)
# -------------------------------------------------------------------------------

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r comuter. Nice.
""" % (likes, lives, computer)
