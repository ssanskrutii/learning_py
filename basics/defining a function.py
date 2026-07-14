#define(def)
"""
here i am gonna make a function hello which doesn't exist but will try
"""

"""
name = input("What's your name?")
hello()
print(name)
"""
#this will apperently give a error coz hello() is not a function
"""
def hello():
    print("hello")

name = input("What's your name?")
hello()
print(name)

now this code will show use the result but in quite weird manner like after hello it will
automatically go to next like so will se hello on one line and then the users input on other
"""

#why not we parameterize this lets tell the function hello() to the the users input like lets add a parameter
def hello(to):
    print("hello,", to)
#i've took 'to' as my parameter it can be anything for now its nice to say hello to whom so...
name = input("What's your name?")
hello(name)


#Default value like sep(i.e seperator) and end(i.e line ending)
"""
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name?")
hello(name)
"""
