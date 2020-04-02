print("==========================================")
print("  STORING YOUR FUNCTIONS IN MODULES")
print("==========================================")
# By using descriptive names for your functions,your main program
# will be much easir to follow.
# --------

# A Module - is a file ending in '.py' that contains the code you want to
#'import' into your program.

# A 'Import' Statement - Tells python to make the code in a module
# available in the currently running program.

# EX:
print("1)Importing All functions from module 'stored_functions':")
import stored_functions

stored_functions.shoe_maker(12, "blue", "green", "yellow")

# Explaining:

# 1)import stored_functions;The way we use the import function in this
# example we tell python all the functions stored in module 'stored_functions'
# give us access to them in 'review_2'.
# 2)stored_functions.shoe_maker;This is how you call functions;
# 2a)First you need to give the name of the module of where the function
# is stored(stored_functions)
# 2b) .shoe_maker;This tells python we are creating arguments for
# the show_maker function.
# -------------------------------------------------------------------------
# Importing Specific Functions
# -------------------------------------------------------------------------
# There are a few diffrent ways you can import a function:
# EX:from module_name import function_name

# You Can also import multiple specific functions:
# EX:from module_name import function_0,function_1,function_2,function_3
# --------------------------------------------------------------------------
# Giving A Function An Alias
# -------------------------------------------------------------------------
# Reasons On Why You Would Need To Use An Alias:
# 1)If the name of the function you're importing is conficting
# with a name in your module.
# 2)If the function Name is to long you can give it a nickname
# by creating an 'alias' for the functions name.
# EX:
from stored_functions import shoe_maker as sm

print("\n1a)Giving A Function An Alias When Importing:")
sm(16, "blue", "red")

# Explianing:
# 1)from stored_functions ;This tells pyhon to  give us access
# to the module 'stored_function'
# 1a)import shoe_maker as sm;This tells python with in the module
#'stored_functions' to import the function 'show_maker' with a
# nickname(as) 'sm'
# 2)We then call the function but instead of giving the original
# name('show_maker') of the function we use the nickname:
# 2a)'sm(16,'blue','red')'
# -------------------------------------------------------------------------
# Giving A Module An Alias
# -------------------------------------------------------------------------
# Giving a module an alias can help you call module's function's more quickly
# EX:
import stored_functions as s_f

print("\n1b)Giving A Module An Alias:")
s_f.shoe_maker(14, "red")

# -------------------------------------------------------------------------
# Importing All Functions In A Module
# -------------------------------------------------------------------------
# NOTE: You can tell python to import every function in a module by
# using the asterisk(*) operator.
# EX:
from stored_functions import *

print("\n1c)Importing All Functions In A Module:")
shoe_maker(20, "yellow", "pink")

# Explainging:
# 1)Since every function stored in 'stored_functions' is being
# imported all we need to do is give the 'function call'(shoe_maker())
# of the function you would like to using along with
# the arguements needed to make that function(shoe_maker) operate.

# NOTE:ALL IMPORT STATEMENTS SHOULD BE USED AT THE BEGINNING OF A FILE
# UNLESS USING COMMENTS TO EXPLAIN.
# =========================================================================
#                     INTRO TO CLASSES
print("==========================================")
print("           INTRO TO CLASSES")
print("==========================================")
# =========================================================================
# Definations:
# 1)Instantiation- The fact or act of producing an instance, example, or
# specific application of a general classification, principle, theory, etc.
# 2)Instance-a step, stage, or situation viewed as part of a process or
# series of events
# -------------------------------------------------------------------------
# A Class - defines the general behavior  that the whole category of objects
# can have.
# The process of making an object for a class is called 'instantiation'.

#'Instances' in a class is the information passed to the class from the
# call of the class.
# EX: example = class(info,info) <-----Instance of a class
# -------------------------------------------------------------------------
# NOTE:In this class we will be creating a 'dog' giving him/she a name
# age and the abilty to sit and roll over.
class Dog:
    """A Simple Attempt To Model A Dog"""

    def __init__(self, name, age):
        """Initialize 'name' and 'age' Attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulating a Dog Sitting"""
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        """Simulating A Dog Rolling Over"""
        print(self.name.title() + " rolled over!")


