# =========================================================================
#         FUNCTIONS THAT ARE IMPORTED TO 'REVIEW_2'
# =========================================================================
# STORING YOUR FUNCTIONS INTO MODULES
# -------------------------------------------------------------------------
# The function used in "1)Importing A Function"
def shoe_maker(size, *colors):
    """Simulating Making Shoes"""
    print("Making a size " + str(size) + ".With colorway:")
    for color in colors:
        print("-" + color.title())


# Explaining:
# 1)First we define a function called 'show_maker' with
# two parameters(size, *colors)
# 2)Then we create a docstring("""Simulating Making Shoes""") telling
# us what the function does.
# 3)Then we create a print statement using the parameter 'size'
# 3a)NOTE:REMEMBER YOU MUST CONVERT A NUMERICAL REPRESENTATION OF A NUMBER(12)
# INTO THE STRING REPRESENTATION OF A NUMBER;str(size);
# 4)Then we create a 'for loop' telling python to loop through
# all the arguments  stored in parameter color and  print them in this format:
# 4a) print("-" + color.title()).
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# IMPORTING CLASSES
# -------------------------------------------------------------------------
# NOTE:'
class Gun_maker:
    """Simulates a buying bullets For The Right Gun"""

    def __init__(self, caliber=""):
        """Initializing Attributes for the '__init__()' method"""
        self.caliber = caliber

    def right_ammo(self):
        """Asking users What Size Caliber They Have"""
        message = input("What size caliber is your gun?")
        if message == 40:
            self.caliber.append(message)
        elif message == 9:
            self.caliber.append(message)
        print("Serching....")

    def come_again(self):
        """Recommending custmors ammo to purchese"""
        if self.caliber == 40:
            print("We recomend you buy 'Remington 180 Grain Golden Saber'")
        elif self.caliber == 9:
            print("We recommend you buy 'Federal HST 124 Grain'")


# Explaining:
# 1)First we define the class Gun_maker the doctring under the class 'Gun_maker'
# tells you what this class will model;
# """Simulates a buying bullets For The Right Gun"""
# 2)Then we define the '__init__()' with two parameters
# 2a)'self' - which is mandatory so the other methods can have access to the attributes
# 2b)caliber - which tells python when we create a instance for this class(Gun_maker) we must
# provide paramter 'caliber' with an agrument(40 or 9).
# 2c)Then indented pieces of code:
# 2d)The docstring tells you what the '__init__()' method does
# 2e)self.caliber = caliber;Tells python to store the parameter '=caliber'
# into the attribute 'self.caliber' to be used in other methods.

# 3)Then we create a method called 'right_ammo' with one parameter 'self'
# so method 'right_ammo' can have access to the 'self.caliber' attribute.
# 3a)The indented pieces of code:
# 3b)"""Asking users What Size Caliber They Have"""; Is a docstring that tells
# you what this method does.
# 3c)message = input("What size caliber is your gun?");Tells python to create a
# a prompt using the input() function to ask the user What size caliber is your gun?
# and store the value back into variable 'message'
# 3d)if message == 40:;Tells python if the user input store in 'message'
# is equal to(==) '40' then add(self.caliber.append(message)) that
# value to attribute 'self.caliber'.
# 3e)elif message == 9:;Tells python if variable 'message' is equal to(==)
# '9' then add(self.caliber.append(message)) the value stored in 'message'
# to the attribute 'self.caliber'.
# print("Serching....");Simply tells python to print "Serching..." when one of
# conditions has been met in the if-elif statement.

# 4)Finilly we define method 'come_again' with one parameter 'self'
# so 'come_again' can have access to the attribute 'self.caliber'.
# 4a)"""Recommending custmors ammo to purchese""";is a docstring that
# tells  you what the method 'come_again 'does.
# 4b)if self.caliber == 40:;Tells python if attribute 'self.caliber'
# value is 40 then print out the recommend type of bullets.
# 4c)elif self.caliber == 9:;Tells python if the attribute 'self.caliber'
# value is equal to(==) '9' then print the statement telling the user
# what bullets is recommend for that caliber.
