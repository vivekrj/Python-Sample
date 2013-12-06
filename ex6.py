x = "There are %d fruits." % 20
apple = "8"
orange = "12"
y = "There is totally %s apples and %s oranges." % (apple,orange)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e