# Explaining:
# 1)First we define a class called 'Dog';capitalized letters refer
# to a class when defining one a program.
# 1a)The parenthese() in the class definition are empty because we are making
# this class from scratch.
# 2)Then we create a docstring decribing what the function does:
# 2a)"""A Simple Attempt To Model A Dog"""

# NOTE:EXPLAINING THE METHODS IN A CLASS
# NOTE: A Function in a class is called a Method.
# 3)The  '__init__()' method:
# 3a) This is a special method that python needs to intialize all the attributes
# that are used within the other methods for them to operate within the class 'Dog()'
# 3b)This method is made up of two trailing underscores(__) and two leading underscores(__)
# which helps python determine pythons default method names and your methods names
# to keep them from conflicting

# 3c)We then give the '__init__' method three parameters:
# 3d)self;This parameter must be include first when using the '__init__'
# method because it gives the other methods access to the class
# intialized attributes.
# NOTE:THE SELF PARAMETER PASS AUTOMACTICALLY SO WE DONT NEED
# TO PROVIDE A ARGUMENT WHEN CALLING THE CLASS 'Dog()'
# 3e)Parameters 'name' & 'age' act as they would in a normal function
# which means when we make a class call we need to provide agruments
# for the two parameters 'name' & 'age'

# 3f)The indented pieces of code:
# 3g)"""Initialize 'name' and 'age' Attributes""";This is docstring that tells
# you what the method '__init__' is doing.
# NOTE:ANY VARIABLE WITH THE PREFIX 'SELF' IS AVAVILABLE TO EVERY METHOD
# IN THE CLASS AND WE WILL ALSO BE ABLE TO ACCESS EACH VARIABLE THROUGH ANY
# INSTANCE CREATED FROM THIS CLASS.
# 3h)self.name = name;Tells python to take the  parameter 'name'
# and store it in the variable 'self.name'. same process for the 'age' parameter
# NOTE:VARIABLES THAT HAVE 'SELF' AS A PREFIX('self.name') ARE CALLED ATTRIBUTES.

# 4)The 'sit()' method:
# 4a)First we define a method called 'sit()' with one parameter:
# 4b)sit(self);The parameter 'self'tells python to give the method 'sit' access to
# to the attributes(self.name) in method '__init__'.
# 4c)The indented pieces of code:
# 4d)"""Simulating a Dog Sitting""";This a docstring that tells you what
# this method does.
# 4e) print(self.name.title() + " is now sitting!");This tells pyhton to create
# a print() statement when this mehtod is called. within the print statement we
# use the value stored in the attribute  'self.name' with the .title() method.
# -------------------------------------------------------------------------
# Making An Instance from Class
# -------------------------------------------------------------------------
# EX:
class Dog:
    """A Simple Attempt To Model A Dog"""

    #                  P#1   P#2                 P= parameter
    def __init__(self, name, age):
        """Initialize 'name' and 'age' Attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulating a Dog Sitting"""
        print("-" + self.name.title() + " is now sitting!")

    def roll_over(self):
        """Simulating A Dog Rolling Over"""
        print("-" + self.name.title() + " just rolled over!")


print("1)Calling The Class 'Dog':")
# variable = Class(arugment#1,agrument#2)
my_dog = Dog("q", 1)
my_dog.sit()
my_dog.roll_over()
# Explaining:
# 1)my_dog = Dog('q',1);When python reads the class call 'Dog('q',1)'
# stored in the variable 'my_dog'.Python sends the postional arguments('q',1) to the
# '__init__()' method to store into parameters 'name' and 'age'.
# 1a)NOTE:NOTICE HOW THE '__inti__method()' DOESN'T HAVE THE 'return'
# STATEMENT,BUT PYTHON AUTOMATICALLY RETURNS AN INSTANCE OF THE CLASS
# BACK TO THE CLASS CALL LINE.
# 2)my_dog.sit();Tells python to take the 'instance' of the class 'Dog'
# stored in variable(my_dog) and apply the values(self.name.title())
# needed to make this method work.
# 3)my_dog.roll_over();Takes the same process as 'my_dog.sit()'
# -------------------------------------------------------------------------
# Accessing Attributes
# -------------------------------------------------------------------------
# To access the attributes of an instance you simple use the name of
# the instance(my_dog) and the attribute(.name) you need from there.
# EX:
print("\n1b)Accessing Attributes From The Instance Of The 'Dog' Class:")
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")

