"""
#Ask user their name
name = input("What's your name?")
#Removing the whitespaces in the users input
name = name.strip()
#Capitalizing the users input
name = name.capitalize()
[prefer title instead of capitalize so that it will capitalize all the words given in the input]
print(f"Hello, {name}")
"""

#TO MAKE THE CODE LOOK MORE CLEAN

name = input("What's your name?").strip().title()
print(f"Hello, {name}")

#In the output screen will see the all of the input given by the user but if I just want the first name like I just wanna say 'Hello, first name'
#first & last = name.split(" ")
#And then the code as it is...
