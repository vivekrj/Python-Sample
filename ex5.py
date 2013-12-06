my_name = 'Vivek'
my_age = 23 # not a lie
my_height = round(5.9) # inches
my_weight = 55 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Hi, my name is %s." % my_name
print "I am %d inches tall." % my_height
print "And  %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "I got %s eyes and %s hair." % (my_eyes, my_hair)
print "I'm %d yrs old" % my_age

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
	
	