# Explaining:
# 1)my_dog.name.title();This peice of code in the first print() statement
# tells python in the instance of the 'Dog' class(my_dog) get the
# value 'Q' from the 'name' attribute stored in the class 'Dog'.

# 1a)str(my_dog.age);Tells python in the instance 'my_dog' get the  value(1)  from the age attribute
# stored in the class 'Dog' and convert the numerical representation of the number 1
# into the string representation(str()) of the number '1' and use it in the print() statement
# -------------------------------------------------------------------------
# Modifying The Attributes Of An Instance
# -------------------------------------------------------------------------
# This class will store infromation about the kind of car we're working with
# and it will have a method that summerizes this infromation.
# EX:
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()


print("\n1c)Modifying The Attributes Of An Instance:")
best_car = Car("bmw", "m8", 2020)
print(best_car.descriptive_info())

# Explainging:
# 1)First we define a class called 'Car';class Car():;
# 1a)"""A Simple Attempt To Represent A car.""";A docstring that tells you
# what the class(Car) does.
# NOTE:THE __init__() METHOD:
# 2)def __init__(self,make,model,year):;Tells python to define the '__init__()' method
# with 4 parameters(self,make,model,year).
# NOTE:REMEMEBER THE 'self' PARAMETER IS USED TO GIVE THE REST OF THE
# METHODS ACCESS TO THE ATTRIBUTES STORED IN THE '__init__()' METHOD
# SO THE 'self' PARAMETER MUST BE THERE FIRST WHEN DEFINING THE '__init__()' METHOD.
# 3)The indented pieces of code:
# 3a)"""Initialize attributes to describe a car.""";This is a docstring that tells
# you what the '__init__()' method is doing.
# 3b)self.make = make;Tells python to store the 'name' parameter into the variable
# 'make' and give access(self) to the rest of the methods.
# 3c)self.model = model;Tells python to store the model parameter into the variable
# model and give it access(self) to the other method in this class(Car).
# 3d)self.year = year;Tells python to store the parameter 'year' into the variable
# 'year' and give access(self) to the other method in this class(Car)
# NOTE:THE 'descriptive_info' METHOD:
# 1)First we define a method called(descriptive_info) with one parameter 'self' to
# to give this method access to the attributes in the '__init__()' method.
# 2)"""Return A Neatly Formatted Descriptive Name""";This is a docstring tell you
# what this method does.
# 3)details = str(self.year) + ' ' + self.make + ' ' + self.model;This tells
# python to store this format of the attributes from the '__init__()' method
# into the variable details.
# 4)return details.title();Tells python to return the format stored in the
# variable 'details' back to the call line using the  arguments given when creating the instance
# as values for those parameter('self.year','self.make','self.module').
# NOTE:CREATING A INSTANCE FOR THE CLASS 'Car':
# 5)best_car = Car('bmw','m8',2020);Tells python to create an instance of
# the class'Car' and store the arguments('bmw','m8',2020) into
# parameters(make,model,year)
# 6)print(best_car.descriptive_info());Tells python to use the
# instance of the 'Car' class 'best_car' in method 'descriptive_info()'
# and print out the outcome.
# -------------------------------------------------------------------------
# Giving A Default Value As A Attribute
# -------------------------------------------------------------------------
# NOTE:EVERY ATTRIBUTE IN A CLASS NEEDS AN INITIAL VALUE,EVEN IF THAT VALUE
# IS 0 OR AN EMPTY STRING.

# EX:Adding An Attribute And A New Method To The Class 'Car'
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default Value as a attribute.

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()

    def odometer_reading(self):
        """Print Statement Showing The Car Mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")


print("\n1c)Modifying The Attributes Of An Instance:")
best_car = Car("bmw", "m8", 2020)
best_car.odometer_reading()
# Explaining:The New Attribute(odometer) And Method(odometer_reading)
# 1)self.odometer = 0 ;This peice of code with in the '__init__()' method
# tells python to add new(odometer) attribute with a default value of '0'
# to the class 'Car'.
# 2)def odometer_reading(self):;This method(odometer_reading) has one
# parameter 'self' which tells python to give this method access to
# the attributes in the '__init__()' method.
# 2a)The indented peices of code:
# 2b)"""Print Statement Showing The Car Mileage""";Is a docstring that
# tells you what this method(odometer_reading) does.
# 2c)str(self.odometer);Tells python to convert the value of the attribute 'odometer '
# from the numerical representation(0) to the string representation('0') and format
# it the way it is in the print() statement.
# 3)Creating a instance:
# 3a)best_car = Car("bmw", "m8", 2020);Tells python to send arguments("bmw", "m8", 2020) to
# parameters(make, model, year) inside the 'Car' class then store that
# instance into variable 'best_car'
# 3b)best_car.odometer_reading();This puts the instance of class 'Car'  through the
# method 'odometer_reading' and then returns the format stored in the print() statement:
# 3c)"This car has " + str(self.odometer) + " miles on it.";
# -------------------------------------------------------------------------
print("------------------------------------------")
# Modifying Attributes Directly & Through A Method OR INCREMENT THE VALUE
# -------------------------------------------------------------------------
# NOTE:YOU CAN CHANGE AN ATTRIBUTE'S VALUE IN THREE WAYS:

# 1)Modifying An Attribute's Value Directly:
# EX:
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default Value as a attribute.

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()

    def odometer_reading(self):
        """Print Statement Showing The Car Mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")


print("\n2)Modifying The Attributes Of An Instance Directly:")
best_car = Car("bmw", "m8", 2020)
best_car.odometer = 23  # Modifying the attribute 'self.odometer' default value.
best_car.odometer_reading()
# Explaining:
# 1a)best_car.odometer=23;Tells python to change the old defualt value(0)
# for parameter 'odometer' to 23 in instance 'best_car' for class 'Car'
# 1b) best_car.odometer_reading();Tells python to take the instance 'best_car'
# for the class 'Car'and send it through method 'odometer_reading()' to format
# the new value(23) in paramter 'odometer'.
# 1c)"This car has " + str(self.odometer) + " miles on it.".
# -------------------------------------------------------------------------

# 2)Modifying An Attribute's Value Through A Method:

# NOTE:You can pass the new value to a method that handles the updating internally.
# EX:
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default Value as a attribute.

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()

    def odometer_reading(self):
        """Print Statement Showing The Car Mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_reading(self, mileage):
        """Set The Odometer reading to a given value
        And Reject if the agrument if its less then the original."""
        if mileage > self.odometer:
            self.odometer = mileage  # <----The New Default Value
        else:
            print("You cant roll back an odometer!")


print("\n2a)Modifying An Attribute's Value Through A Method:")
best_car = Car("bmw", "m8", 2020)
print(best_car.descriptive_info())

print("\n-Old Reading:")
best_car.odometer_reading()

best_car.update_reading(25)
print("\n-New Reading:")
best_car.odometer_reading()

print("\n-Using The 'Else Block' In 'update_reading' Method:")
best_car.update_reading(12)

# Explaining:
# 1)First we add a new method 'update_reading'  and give this method two parameters:
# 1a)'self';Which gives the method 'update_reading' access to the attribute's
# stored in the '__init__()' method.
# 1b)milage;Tells python when this method(update_reading) is called we need
# to provide a argument(25) for the parameter 'mileage'.
# 2)The indented pieces of code:
# 2a)The docstring tells you what the method is doing.
# 2b)if mileage > self.odometer:;Tells python if mileage value is greater then > the
# value already stored in the attribute 'self.odometer' then store the new value
# from the parameter 'mileage' onto the attribute 'self.odometer'.;self.odometer = mileage;
# 2c)else:;The else block  simply tells python if the  parameter 'mileage' is less
# Then the '__init__()' methods  attribute 'self.odometer' then print the statement;
# "You cant roll back an odometer!".

# NOTE:Calling The Methods 'update_reading()' and 'odometer_reading()':
# 3)best_car.update_reading(25);Tells python to take the instance(best_car)
# of the class 'Car' call the method 'update_reading' and provide it a
# new value the argument '25'.
# 3a)best_car.odometer_reading();Tells python to call the method 'odometer_reading'
# and send the instance(best_car) of the 'Car' class through the method 'odometer_reading'.
# Which in return shows you the new value.
# 3b)best_car.update_reading(12);Tells python to call the method 'update_reading'
# and send the instance(best_car) of the 'Car' class through the
# method 'update_reading' but this time shows you what happens when
# you put in a value(12) thats less then the pervious value(25) stored
# in the instance(best_car) of 'Car'; The else block;"You cant roll back an odometer!";
# -------------------------------------------------------------------------
# Incrementing An Attribute
# -------------------------------------------------------------------------
# Defintion:
# Increment-To increase the value of something by 1 or any other number
# you choose.
# -------------------------------------------------------------------------
# Sometimes you'll want to increment an attribute's value by a certain
# amount rather than  set an entirely new value.

# EX:This method allows us to increment an amount
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default Value as a attribute.

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()

    def odometer_reading(self):
        """Print Statement Showing The Car Mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_reading(self, mileage):
        """Set The Odometer reading to a given value
        And Reject if the agrument if its less then the original."""
        if mileage > self.odometer:
            self.odometer = mileage  # <----The New Default Value
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        """Adding The Given Amount To The Odometer."""
        self.odometer += miles


print("\n2b)Incrementing A Value Though A Method:")
used_car = Car("ford", "Gt", "2012")
print(used_car.descriptive_info())
print("\n-The Old Value For Attribute 'self.odometer':")
used_car.update_reading(12)
used_car.odometer_reading()
print("\n-The New Value For Attribute 'self.odometer':")
used_car.increment_odometer(35)
used_car.odometer_reading()

# Explaining:
# 1)def increment_odometer(self, miles):;First we define a new
# method 'increment_odometer' with two parameters:
# 1a)'self' - which gives the method 'increment_odometer()' access
# to the attributes stored in the '__init__()' method.
# 1b)miles;This parameter stores the argument(35) given from the
# method call.
# 2)The indented peices of code:
# 2a)"""Adding The Given Amount To The Odometer.""";Tells you what
# the method does.
# 2b)self.odometer += miles;Tells python to add the value of 'miles'
# to the value stored in the attribute 'self.odometer' from the
# '__init__()' method.
# NOTE:Creating A Instance Of 'Car' and Calling The New Method
# Creating Instance Of 'Car':
# 3)used_car = Car("ford", "Gt", "2012");Tells python to take
# three postional arguments '("ford", "Gt", "2012")' and store them
# in the parameters 'make, model, year' from the '__init__()' method
# then store that instance back into the variable 'used_car'.
# Calling The New Method:
# 3a)used_car.increment_odometer(35);Tells python to take the value
# for the 'self.odometer' attribute in the '__init__()' and
# pass it through the 'increment_odometer' method so '35' can
# be added(self.odometer += miles) to the value in 'self.odometer'.
# 4)Finally we see whats the new value for 'self.odometer' attribute
# =========================================================================
#                       INTRO TO INHERITANCE
print("==========================================")
print("          INTO TO INHERITANCE")
print("==========================================")
# =========================================================================
# definitions:
# Inheritance-The act of inheriting property
# -------------------------------------------------------------------------
# When one class inherits from another, it automatcally takes all the attributes
# and methods of the first class.
# NOTE:
# The 'Parent Class' - is the original class when inheriting

# The 'Child Class' - is the class that has all the attributes and methods
# from the 'parent class'

# The super() function - That helps python make the connection between the parent and the child
# class,
# EX:Creating a child class called 'Electric Car' inheriting from the 'Car' class
class Car:
    """A Simple Attempt To Represent A car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # Default Value as a attribute.

    def descriptive_info(self):
        """Return A Neatly Formatted Descriptive Name"""
        details = str(self.year) + " " + self.make + " " + self.model
        return details.title()

    def odometer_reading(self):
        """Print Statement Showing The Car Mileage"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_reading(self, mileage):
        """Set The Odometer reading to a given value
        And Reject if the agrument if its less then the original."""
        if mileage > self.odometer:
            self.odometer = mileage  # <----The New Default Value
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        """Adding The Given Amount To The Odometer."""
        self.odometer += miles


class ElectricCar(Car):
    """Representing aspects of a car,specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initializing Attributes Of The Parent Class 'Car'"""
        super().__init__(make, model, year)


print("1)Using The Child Class 'ElectricCar':")
flash_car = ElectricCar("telsa", "model s", 2016)
print("-" + flash_car.descriptive_info())

# Explaining:
# NOTE:WHEN YOU CREATE A CHILD CLASS YOU MUST HAVE THE PARENT CLASS(Car)
# WITH IN THE SAME FILE  AND BEFORE THE CHILD CLASS(ElectricCar)

# 1)class ElectricCar(Car):;Tells python to define a new class named
#'ElectricCar' with one parameter 'Car'which is the class 'Car'
# 1a)The parameter 'Car'; Tells python to to store the class 'Car' into
# the class 'ElectricCar'
# 1b)The docstring tells us what the class 'EletricCar' do.
# 2)Then we define the '__init__()' method with four
# parameters(self,make,model,year)
# 2a)The indented peices of code:
# 2b)The docstring tells you what the '__init__()' do.
# 2c)super().__init__(make,model,year):Tells python to let
# the child class 'ElectricCar' have access(super().) to the attributes 'make,model,year' in
# the parent class 'Car'
# NOTE:Calling The Child Class 'ElectricCar':
# 3)flash_car = ElectricCar('telsa','model s',2016);Tells python to create a
# instance of the class 'ElectricCar' with the arguments('telsa','model s',2016)
# and store the instance into variable 'flash_car'.
# 3a)print('-' + flash_car.descriptive_info());Tells python to
# pass the instance(flash_car) through the method 'descriptive_info'
# and return back to the call line(print()) with a dash(-) behind it.
# -------------------------------------------------------------------------
# Defining Attributes And Methods For The Child Class
# -------------------------------------------------------------------------
# EX:
class ElectricCar(Car):
    """Representing aspects of a car,specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initializing Attributes Of The Parent Class 'Car'"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def battery_info(self):
        """Generating Battery info based off the 'self.battery_size' value"""
        print("-This cars battery is a " + str(self.battery_size) + "kWh battery.")


print("\n1a)Using The 'battery_info' Method from 'ElectricCar' class:")
flash_car = ElectricCar("telsa", "model s", 2016)
print("-" + flash_car.descriptive_info())
flash_car.battery_info()
# Explaining:
# 1)First we define a method named 'battery_info' with the parameter 'self'
# so the method 'battery_info' can have access to the attributes stored
# in the '__init__()' method.
# 2)The indented pieces of code:
# 2a)Then we create a docstring explaining what the method 'battery_info' do
# 2b)str(self.battery_size) ;Tells python to convert the numerical reprentation
# of the value in attribute 'self.battery_size' to the string reprentation(str())
# NOTE:Calling the Method:
# flash_car.battery_info();Tells python to take the instnace of the child class 'EletricCar'
# and pass it through the method ''battery_info' which in return outputs
# a statement telling you what kind of battery you have.
# -------------------------------------------------------------------------
# Overriding Methods From The Parent Class
# -------------------------------------------------------------------------
# Say if theres a method in the parent class that you didnt want to use
# in your child class you can override that mathod from the parent class
# by rewriting the method form the parent class inside the child class
# EX:
# class Car():
#       --snip--
#   def fill_gas(self)
#        """This Method tells you to fill the gas tank"""
#          print("FILL GAS!!!")
# class ElectricCar(Car):
#       --snip--
#   def fill_gas(self):
#          """This Method tells you to fill the gas tank"""
#             print("Electric Cars Dont Take Gas!")
# Explaining:
# 1)This example explains that the method(fill_gas) in the parent class 'Car'
# is not needed in the child class 'ElectricCar' so we rewrite the method
#'fill_gas' in the child class 'ElectricCar'  so when someone uses the
# child class 'ElectricCar' with method 'fill_gas' they get a print() statement
# telling users;"Electric Cars Dont Take Gas!".
# -------------------------------------------------------------------------
# Creating A Class for just Handling The battery
# -------------------------------------------------------------------------
# In this situation we could point out, what more we can do to provide more
# value to the user using our program to get there battery information.
# like tell them how far they can go depending on what kind of battery they have.
# EX:
class BatteryFile:
    """Tells you information about the battery"""

    def __init__(self, battery_size=70):
        """Initialize The Battery's Attributes"""
        self.battery_size = battery_size

    def battery_info(self):
        """Printing The Battery Size And How Far You Can Go."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "-This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Representing aspects of a car,specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initializing Attributes Of The Parent Class 'Car'"""
        super().__init__(make, model, year)
        self.battery_folder = BatteryFile()


print("\n1b)Using The Class 'BatteryFile' ")
flash_car = ElectricCar("telsa", "model s", 2016)
print("-" + flash_car.descriptive_info())
flash_car.battery_folder.battery_info()
# Explaining:
# 1)First we create a class called 'BatteryFile' then provide a docstring
# telling us what the class 'BatteryFile' do;
# """Tells you information about the battery"""

# 2)Then we define the '__init__()' method with 2 parameters
#'self' and 'battery_size' with a default value '=70'
# 2a)The indented pieces of code:
# """Initialize The Battery's Attributes""";Tells you what the
#'__init__()' method does.
# 2b)self.battery_size = battery_size;Tells python to store the parameter
#'battery_size' into attribute 'self.battery_size'.
# 3)We then define the method 'battery_info' with one parameter 'self'
# which gives the method 'battery_info' access(self) to the attributes
# stored in the '__init__()'.
# 3a)The indented pieces of code:
# 3b)"""Printing The Battery Size And How Far You Can Go.""";Is a
# docstring that tells you what the method 'battery_info' do.
# 3c)if self.battery_size == 70:;Tells python if the value stored
# in the attribute 'self.battery_size' is equal too(==) '70' then
# we create a new variable 'range' with a value of '240'.
# 3d)elif self.battery_size == 85:;Tells python if the attribute
# 'self.battery_size' from the' __init__()' method is equal too(==)
# '85' then we create a new variable 'range' with the value of '270'.
# 3e)Then we store a prompt into the variable 'message' to inform
# users how many miles they get on there type of battery.
# 4)Then we create a attribute for the '__init__()' in the child

# class 'ElectricCar(Car)':
# 4a)self.battery_folder = BatteryFile();Which Tells python to create
# a instance of the 'BatteryFile' class and store it in attribute,
#'self.battery_folder' with the defualt value '70'.
# NOTE: Calling The Class BatteryFile using the instance from 'flash_car'
# 5) flash_car.battery_folder.battery_info();Tells python to take
# the instance of the class'ElectricCar(Car)' stored in
# 'flash_car' and find the instance of class 'BatteryFile' stored in the
# attribute 'battery_folder' then pass the defualt value(battery_size=70)
# through the method 'battery_info' and since the matches  '70' then
# we create a variable called range and a value of 240 which will be used in the
# print statement stored in message.
# -------------------------------------------------------------------------
# Importing Classes
# -------------------------------------------------------------------------
print("-------------------------------------------")
print("2)Importing Classes:")
# Importing A Single Class
print("\n2a)Importing A Single Class:")
# EX:
from stored_functions import Gun_maker


person = Gun_maker(40)
person.right_ammo()
person.come_again()

# Explaining:
# 1)First we 'import' the class 'Gun_maker' from the
# module 'stored_functions'
# EX:from stored_functions import Gun_maker
# 2)Then we create a instance of the class 'Gun_maker'
# with arguemnt '40' for the parameter 'caliber' defined
# in the '__init__()' method and store it in variable 'person'
# 3)Then we call the Class:
# 3a)person.right_ammo();tells python to send the instance(person) and
# pass it through the method 'right_ammo' which stores the value(40)
# into the attribute 'self.caliber'
# 3b)person.come_again();tells python to send the instance(person) and
# pass it through the method 'come_again' which takes the value(40)
# and recommend which kind of bullets they should buy.
# -------------------------------------------------------------------------
# Importing Multiple Classes/Methods From A Module
# -------------------------------------------------------------------------
from stored_functions import shoe_maker, Gun_maker

print("\n2b)Importing Multiple Classes/Methods From A Module:")

# Using The shoe_maker Method:
print("\n-The 'shoe_maker' Method")
new_shoes = shoe_maker(12, "blue", "green", "purple")
print(new_shoes)

# Using The 'Gun_maker' Class:
print("\n-The 'Gun_maker' Class:")
gun = Gun_maker(9)
gun.right_ammo()
gun.come_again()
# -------------------------------------------------------------------------
# NOTE:OTHERS WAYS OF IMPORTING A CLASS
# 1)Importing An Entire Module:
# 1a)import stored_functions;Tells python to give you access to all the Class\Methods
# you need from that module
# 2)Importing All Class From A Module:
# 2a)from module_name import*;Tells python to give you access to all
# the classes in a module.
