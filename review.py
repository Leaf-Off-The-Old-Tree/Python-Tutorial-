# =========================================================================
#                         LEARNING PYTHON
# =========================================================================
#  Keys:
# (EX:)- example
# (op)-output
#  =========================================================================
#                INTRO TO STRINGS ,VARIABLES,METHODS.
print("         ***INTRO TO STRINGS,VARIABLES,METHODS.***")
print("           =========================================")
# =========================================================================
# A simple print statement:
# The print() statement tells python to produce the output onto your terminal window
# whatevers in between the paratheses():
print("1)A Simple print statement:")

# ------------------------------------------------------------------------
print("1a)Hello everyone ")
print("-----------------------------------------")
# ------------------------------------------------------------------------
# A simple Variable And Value:
# ------------------------------------------------------------------------
# Every variable holds a value that is information associated
# with that variable.
print("2)Printing A Variables Value:")
messagess = "2a) Hello world,I'm Kevin."
print(messagess)
# Explaining This Example:
# In this example the variable "messagess" is associated
# with the value;"Hello world!Im Kevin."; to see the value in teminal
# you just put the variable into the print statement.
# ------------------------------------------------------------------------
# Whats not allowed in the variable name:
# 1) Spaces instead use underscores(_).
# 2)Numbers cant come first when naming a variable.
# EX: message_1 not 1 message
# 3) Advoid using python keywords as variable names.
# EX: print,str()
# 4)Variable names should be short and descriptive.
# EX: 'name' is better then 'n', student_name is better then s_n.
# ------------------------------------------------------------------------
# Variable Rules.
# ------------------------------------------------------------------------
# Becareful using lowcase 'L' and uppercase O
# Could be confused for   '1' and '0'
# ------------------------------------------------------------------------
# Advioding names errors when using variables:
# ------------------------------------------------------------------------
# When a error occurs a traceback appears.
# Traceback - is a record of where the interpreter ran into
# trouble when trying to excute your code.
# ------------------------------------------------------------------------
# Ex:
# print(messagesss)
# ------------------------------------------------------------------------
# 1)First part tells us that a error occured on line 43
# 2)The second part,tells us what kind of error was found.
# EX: print(messagesss)
# 3)At the bottom of the traceback message it will tell you what
# went wrong.(Name error:)
# In this case the error is a misspelled variable name.(messagess)
# ------------------------------------------------------------------------
# Understanding What "Strings" Are.
# ------------------------------------------------------------------------
# strings are data types
# strings are a series of characters
# anything inside of a of quotes ("") or apostrophes ('').
# EX:
# 1)"This is a string "
# 2)'This is a string'
# ------------------------------------------------------------------------
# You can also us quotes and apostrophes togther:
# EX: 'I told my friend ,"Python is my favorite language."'
# ------------------------------------------------------------------------
# Understanding Methods.
print("------------------------------------------")
# ------------------------------------------------------------------------
# Method - is an action that python can perform on a piece of data.
# EX:
name = "ada lovace"
print("3)Using '.title()' Method To Capitalize The Begining Of Each Word:")
print("3a)" + name.title())
# ------------------------------------------------------------------------
print("------------------------------------------")
# Explaining the example:
# 1)The string "ada lovelace" is stored in variable 'name'"
# 2)The 'DOT'(.) after name in "name.title()" tells python to
# make the .title() method act on variable 'name'.
# 3)The ".title()" does not need additional info thats why the
# parentheses"()" are  empty.
# ------------------------------------------------------------------------
# Using ".upper()" and ".lower()" Methods
# ------------------------------------------------------------------------
# EX:
print("4)Varible 'name' using 4a).upper() and 4b).lower() Methods")
print("4a)" + name.upper())
print("4b)" + name.lower())
print("------------------------------------------")
# NOTE: '.lower()'  method is particularly used to store data*******
# ------------------------------------------------------------------------
# Combining/'Conatenating' Strings:
# -------------------------------------------------------------------------
# Conatenation - is the method of combing strings, python uses
# the '+' symbol to combine strings.
# ------------------------------------------------------------------------
# Creating a first_name and last_name variable then combining
# them to create a full_name variable:
# ------------------------------------------------------------------------
# 1)Start by creating the first name variable:
first_name = "ada"
# 2)We then create a variable for the last_name:
last_name = "lovelace"
# 3)We finally create a concatenation with in the variable 'full_name'
full_name = first_name + " " + last_name
# 4)Now we print full_name:
print("5)This Is Concatenating Two Variables output:")
print("5a)" + full_name)
# ------------------------------------------------------------------------
# You can use the variable 'full_name' to also make a message:
print("\n5b)Using The Concatenation('full_name') To Create A Message:")
print("5c):Hello people, my name is " + full_name.title() + ".")
# ------------------------------------------------------------------------
# We can also take the message in the print statement
# and store it in a variable(into):
intro = "Hello people, my name is " + full_name.title() + "."
print("\n5b)The same message as before, just using the name of the variable to print:")
print(intro)
# This is a easier way to reuse the message instead of printing the same thing over.
print("------------------------------------------")
# ------------------------------------------------------------------------
# Whitespaces,Tabs,and Newlines.
# ------------------------------------------------------------------------
# WhiteSpaces - are any non-printing characters
# EX: spaces,tabs and newlines
# ------------------------------------------------------------------------
# To add a tab to your text use \t:
print("6)Showing How Tab Looks Being Used:")
print("6a)Without Tab:")
print("python")
print("6b)With Tab: ")
print("\tpython")
# ------------------------------------------------------------------------
# Now lets us \n to create newlines:
print("\n6c)Creating A New Line:")
print("6d)favorite cars:\n-Lambo\n-Kia\n-Tesla ")
# ------------------------------------------------------------------------
# Now we are going to explain striping the whitespaces:
# "Python" vs " Python"
# The extra whitespaces are detected by python and
# makes the two words in the strings two different things.
# ------------------------------------------------------------------------
# '.rstrip()' method -  gets rid of the white spaces on
# the right side.
# '.lstrip()' method -  removes white spaces on the leftside
# '.strip()' method - removes whitespaces from the both sides
# ------------------------------------------------------------------------
# The '.strip()' method is temporary, so you MUST put into
# variable to make permanet.
# EX:
# favorite_language = "python "
# favorite_language = favorite_language.strip
# print(favorite_language)
# ------------------------------------------------------------------------
# Understanding Some Errors Involing Strings
# ------------------------------------------------------------------------
# Syntax errors occurs when python doesn't recongize a
# section of your program as valid python code.
# EX: Using a apostrophe within a single quote:
# Q = 'One of my favorite book's are crash course.'
# print(Q)
# ------------------------------------------------------------------------
# If a apostrophe('') is used within single quotes its hard,
# for python to determine where the string ends.
# So you get a "syntax error:invalid syntax"
# ------------------------------------------------------------------------
# NOTE:
# Make sure you use double quotes("") if you want to use
# single quotes('') within a statement
# ------------------------------------------------------------------------
# Using Numbers In Python.
# ------------------------------------------------------------------------
# The common signs in math is the same in python:
# 1)Additon "+"
# 2)Subtraction "-"
# 3)Multipling "*"
# 4)Division "/"
# 5)Exponents "**"
# ------------------------------------------------------------------------
print("------------------------------------------")
# Floats are any number with a decimal point:
# EX:
print("7)Showing You What A 'Float' Looks Like: ")
print(0.2 + 0.1)
# ------------------------------------------------------------------------
print("------------------------------------------")
# Avioding Type Errors With The 'Str()' Function
# ------------------------------------------------------------------------
# 'str()' function- converts non-string values into strings.
# An example of when you should use the str() function :
# THE ERROR:
age = 23
# messages = "Happy " + age + "rd Birthday!"
# print(messages)
# creates a tracback with a TypeError: can only concatenate
# str(not 'int') to str
# The "int" in this traceback stands for interger
# so basically you cant add a string and a number in a concatention(+).
# Which is why a interger must be converted to a string('str()').
# ------------------------------------------------------------------------
# Correct way:
messages = "Happy " + str(age) + "rd Birthday!"
print("8)This Is The Output Of Converting A Numerical value into a str():")
print("8a)" + messages)
# =========================================================================
#                           INTRO TO LIST
print("==========================================")
print("               INTRO TO LIST")
print("==========================================")
# =========================================================================
# list- are a collection of items in a particular order.
# The way a list is set up :   (name = ['Kevin','bro'])
# ------------------------------------------------------------------------
# NOTE:ALWAYS REMEMBER:
# PYTHON CONSIDERS THE FIRST ITEM IN THE LIST AS 0!
# IF YOUR GETTING UNEXPECTED RESULTS CONSIDER THE
# OFF-BY-ONE ERROR.
# ------------------------------------------------------------------------
# A simple list:
#         0        1        2     3     <------------Order of the list.
cars = ["Ford", "Lambo", "Kia", "Chevy"]
print("1)A Simple List: ")
print(cars)
# Explaining:
# 1)First we create a variable(cars) to store the elements("ford")
# in the list(cars).
# 2)The  square brackets '[]' tells python that your storing elements
# into the list.
# 3)The elements are peices of infromation stored in a list:
# 3a)"Ford", "Lambo", "Kia", "Chevy".
# 4)We then print the list(cars);print(cars).
# ------------------------------------------------------------------------
# Assessing Elements In A List.
# ------------------------------------------------------------------------
# EX:
print("\n1a)Assessing The '3rd' Element '[2]' In List 'cars' :")
print("-" + cars[2])
# Explaining:
# 1)Seeing how python starts off the count of a list at 0,if we
# wanted to see the 3rd item in the list we would have to print the
# second item in the list; 'cars[2]'.
# NOTE:REMEMBER THE OFF-BY-ONE ERROR WHEN WORKING WITH LIST!!!
# ------------------------------------------------------------------------
# Accessing The 'Last' Element In A List.
print("\n1b)Accessing The Last[-1] Wlement In The List 'cars'.")
print("-" + cars[-1])
# You can us the negative "-" symbol on a number'[-1]'
# and get the last item in the list.
# 'cars[-2]' to get the 2nd item from the end of the list and so on.
# ------------------------------------------------------------------------
# You can use concatenation to create a message with a specific element:
# EX:
simple = "I like the " + cars[1] + " the most."
print("\n1c)Using  Conctenation To Create A Message With A Specify Element: ")
print("-" + simple)
# Explaining:
# 1)First we create a variable(simple) to store a sentence using the
#  second element in the list(cars[1])
# 2)Then we use the print statement to style our output(print("-" + simple))
print("------------------------------------------")
# ------------------------------------------------------------------------
# Modifying Elements In A List.
# -------------------------------------------------------------------------
# NOTE:YOU CAN CHANGE THE LIST ELEMENTS IF YOU DOWNLOAD THE FILE***********
# EX:
life = [
    "money",
    "weed",
    "sex",
    "cars",
]
print("2)An Example Of Modifying A Element In A List:")
print("\n2a)Before Modifying")
print(life)
life[0] = "cash"
print("\n2b)After Modifying Elements:")
print(life)
# Explaining:
# 1)First we create a list(life) with 4 elements in it
# 2)'print(life)';We then tell python to print the original
# order of the list
# 3)life[0] = "cash";This tells python for the list 'life' put
# the element 'cash' at the begining '[0]' of the list(life) in place
# of the original element('money').NOTE:THIS IS MODIFYING('CASH') A ELEMENT('MONEY').
# 4)Then we reprint the list(life) to compare the differences between
# the changes.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Appending An Item To A List
# -------------------------------------------------------------------------
# ".append()" method - adds a new element to the end of a list.
# EX:
life.append("love")
print("\n5)Adding A New Values To The End Of The List Using The Append() Method")
print(life)
# Explaining:
# 1)Using the perivous list(life) we will we add the element 'love'
# to the end of the list(life);life.append("love");
# 2)Then we print show the results of appending a item.
# -----------------------------------------
# Adding items to a empty list:
# EX:
print("\n5a)This Is The Print Output Of A Empty List:")
empty = []
print(empty)
print("5b)Adding Three Elements To List 'empty':")
empty.append("johnnie")
empty.append("cruz")
empty.append("whois")
print(empty)
# explaining:
# 1)First we create a empty list called 'empty'
# 2)Then we add three elements 'johnnie','cruz',and 'whois'
# 3)Now we print the list to show you that the list is not empty anymore.
# 3a)print(empty)
print("------------------------------------------")
# ---------------------------------------------------------------------
# The insert method - is used when you want to put in a item in a specify place.
life.insert(2, "thoughts")
print("6)Using The 'Insert()' Method To Put A Value In A Specific Place:")
print(life)
# Explaining:
# 1)Using the perivous list(life) we insert a new element 'thoughts' into the
# list at the 3rd position in the list(insert(2, "thoughts"))
# NOTE:REMEMBER WHEN WORKING WITH LIST THE POSITIONS OF THE ELEMENTS
# STARTS AT 0.SO IF YOU WANTED THE 3RD ITEM YOU WOULD ASK FOR THE 2ND ITEM*****
# ------------------------------------------------------------------------
print("------------------------------------------")
# REMOVING ELEMENTS IN A LIST
# ------------------------------------------------------------------------
# Deleting A Element:
# EX:
life.append("crack")
print("7)Without The Delete(del) statement:")
print(life)
del life[-1]
print("\n7a)Deleting crack from variable life:")
print(life)
# Explaining:
# 1)Using the perivous example list(life) we add a new element(crack) to the end
# of the list(life).
# 2)print(life);Now we print the list to show that the new element(crack) is in
# the list.
# 3)del life[-1];Tells python to delete('del') the last(.append) item in the list 'life'.
# 4)Then we reprint the list(life) to show you that the element(crack) was deleted.
# ------------------------------------------------------------------------
# Using The '.pop()' Method To Remove Elements.
print("------------------------------------------")
# ------------------------------------------------------------------------
# The pop() method -removes the last item  in a list by default, but lets you still work
# with the element after removing it.
# EX:
motorcycles = ["honda", "bmw", "yamaha", "suzuki"]
print("8)The Original List")
print(motorcycles)
popped_bikes = motorcycles.pop()
print("\n8a)Showing You Which Item 'pop()' Method Took:")
print(popped_bikes)
# Explaining:
# 1)First we create a list of 'motorcycles' with the name of the
# bikes as elements in the list(motorcycles)
# 2)Then we print the original list to show you all the elements
# in the list;print(motorcycles).
# 3)popped_bikes = motorcycles.pop();Tells python to create variable 'popped_bikes' to
# store the last(pop()) item('suzuki') in the list 'motorcycles'.
# 4)Finally we print the variable 'popped_bikes' to show you which item
# was removed from the list 'motorcycles';print(popped_bikes).
# ------------------------------------------------------------------------
# You Can Also 'pop()' Items From Any Position In A List
# EX:
favorite_bike = motorcycles.pop(1)
print(
    "\n8b)Using 'pop()' Method To Get A Item From A Specific Place And Making A Sentence:"
)
print("-My favorite bike was a " + favorite_bike.title() + ".I just loved it!")
# Explaining:
# 1)we create a variable called 'favorite_bike' and store the removed(pop())
# item(bmw) from the 2nd'(1)' position in the list 'motorcycles'.
# 2)Then we create a print statement using the variable 'favorite_bike'
# with the title() method;'+ favorite_bike.title() +' .
print("----------------------------------------------------")
# ------------------------------------------------------------------------
# Using The Remove() Method
# ------------------------------------------------------------------------
# You can use the '.remove()' method to get rid of a item by name.
# EX:
candy = ["reeses", "herseys", "kit-kat"]
print("\n9)The original list:")
print(candy)
print("\n9a)Using the remove() method: ")
candy.remove("herseys")
print(candy)
# Explaining:
# 1)First we create a list(candy) and store three elements into the list
# 2)We then print the original list;print(candy).
# 3)candy.remove("herseys");This tells python to remove the element 'Herseys'
# from the list(candy)
# Finally we reprint the list to show that the element 'Herseys' was removed.
# ------------------------------------------------------------------------
# The remove method only deletes the first occurence
# of the value('herseys')
# Which we will elaborate on later  about how to delete multiply items at once.
# ------------------------------------------------------------------------
print("------------------------------------------")
# Using The Sort() Method
# ------------------------------------------------------------------------
# Sort() method - lets you change the order of the list to alphbetical order.
# EX:
games = ["nba 2k", "gta", "red dead"]
print("10) The Original List:")
print(games)
print("\n10a) The Same List Of Games But In Alphbetical Order:")
games.sort()
print(games)
# Explaining:
# 1)First We Create a list(games) of elements.
# 2)then we show the list before sorted;print(games)
# 3)games.sort();Tells python to put all the elements in the list 'games'
# in alphbetical order(.sort).
# 4)Finally we print the new sorted list to compare the differences.
# ----------------------------------------------------------------------
# The sort() method changes the order of list permanently.
# You can also put it in reverse alphbetical order.
# With "reverse = True"
# EX:
print("\n10b) The List Of Games In Reverse Alphbetical Order:")
games.sort(reverse=True)
print(games)
# explaining 'games.sort(reverse=True)':
# 1)Basically here we are telling python the elements in list
#'games' put in alphbetical order(sort) but switch reverse from 'False'
# to  equal(=) 'True'.
# -----------------------------------------------------------------------
print("------------------------------------------")
# Using the Sorted() function
# -----------------------------------------------------------------------
# 'sorted()' function lets you put the list in alphbetical order but is not permanent.
# You can also do reverse = True
# EX:
print("11) The Orginal List Of Games:")
print(games)
print("\n11a) Using The Sorted() Function:")
print(sorted(games))  # sorted Method
print("\n11b) Back To The Orginal List:")
print(games)
# ------------------------------------------------------------------------
# The Reverse() Method
# ------------------------------------------------------------------------
# The reverse() Method just reverses the orginal order in the list
# ("does not put in alphbetical order")
# The reverse() method changes order permanently, to change
# the order back just apply the 'reverse()' method to the
# list again.
# EX:
test = ["test_1", "test_2"]
print("\n12) The original list test :")
print(test)
print("\n12a) The reverse() order of test")
test.reverse()  # reverse() method
print(test)
# --------------------------------------------------------------------------
print("------------------------------------------")
# Using The 'len()' Function.
# -------------------------------------------------------------------------
# The len() function finds the length of the list.
# EX:
print("\n13)Showing you how many items are in the list test:")
print(len(test))
# ------------------------------------------------------------------------
print("------------------------------------------")
# Advoiding Index Errors When Working With List.
# ------------------------------------------------------------------------
# When forgeting about the 'off-by-one' error:
# remember python considers the list count to start at 0 for the
# first item in a list instead of 1.
# -----------------------------------------------------------------------
# You can get a traceback that tells you the item you're
# asking for is out of range which means that the list does not
# contain that many items .
# EX:test = ["test_1", "test_2"]:
# print(test[2])
# The actual name for the error is:
# index error:list index is out of range.
# You can also get this error if the list is empty.
# =========================================================================
#              INRO TO 'FOR-LOOPING' WITH LIST
print("==========================================")
print("    INTRO TO 'LOOPING' THROUGH A LIST ")
print("==========================================")
# =========================================================================
# Looping allows you to take the same action or set
# of actions and use them for every item in the list
# EX:A 'for loop'
# The for loop will help get every name from the list
# and print them one by one, instead of accessing them
# one by one.
hobbies = ["programming", "basketball", "video games"]
print("1)Using A 'for loop ' To Print Every Item In List:")
for hobby in hobbies:
    print("-" + hobby.title())
print("My favorite is " + hobbies[0] + ".")
# -------------------------------------------------------------
# Explaining example:
# 1) We create a list of items to use in our 'for loop'
# 2) We then create the for loop:
# 2a)You must start with the word 'for' to let python know your starting a 'for loop'
# 2b)You must then create a temporary variable(hobby) to store the indented pieces of code in.
# 2c)The 'for loop' also tells python that the indented pieces of code will be acting
# on whats stored in the main variable("hobbies")
# 3)The 'for loop' then tells python that you would like to print each item
# in 'hobbies' with a "-" behide it and with the .title() method.
# NOTE:You can add as many pieces of indented code as you want,
# Any unindented piece of code after the loop only show once.***********
# ------------------------------------------------------------------------
# Advioding Indentation Errors.
# ------------------------------------------------------------------------
# Forgetting to indent
# EX:
# hobbies = ['programming','basketball','video games']
# for hobby in hobbies:
# print("-" + hobby)
# ------------------------------------------------------------------------
# NOTE:Always rememeber to indent the next line  when creating a 'for loop'
# or you get error:
# -traceback:indentation error:expected and indented block.
# ------------------------------------------------------------------------
# NOTE:
# If your program runs, but does not produce the right
# results then that is called a 'logical error'.
# -----------------------------------------------------------------------
# Another indentation error is caused by unnecessarily indenting.
# EX:
# message = "Hi, im kevin."
#   print(message)
# EX of error:indentation error:unexpected indent.
# -----------------------------------------------------------------------
# NOTE THAT AFTER EVER LOOP THERE SHOULD BE A
# COLON ':'.YOU WILL GET AN ERROR.
# EX:
# mange = ['crazy','loop']
# for manage in mange
#    print(manage)
# the error you will get;SyntaxError: invalid syntax.
# -----------------------------------------------------------------------
# Making A Numerical list
# ------------------------------------------------------------------------
# Using The Range() Fucntion
# ----------------------------------------------------------------------
#  'range()' function-makes it easy to generate a series of numbers.
# EX:
print("------------------------------------------")
print("2)Using The Range() Function To Create A Series Of Numbers:")
for value in range(1, 5):
    print(value)
# NOTE:This is a another good example of off-by-one error
# because when python prints out the range it shows
# "1-4"
# ------------------------------------------------------------------------
# list() function-converts a range of numbers into list a format.
# EX:printing a range of numbers in a list format.
cool = list(range(1, 7))
print("\n2a)Converting A Range Of Numbers Into A List.")
print(cool)
# -------------------------------------------------------------------------
# Using range() function to print out only even numbers.
# EX:
positive_numbers = list(range(2, 11, 2))
print("\n2b)Using The Range() Function To Print Only Even Numbers:")
print(positive_numbers)
# Explaining:
# 1)The first number(2) is where the list starts with the range of numbers.
# 2)The second number(11) tells python where to end the range of numbers.
# 3)The last number(2) adds 2 to the first number then,
# ever other number after that until it reachs 11 or in this case
# stops at 10.
# ------------------------------------------------------------------------
# Using A For Loop With The Range() Function.
print("------------------------------------------")
# ------------------------------------------------------------------------
# We will be showing you how to print squared numbers in a loop.
# EX:
squares = []
print("3)Using A 'for loop' To Create Values Squared:")
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# Explaining:
# 1)First we create a for-loop with a range of numbers from
# '1-11'
# 2)The indented pieces of code:
# 2a)square = value ** 2;Tells python to store all the squared numbers
# '1-11' into the variable 'square'.
# 2b)squares.append(square);Tells python to add all the squared numbers
# stored in the variable 'square'  to the empty list 'squares'
# 3)Then we print to see the range of numbers squared.
# NOTE: Notice how it only went to 100 because its the square
# root of 10 since the  range is 1-11.
# -------------------------------------------------------------------------
# Now we will get rid of the 'square' variable and
# append the values straight to the list 'squares';squares.append(value ** 2);
# EX:
print(
    "\n3a)Getting Rid Of The 'square' Variable And Appending "
    + "Straight To The Empty List 'squares':"
)
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# -------------------------------------------------------------------------
# Now will be using list comprehension to produce the same
# outcome as in the previous explains with 'squares'.
# NOTE:
# List comprehension combines the for loop and the
# creation of new elements into 1 line and automatically
# appends each new element.
# EX:
suqares = [value ** 2 for value in range(1, 11)]
print("\n3b)Using list comprehension to generate a range of numbers:")
print(squares)
# EXPLAINING:
# 1)We begin with the name of our list("squares")
# 2)We open a set of brackets '[]'
# 3)Then we tell python for the temp. variable(value)
# all the values stored there needs to be squared(value**2)
# 4)Now we print the 'for loop' to generate all the numbers squared
# we used in the range() method.
# EX:'[value**2 for value in range(1,11)]'
# ------------------------------------------------------------------------
# Using Min,Max,Sum functions .To find out how many items are in a list
# THESE FUNCTIONS ARE ALL SPECIFIC TO LIST OF NUMBERS
# -----------------------------------------------------------------------
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# To find the min.
print("------------------------------------------------")
print("4)Using Min,Max,Sum Functions On A List Numbers:")
print(digits)
print("\n4a)Finding Out The Lowest Number In The List Using 'min()':")
print(min(digits))
print("\n4b)Finding The Highest Number In The List Using 'max()':")
print(max(digits))
print("\n4c)Finding The Sum Of All The Numbers In The List Using 'sum()':")
print(sum(digits))
print("-----------------------------------------------")
# ------------------------------------------------------------------------
# Using Slice To Work With Part Of A List
# ------------------------------------------------------------------------
# To make a slice:
# 1)You first specify the index of the first and last
# elements you want to work with.
# EX:
print("5)Using A Slice To Get The First 3 Elements In A List:")
players = ["charles", "martian", "michael", "florence", "eli"]
print("\n5a)The original list of players:")
print(players)
print("\n5b)Now getting the first 3 elements using slice:")
print(players[0:3])
# Explaining:
# 1)In the print statement the first value in a slice
# lets you know where the slicing will begin(0).
# 2)The second number in the slice lets python know where
# the slice should end(3)
# ------------------------------------------------------------------------
# You can get rid of the first value in a slice
# and get all the elements in the list up to the ending number(4)
# EX:
print("\n5c)Getting The First 4 Elements After Omiting The First Number In The Slice:")
print(players[:4])
# ------------------------------------------------------------------------
# If you get rid of the second number the slice returns
# all the values after the first value(2)
# EX:
print("\n5d)Getting All The Elements After Omiting The Second Number In A Slice:")
print(players[2:])
# ------------------------------------------------------------------------
# You can also use the negative numbers to get the last
# 3 elements in the list.
# EX:
print("\n5e)Printing The Last 3 Elements With '-3' In The Slice:")
print(players[-3:])
# ------------------------------------------------------------------------
# We can also us slice in a 'for loop'
# EX:
print("\n5f)Using A 'for loop' To Get The First 3 Elements In The List With Slice:")
for player in players[:3]:
    print(player)
# ------------------------------------------------------------------------
# The last way of using slice is  to copy a list:
# 1)To copy a list with a slice you must get ride of the
# first and last value '[:]'.
# 2)then store it in a variable
# EX:
my_food = ["pizza", "tacos", "subs"]
my_friends = my_food[:]
print("\n5g)Using Slice To Copy A List:")
print("-My food list:")
print(my_food)
print("-My friends food list:")
print(my_friends)
# Now we can see that they are two different list in two different variables
# ------------------------------------------------------------------------
# Now we can use them as seperate list
# EX:
my_food.append("ice cream")
my_friends.append("jelly")
print("\n5h)Showing You The New Items In Each List:")
print("-My Food:")
print(my_food)
print("-My Friends Food.")
print(my_friends)
print("---------------------------------------------------------")
# ------------------------------------------------------------------------
# TUPLES
print("--TUPLES---")
# ------------------------------------------------------------------------
# Tuples are immutable list
# Python calls any values that can not be changed immutable.
# Tuples use parentheses() instead of square brackets[]
# Tuples are also single data structures.
# ------------------------------------------------------------------------
# EX:
dimensions = (200, 50)
print("6)Making A Tuple:")
print(dimensions[0])
print(dimensions[1])
# ------------------------------------------------------------------------
# You get a error if you try and change a tuples elements.
# EX:
# dimensions[0]=100
# TypeError: 'tuple' object does not support item assignment
# ------------------------------------------------------------------------
# You can write over a tuple by re-defining dimensions.
# EX:
dimensions = (400, 100)
print("\n6a)Showing New Values After Re-Defining Dimensions:")
print(dimensions[0])
print(dimensions[1])
# ------------------------------------------------------------------------
# Using 'for loop' with a tuple.
# EX:
dimensions = (100, 50)
print("\n6b)Using A 'for loop' With A Tuple:")
for dimension in dimensions:
    print(dimension)
print("--------------------------------------------------------------------")
# ------------------------------------------------------------------------
# Using A Simple If Statement
# ------------------------------------------------------------------------
# We will get more into if statements ,just needed to introduce
# you a to them a little bit, so we can do conditional test.
# ------------------------------------------------------------------------
# The following exmaple shows how a if-else statement test
# lets you respond to special situations.
# ------------------------------------------------------------------------
# EX:
favorite_cars = ["audi", "lambo", "bmw", "kia"]
print("7)The Original List")
print(favorite_cars)
print("\n7a)Using 'if-else' Statement To see 'If' 'bmw' Is In The List:")
for fav_cars in favorite_cars:
    if fav_cars == "bmw":
        print("-" + fav_cars.upper())
    else:
        print("-" + fav_cars.title())
print("-------------------------------------------------------------------")
# Explaining:
# 1)We create a list to loop through('favorite_cars') with 4 elements.
# 2)We then create a for loop to loop through all the
# items in favorite_cars('for fav_cars in favorite_cars')
# 3)The indended code tells python:
# 3a)If element "bmw" is in the list favorite_cars then
# print bmw in all caps(BMW);if fav_cars == "bmw":
# 3b)The else block is for the all elements that are not 'bmw'
# which will be printed in .title() method when the loop reaches them.
# ------------------------------------------------------------------------
# Conditional Test
# ------------------------------------------------------------------------
# A if-statement output is determined by true or false
# which is called a 'conditional test'.
# Python uses the values True an false to decide which code
# should be excuted in a if statement.
# 1)True = excute code
# 2)False = ignore code
# ------------------------------------------------------------------------
# In some parts of the lessons we will need to open
# the python terminal to check wether certain conditions
# are True or False
# NOTE:IF WE NEED TO USE CODE IN TEMINAL WILL BE NOTIFIED BY '>>>'
# ------------------------------------------------------------------------
# The simplest way to do a conditional test check:
# First we will put a value in a variable and use
# the equality operator(==) to see if the value in
# the variable is the same as the one we want to compare too.
# EX:better in python teminal
do = "x"
print("8)The Original Value Of list 'do':")
print(do)
print("\n8a)Using Conditional Test To See If Value In 'do' Is = To 'y':")
print(do == "y")
# Now we will compare two items to get the 'True' out come.
# EX
print("\n8b)Getting The True Output In A Conditional Test:")
print(do == "x")
# ------------------------------------------------------------------------
# Ignoring Case When Checking For Equalitly
# ------------------------------------------------------------------------
# Testing for equality is affected by how you compare the
# items your trying to test.
# EX:
do = "X"
print("\n8c)Doing A Conditional Test On A Capital 'X' And Lower Case 'x':")
print(do == "x")
# As you see the results say 'False' because in pyhton
# capital letters are condsider a different type of value when compared to lower case.
# ------------------------------------------------------------------------
# If capital letters does not matter you can
# use .lower() method to ignore the capital letter
# EX:
do = "J"
print("\n8d)Using The '.lower()' Method To Ignore The Capital 'J':")
print(do.lower() == "j")
# Explaining:
# 1)We create a variable(do) with a value of a capital letter(J)
# 2)Then we use the '.lower()' method to convert the capital 'J'
# to lowercase when comparing
# 3)Now even if its lowercase or uppercase as long as they
# are the same letter the results will equal 'True';do.lower() == "j".
# ------------------------------------------------------------------------
# Checking to see if a value is in a list:
# The exclamation point(!) in python means 'NOT'.
# EX:
requested_topping = "mushrooms"
print("\n8e)Using The '!' To Check If A Value Is Not('!') In A List:")
if requested_topping != "anchovies":
    print("-Hold the anchovies!")
# EXplaining:
# 1)We create a variable using a value that we can compare to
# for the conditional test.
# 2)We then create a 'for loop' to check all the items in
# requested_topping.
# Within that for loop we ask python if the requested_topping
# is not equal(!=) to 'anchovies' then print("Hold the anchovies")
# ------------------------------------------------------------------------
print("-------------------------------------------------------------------")
# Numerical Comparison
# ------------------------------------------------------------------------
# Here we will be comparing numbers in the same format we
# Was using perviously.
# EX:Checking for equality
age = 18
print("9)Comparing Two Numbers:")
print(age == 18)
# You can also test to see if two numbers are not equal '!=':
# EX:
answer = 17
print("\n9a)Comparing Two Numbers To See If There Not Equal(!=):")
if answer != 42:
    print("-42 is not equal to 17.")
# You can also compare using:
# 1)less than or greater then (<>)
# 2)less then or equal too/greater then or equal too
# (<=\>=)
# ------------------------------------------------------------------------
# Checking For Multiple Conditions
# -------------------------------------------------------------------------
# Keywords 'and' and 'or' help you test two conditions at once.
# keyword 'and' means both items you are comparing must be equal.
# EX:
print("\n-THE KEYWORD 'and':")
age_1 = 25
age_2 = 19
print("\n9b)Using Keyword 'and' To Do Two Conditional Test At Once: ")
#      item 1              item 2
print((age_1 <= 19) and (age_2 >= 18))
# It returned False because:
# 1)age_1 is not less then or equal too 19
# 2)Seeing how age_2 is greater then 18 we still get
# 'False' because they're both not 'True'.
# ------------------------------------------------------------------------
# Using the Keyword 'or'
# Now with the keyword "or" only one side of the conditional test has to be True.
# EX:
print("\n-THE KEYWORD 'or':")
age_1 = 25
age_2 = 19
print("\n9c)Using Keyword 'or' To Do Two Conditional Test At Once: ")
print((age_1 <= 19) or (age_2 >= 18))
# Now you see that the result of the conditional test equal True.
# Because age_2 is is greater then 18.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using the keyword 'in'
# The keyword 'in' allows you to check wether a element is 'in' the list.
# EX:
print("\n-THE KEYWORD 'in':")
requested = ["mushrooms", "turkey", "hamburger"]
print("\n10)Checking To See If 'mushrooms' Is 'in' The List 'requested':")
print("\n10a)" + "mushrooms" in requested)
print("checking to see if 'pepperoni' is 'in' the list requested:")
print("\n10b)" + "pepperoni" in requested)
# Explaining:
# 1) We give python  the item ('mushrooms' ) which we are looking
# for.
# 1a) Then use the keyword 'in' and the list we are searching,
# in ('requested') to see if the item is located in the list 'requested'.
# 2) "pepperoni" in requested; Same concept when using keyword 'in'
# just the output comes out as false because 'pepperoni' is not part of
# the list 'requested'
# -------------------------------------------------------------------------
print("------------------------------------------")
# How to check whether a element is 'not in' a list.
# EX:
banned_users = ["chris", "johnnie"]
users = ["maria"]
print("11)Checking Whether A Element Is 'not in' The List 'users':")
print("\n11a)You are banned from our website:")
if banned_users not in users:
    print(banned_users)
# Explaining:
# 1)We start off by creating two list so we can compair:
# (banned_users) and (users)
# 2)if banned_users not in users:;this tells python see if any of  the elements
# that are in "banned_users" are 'not in' the list "users.
# 3)All the elements in (banned_users) that are not in
# list 'users' will be printed;print(banned_users).
# -------------------------------------------------------------------------
# Boolean Expressions
# -------------------------------------------------------------------------
# NOTE: ALL BOOLEAN EXPRESSIONS IS JUST ANOTHER WORD FOR
# CONDITIONAL TEST.
# -------------------------------------------------------------------------
# A boolean is either 'True' or 'False' just like a condional test
# -------------------------------------------------------------------------
# =========================================================================
#                        INTRO TO DICTIONARIES
print("==========================================")
print("          INTRO TO DICTIONARIES")
print("==========================================")
# =========================================================================
# A 'dictionary' - in python is a collection of 'key-value' pairs
# A dictionary is composed of being wrapped in curly brackets'{}' with
# key:values inside.
# Every key is connected to its value by a colon(:) and each key:value
# pair is seperated by a comma(,).
# You can store as many key:value pairs as you want in a dictionary
# EX:This is what a  dictionary looks like.
# Variable = { Key :value , key:value}
alien = {"color": "green", "points": 5}
# Explaining:
# 1)First we create a variable to store the dictionary(alien)
# 2)Then we give the dictionary two key:value pairs:
# {'color':'green','points':5}
# -------------------------------------------------------------------------
# Accessing values in a dictionary
# -------------------------------------------------------------------------
# To get the item associated with a "Key" give the name of the dictionary
# and then place the key inside of the square brackets([])
# EX:
print("1)The Dictionary Aliens:")
print(alien)
print("\n1a)Accessing The Value For Key 'color' In Dictionary 'alien':")
print(alien["color"])
# Explaining:
# 1)We create a print statement 'print(alien['color'])'
# 2)Within that print statement the name of the dictionary(alien)
# and the key 'color'.
# -------------------------------------------------------------------------
# This will show you how to use concatention to get the,
# value(5) from the key(points) to use in a  statement.
# EX:
print("\n1b)Using Concatention To Print The Value(5) From key(points) In A Statement.")
alien = {"color": "green", "points": 5}
new_point = alien["points"]
print("You just earned " + str(new_point) + " points")
# Explaining:
# 1)First we create a dictionary 'alien' with two key:value pairs:
# 1a){"color": "green", "points": 5}
# 2)Then we create a new variable 'new_point' to store the value
# from key("points") in the dictionary 'alien';new_point = alien["points"]
# 3)str(new_point);With in the print() statement we have to convert the numerical
# value into the string representation(str()) of that number '5'
# EX:
print("\n1c)Without Using 'new_point' Variable")
print("You just earned " + str(alien["points"]) + " points")
# -------------------------------------------------------------------------
print("------------------------------------------")
# Adding New Key-Values
# -------------------------------------------------------------------------
# To add new Key-Values pairs just give the name of the
# dictionary followed by the new-key in the square brackets([])
# and the Value of the new Key after the equal sign(=)
# EX:
alien = {"color": "green", "points": 5}
print("\n2)The Original Alien Dictionary:")
print(alien)
print("\n2a)Adding A New Key:Value Pair:")
alien["x-position"] = 0
alien["y-position"] = 25
print(alien)
# Explaining:
# 1)We start by creating the new Key-Value pair 'x-position'
# by giving the name of the dictionary(alien) and then the
# new key('x-position') in square brackets([])
# 2)Then we use the equal sign(=) to assign a new Value(0)
# to the new Key('x-position')
# 3)The same process is used for 'y-position'
# -------------------------------------------------------------------------
print("------------------------------------------")
# Now we can add Key-Values pairs to a empty dictionary
# EX:
print("3)Adding Items To The Empty List 'alien_0':")
alien_0 = {}
alien_0["color"] = "blue"
alien_0["points"] = 200
print(alien_0)
# Explaining:
# 1)First we create a new dictionary called 'alien_0'
# 2)We then give the list two new Key-Value pairs:
# 2a)alien_0['color']='blue'
# 2b)alien_0['points']=200
# 3)Now we print the dictionary to see if it worked.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Modifying Values In A Dictionary
# -------------------------------------------------------------------------
# When modifying a value all you need to do is give the dictionary name(alien_0).
# Then the Key you want to change.
# EX:
print("\n3a)Showing The Original Dictionary 'alien_0' :")
print(alien_0)
print("\n3b)Now Changing The Color To 'yellow' :")
alien_0["color"] = "yellow"
print(alien_0)
# Explaining:alien_0["color"] = "yellow":
# 1)We give the dictionary we want to use(alien_0)
# 2)Then we give python the key(['color']) we want to change.
# 3)With the equal sign(=) we tell python what the new value with be
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using If-Else Statement To Modify Values In A Dictionary.
# -------------------------------------------------------------------------
# This example we will be explaining how to use the 'if-elif-else' statement to
# modify a vaule in a dictionary.
# **NOTE:THE 'X-INCREAMENT'STORES THE VALUE THAT DETERMINES HOW FAR
# THE ALIEN SHOULD MOVE RIGHT***
# EX:
alien = {"color": "green", "points": 5, "x-position": 0, "y-position": 25}

print("4)Using 'if-elif-else' Statement To Modify Values In A Dictionary:")
print("The Original Dicitionary:")
print(alien)
print(
    "\n4a)The Modified Dictionary Using The 'if-elif-else' Statement"
    + "By Adding The Key-Value('speed'):"
)
# First we will need to add the key('speed') and the values'slow',
# or medium to the dictionary(alien).
alien["speed"] = "medium"
# Now after creating the new Key('speed') and value('medium')
# we can create the if-elif-else statement to determine how far
# the alien moves:
if alien["speed"] == "slow":
    x_increament = 1
elif alien["speed"] == "medium":
    x_increament = 2
else:
    x_increament = 3
# Once the x-increament is calulated the results are added
# to x-position:
alien["x-position"] = alien["x-position"] + x_increament
print(alien)
# EXplaining:
# 1)First we start by adding a new Key("speed") and
# new Value("medium");alien["speed"] = "medium".
# 2)Then created a "if-elif-else" statement to adjust the
# x-increament(how far right a alien moves) by how fast the
# alien is moving.
# 3)Now we modify the Key('x-poistion') by adding the value
# from 'x-increament' to replace the old value(0).
# -------------------------------------------------------------------------
print("------------------------------------------")
# How To Remove Key-Values Pairs From A Dictionary
# -------------------------------------------------------------------------
# Using the del statement:
# EX:
del alien["y-position"]
print("5)Using 'del' Statement On Dictionary 'alien_0' To Delete 'y-position': ")
print(alien)
# The deleted Key('y-position'):Value(25) are gone permanitly
# -------------------------------------------------------------------------
print("------------------------------------------")
# A Different Way of Formatting A Dictionary.
# -------------------------------------------------------------------------
# You can use a dictionary to store one kind of information about many
# about many things
# EX:
favorite_language = {
    # KEYS : VALUES,
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# Explaining:
# 1)We create a dictionary(favorite_language)
# 2)Then we neatly format multiply Key-Values
# NOTE:When you need more then one line just press
#'ENTER' after the opening brace '{'
# EX:'favorite_language={'
# The indent the first line one level(4spaces) and the rest will follow
# NOTE:Make sure you have the closing brace at the end '}'.
# -------------------------------------------------------------------------
# Breaking Down A Long Print Statement
# -------------------------------------------------------------------------
# 1)Choose a approiate point to break the the print() statement
# 2)Then add a concatention operator(+) at the end of the first line
# EX:
print("6)Breaking Down A Long 'print()' Statement:")
print("Jens favorite language is " + favorite_language["jen"].title() + ".")
# Explaining:
# 1)First we have to create a print() statement
# 2)Then we add a concatention operator(+) at the end of the
# first string("Jens favorite language is " + )
# 3)Lastly we match up the second line with the begining of the first string.
# The second string contains:
# 3a)The name of the dictionary(favorite_language) and the value you want
# to access from the key('jen') and the .title() method.
# 3b)after the second concatention operator is a period(+ ".").
# --------------------------------------------------------------------------
print("------------------------------------------")
# Looping Through A Dictionary
# --------------------------------------------------------------------------
# EX:A Dictionary That Stores Infromation From A Website:
user_0 = {
    #    'KEYS'   :'VALUES',
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
# Using a 'for-loop' to print all the Keys:Value pairs in 'user_0'
# EX:
print("7)Using A 'for loop' On A Dictionary:")
for key, value in user_0.items():
    print("\n-Key:" + key)
    print("\n-Value:" + value)
# Explaining
# 1)First we create a dictionary(user_0) with multiply KEY:VALUES pairs.
# 2)Then we create a 'for-loop' using two temporary variables:
# 2a)'keys' which stores all the 'keys' from the dictionary(user_0)
# 2b)'value' which stores all the 'values' from the dictionary(user_0)
# 3)Then we use the .items() method on the dicitionary(user_0)
# 3a)NOTE:**The .items() method- returns a list of all the 'keys:values'
# pairs and stores them in the temp variables('key,value')***
# 4)The indent pieces of code:
# 4a)print("\nKey:" + key)- which shows you all the keys in the dictionary(user_0)
# 4b)print("\nValue:" + value )- which shows you all the values in the dictionary(user_0)
# ***
#   You dont have to use temp. variables name 'key,value' when loopping through a dictionary
#                                                                              ***
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using The .Key() Method
# -------------------------------------------------------------------------
# The .key() method - allows you to output only the 'Keys' in a dictionary
# EX:
lucky = {"hello": "world", "this": "kevin"}
print("8)Using The '.key()' Method To Print Out The 'keys' in dictionary 'lucky':")
for luck in lucky.keys():
    print("-" + luck.title())
# Explaining:
# 1)first we create a dictionary(lucky)
# 2)then we create a for loop:
# 2a)We use one temporary variable(luck) to group
# the keys:values pairs together instead of seprate(key,value).
# 2b)'lucky.keys()' tells python to grab all the key
# elements from the dictionary(lucky).
# 3)With the indented code we format how we want the
# output to be 'print('-' + luck.title())'.
# NOTE:Looping through keys is the default behavoir when
# looping through a dictionary.
# EX:BOTH CREATE SAME OUTPUT:
# 1)for luck in lucky.keys():
# 2)for luck in lucky:
# Using '.keys()' method helps your code more easier to read.
# -------------------------------------------------------------------------
# Using the .keys() method to create a message:
favorite_language = {
    #    KEYS : VALUES,
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# The list of friends you want to send the message to:
friends = ["jen", "sarah"]
print("\n8a)Using .keys() Method To Create A Message For The Ones In 'friends' List:")
for name in favorite_language.keys():  # **NOTE:THE TEMPORARY VARIABLE(NAME)
    if name in friends:  # IS USED TWICE BECAUSE:********
        print(  # 1)In 'for loop' the name variable
            "\n"  # is used to store the keys from
            + "Hey "  # from dictionary 'favorite_language'
            + name.title()  # 2)The  if statement uses the name variable
            + ","  # to compare the keys from dictionary 'favorite_language'
            + "i see your favorite "  # to the list of friends
            + "programing language is "  # if there(dictionary/list) elements match then the
            + favorite_language[name].title()  # message is printed for there names.
            + "."
        )
    print(name.title())
# Explaining
# 1)We reuse the dictionary favorite_language from  a pervious example.
# 2)Then we create a list(friends) to send the message to
# certain people.
# 3)Then we create a 'for-loop' using the temporary variable 'name'
# only extracting the 'keys' from the dictionary(favorite_language);
# "in favorite_language.keys():"
# 4)One piece of the indented code is a if - statemant(if name in friends:):
# 4a)"if name in friends:"; Is basically telling python if any of the keys
# from dicitonary "favorite_language" matches the names in the list(friends)
# run the print() statement.
# 5)print(name.title()); just prints the keys from 'favorite_language' in .title()method.
# -------------------------------------------------------------------------
# Using The .Keys() Method To See If A Particular Element Is The Dictionary.
# EX:
favorite_language = {
    #    KEYS : VALUES,
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\n8b)Using '.keys()' Method To Check If A Element Is In A Dictionary:")
if "brad" not in favorite_language:
    print("BRAD,GO TAKE THE POLL!!")
# -----------------------------------------------------------
# Sorting Before Looping:
# EX:
print("\n8c)Using The 'sorted()' Function To Put The keys In 'abc' Order:")
print("Thank You For Taking The Poll!!!")
for name in sorted(favorite_language.keys()):
    print("-" + name.title())
print("\n8dThe Original Order For The keys():")
print(favorite_language.keys())
# NOTE:REVEIW:The sorted() function temporarly puts
# the order of the dictionary/list elements in
# alphabetical order.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Looping Through All The Values Of A Dicitonary.
# -------------------------------------------------------------------------
# .values() method - returns all the values of a dictionary
# EX:Printing all the values of 'favorite_language'
print("9)Using .values() Method To Print All The" + " Values In 'favorite_language'")
for name in favorite_language.values():
    print("-" + name.title())
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using The Set() Method
# -------------------------------------------------------------------------
# If a dictionary had a duplicate of one item(python)
# then the sort() method will only print out the first
# occurance of that element(python)
favorite_language = {
    #    KEYS : VALUES,
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("10)Using 'set()' Method To Only Print The First Occurance Of An Element:")
print("\n10a)The Original List Of Values:")
print(favorite_language.values())
print("\n10b)Using The 'set()' Method:")
print(set(favorite_language.values()))
# =========================================================================
#                         NESTING
print("==========================================")
print("              INTRO TO NESTING")
print("==========================================")
# =========================================================================
# Nesting is when you want to combine:
# 1)A list inside a dictionary
# 2)A Dictionary inside of a dictionary
# 3)A Dictionary inside of a list
# -------------------------------------------------------------------------
# A List Of Dictionaries:
# EX:
cast_1 = {"Act_1": "Jerry", "points": 10}
cast_2 = {"Act_2": "Mark", "points": 7}
cast_3 = {"Act_3": "Johnnie", "points": 9}
records = [cast_1, cast_2, cast_3]
print("1)NESTING:A List of Dictionaries:")
for cast in records:
    print(cast)
# Explaing:
# 1)First we create 3 dictionaries(cast_1,cast_2,cast_3)
# 2)Then we store the 3 dictionaries into a list(records)
# 3)Then we create a 'for-loop' to grab all elements in
#'records'
# NOTE:The output is what is stored in each dictionary.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using the range() function to create 30 dicitionaries
# EX:
aliens = []
# Making 30 green aliens:
for alien_number in range(30):
    new_alien = {
        "color": "green",
        "points": 5,
        "speed": "slow",
    }
    aliens.append(new_alien)
print(
    "\n1a)Using The 'range()' Function To Create 30 Dictionaries"
    + "But Only Listing The First 5:"
)
# Showing the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
print("total numbers of aliens " + str(len(aliens)))
# Explaining
# 1)First we create a empty list(aliens)
# 2)We then create a 'for loop' using the temporary
# variable 'alien_number' to store the numbers 1-30.
# The indented pieces of code:
# 2a)'new_alien' is a dictionary of the 'color','points',and 'speed'
# of the aliens that will be created 30 times.
# 2b)'aliens.append(new_alien)'; tells python to add all 30 of the new dictionaries
#  to the list 'aliens'.
# 3)In the second 'for-loop'(for alien in aliens[:5]:)
# uses the temporary variable 'alien' to store the first 5 aliens('in aliens[:5]:').
# The indented piece of code(print(alien)) just prints
# the first 5 aliens.
# NOTE: in the last print statement:
# print("total numbers of aliens" + str(len(aliens)) )
# we must convert the interger into a string first(str(len(aliens)))
# -------------------------------------------------------------------------
# Since each one of the aliens are different dictionaries
# with the same characteristics we can change the first 3
# aliens.
# EX:
print(
    "\n1b)Changing '3 out 30' Dictionaries In List 'aliens';'color','speed',and'points'."
)
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    print(alien)
# EXplaining
# 1)first we create a 'for-loop' with temporary variable
#'alien' to store the 3 out of 30  aliens by slicing the
# list('in aliens[:3]:')
# 2)We then create a if-statement telling python:
# 2a)if theres any aliens with the value 'green' for the
# key 'color' with in the first 3 aliens then:
# 2b)the indented peices of code tells python:
# if we find a green alien out of the first 3 then
# change the color to 'yellow','speed to 'medium' and points to '10'.
# Then print the first 3 aliens.
# -------------------------------------------------------------------------
print("------------------------------------------")
# A List In A Dictionary.
# -------------------------------------------------------------------------
# Creating a pizza:
pizza = {
    "crust": "thick",
    "toppings": ["turkey", "mushrooms"],
}
print("2)Creating A List In A Dictionary:")
print(
    "You order a " + pizza["crust"] + "-crust pizza," + " With the following toppings:"
)
for topping in pizza["toppings"]:
    print("-" + topping)
# Explaining:
# 1)First we create a dictionary(pizza)
# 1a)Within the dictionary we have:
# 1b)key('crust'):value('thick') format
# 1c)Key('topping') and a list as values(['turkey','mushrooms'])
# 2)We then create a print statement using:
# 2a)the value of key 'crust'(pizza['crust']) from the pizza dictionary.
# 3)We then create a 'for-loop' with the temporary varaiable 'topping':
# 3a)'topping' stores the list from the key('toppings') from the
# 'pizza' dictionary; in pizza['toppings'];.
# 4)The indented piece of code tells python to format the results
# from temporary variable 'topping':print("-" + topping):.
# -------------------------------------------------------------------------
# Another Way Of Using A List In A Dictionary.
# EX:Using 'favorite_language' dictionary:
favorite_language = {
    #    KEYS : VALUES/LIST,
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskel"],
}
print("\n2a)Another Way To Use A List In A Dictionary:")
for name, language in favorite_language.items():
    print("\n" + name.title() + "'s favorite language is ")
    for languages in language:
        print("-" + languages.title())
# Explaining:
# 1)We create a dictionary(favorite_language), within this dictionary:
# 1a)The keys() are the name of the people
# 1b)The values are a list of the programing language(s)
# of each person.
# 2)We then create a for-loop using temp. variables(name,language)
# 2a)The 'name';temp. variable stores all the keys in the dictionary
# 2b)The 'language' temp. variable stores all the values which are the list of languages.
# 3)Then we use the '.items()' which returns all the key:value
# pairs as a list  and stores them in (name,language).
# 4)The indented code prints out a message for the keys(name.title())
# 5)the second 'for loop' takes all the values(for languages in language:)
# and prints them out;print("-" + languages.title());
# -------------------------------------------------------------------------
print("------------------------------------------")
# A Dictionary Inside Of A Dictionary.
# -------------------------------------------------------------------------
# EX:
users = {
    "aeinstein": {"first": "albert", "last": "einstein", "location": "princeton",},
    "mcurie": {"first": "marie", "last": "curie", "location": "paris",},
}
print("3)A Dictionary Inside Of A Dictionary:")
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\tLocation:" + location.title())
# EXplaining:
# 1)We first create a dictionary(users) with two keys:
# 1a)'aeinstein' and 'mcurie'
# 2)Within the two keys('aeinstein','mcurie') is a dictionary as there values,
# With 3 indavidual keys-values:
# 2a)Keys('first','last','location'):Values
# 3)Then we create a for loop with two temp. varaiables:
# 3a)'username' stores keys ('aeinstein','mcurie') from dictionary 'users'
# 3b)'user_info' stores the values('first','last','location')
# from dictionaries('aeinstein','mcurie')
# 4)The indented pieces of code tells python:
# 4a)The first piece just tells python to print every user name('aeinstein','mcurie')
# 4b)The second piece of code uses the user_info temp.variable to concatenate
# the values for keys user_info["first"] and user_info["last"] which are
# the same key:values from dictionary 'aeinstein' and 'mcurie'
# 5)location = user_info["location"]; also uses the temp. variable user_info but this time
# grabs the value for the 'location' key in dictionary 'aeinstein','mcurie'
# 6)The last two print statements tells python:
# 6a)print() the full_name variable with the .title() method.
# 6b)print() the location variable with the .title() method.
# =========================================================================
#                 INTRO TO INPUT() & INT() FUNCTION
print("==========================================")
print("   INTRO TO INPUT() & INT() FUNCTIONS")
print("==========================================")
# =========================================================================
# The input() function allows you to recive input from the user
# then is store the information inside a variable that you can use later.
# EX:
# tell_me = input("Tell me somthing you like about python. ")
# print(tell_me)
# Explaining:
# 1)First we create a variable(tell_me) to store the
# users input in.
# 2)Within that variable(tell_me) is the input() function
# and within the parentheses is the prompt:
# 2a)"Tell me somthing you like about python. " which will
# be displayed for the user to respond too.
# 2b)once the user responds and then  pressing 'ENTER'. The response
# is stored in the variable(tell_me)
# 3)print(tell_me) tells python to print the response
# stored in the variable(tell_me)
# -------------------------------------------------------------------------
# How To Write A Clear Prompt.
# -------------------------------------------------------------------------
#  ***The prompt in the input statement is also consider the instructions for
# the user to follow.So a clear easy-to-follow 'prompts' will help the user know exactly
# what you are looking for.************************************************
# EX:
# name = input("Please tell me your name: ")
# print("Hello," + name.title() + "!")
# EXplaining:
# 1)First we create a a variable named 'name'
# 2)Then we use the input() function to create a prompt for
# the user to respond to then its stored back into variable(name)
# 3)then we create a print statement which prints "hello" then
# the users with the .title() method;input(name.title()).
# NOTE:MAKE SURE YOU ALWAYS ADD A SPACE AT THE END OF YOUR PROMPT
# TO SEPERATE THE PROMPT FROM THE USER INPUT.
# -------------------------------------------------------------------------
# Writting A Prompt With More Then One Line
# EX:
# prompt = "I can probably help you with something."
# prompt += "\nWhat can I do for you? "
# service = input(prompt)
# print("Okay let me find, " + service)
# EX:
# 1)We create a variable(prompt) to store the strings used to instuct the user
# 2)The second 'prompt' we use the operator "+=" to add the second string
# to the end of the first string.
# 2a)Since we have "\n" within the second string; the second string will be underneath the first.
# 3)We then create another variable(service) to store the users input
# 4)inside of that variable(service) we give the input function the variable(prompt)
# 5)then we print the output.
# -------------------------------------------------------------------------
# Accepting Numerical Input With Int() function
# -------------------------------------------------------------------------
# NOTE:When using the input function,pyhton interpets the user input as a string.
# EX:
# age = input("How old are you? ")
# print(age)
# Explaining:
# 1)We create a variable(age) to store input from prompt("How old are you? ")
# 2)When the users input is 'ENTERED' the number should be
# outputed like this :'21' since all user input is interpeted as a string
# -------------------------------------------------------------------------
# How To Compare Numbers With User Input()
# -------------------------------------------------------------------------
# If we tried to compare the 'age' variable input with a number:
# EX:
# print(age >= 18)
# Explaining:
# 1)With this simple comparision we see that we can not compare
# string objects(age) with a numerical represention of '18'
# 2)The traceback that occurs is:
# TypeError: '>=' not supported between instances of 'NoneType' and 'int'
# 2a)Basically stating that the comparision(>=) can not be made because
# the 'Nonetype'(string) cant be compared to a interger'int'
# -------------------------------------------------------------------------
# NOTE:The 'int()' function converts the string representation of a number
# into the numerical representation*************************************
# THE CORRECT WAY TO COMPARE USER INPUT:
# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)
# Explaining:
# 1)We use the 'age' variable to store user input
# 2)We then take the user input and convert it into the
# numerical representation of that number(int(age)).
# 2a)Then we store the conversion back into the variable(age)
# print(age >= 18);Now we can compare numbers from user input without
# getting a traceback.
# NOTE:ALWAYS MAKE SURE YOU CONVERT(int()) AND STORE BACK INTO VARIABLE(age)
# BEFORE COMPARING(age >= 18)
# -------------------------------------------------------------------------
# The Modulo Operator(%)
# -------------------------------------------------------------------------
# The modulo operator(%) divides one number by anothor number and returns the
# remainder.
# ***The modulo operator does not tell you how many times a number
# fits in another number.**************************************************
# NOTE:IF THE  MODULO OF A NUMBER AND TWO('numbers %2') IS ZERO(== 0) THEN
# THE NUMBER IS EVEN
# EX:Using the modulo operator to determine if a number is even or odd
# numbers = input("Enter a number to see if its even or odd.")
# numbers = int(numbers)
# if numbers % 2 == 0:
#    print("Your number, " + str(numbers) + " is even.")
# else:
#   print("Your number, " + str(numbers) + " is odd.")
# Explaining:
# 1)We create a variable(numbers) with the input() function stored inside
# 2)Then we convert the string representation of the number the user
# inputed(numbers = int(numbers))
# 3)Then we create a if-else statement:
# 3a)'if numbers %2==0:' This tells python if the number that the user
# inputed can be divisiable by 'two' and equal to '0' then its 'even'.
# 3b)if not then we use the else statement which tells the user the number is 'odd'
# =========================================================================
#                      INTRO TO WHILE LOOPS
print("==========================================")
print("         INTRO TO WHILE LOOPS")
print("==========================================")
# =========================================================================
# In retrospect the "for-loop" takes a collection of items and excute a block
# of code once for each item then ends.
# The While loop runs as long as a certain condition is true.
# -------------------------------------------------------------------------
# Using a 'while-loop' to count to 5:
current_number = 1
print("1)Using A 'while-loop' To Count To 5:")
while current_number <= 5:
    print(current_number)
    current_number += 1
# Explaining:
# 1)We create a variable called 'current_number' which sets the
# start of the count to 1(current_number = 1).
# 2)We then create a while-loop('while') which runs as long as
#'current_number' is less then 5(current_number <= 5:)
# 3)The indented pieces of code:
# 3a)print(current_number); tells python to print the number that its
# on right now as its counts to 5
# 3b)current_number += 1; tells python to add a one to every number until it
# reaches 5; basically(1+1),(2+1),(3+1),(4+1)
# -------------------------------------------------------------------------
print("------------------------------------------")
# Letting A User Know When To Quit
# -------------------------------------------------------------------------
# EX:
# prompt = "Tell me something and i will print it back to  you."
# prompt += "\nEnter 'quite' to end program."
# message = " "
# while message != "quit":
#    message = input(prompt)
#    if message != "quit":
#       print(message)
# Explaining:
# 1)First we create a  prompt to let users know what information we
# want as there input
# 2)We then create a variable named 'message' with a empty string because:
# 2a)The 'while-loop' needs to compare the input of the user to quite so in order
# to start the while loop the variable message is checked to make sure
# that it does not have the 'quite' input stored.
# 3)while message != "quit":; tells python to keep running the while loop until
# the 'quit' input is entered
# 4)The indendet peices of code:
# 4a)message = input(prompt); tells python to store the prompt into the variable
#'message'
# 4b)if message != "quite":; tells python if the users input is not-equal(!=) to 'quit'
# then keep printing the users input.
# NOTE:IF THE USER DOES NOT ENTER 'QUIT' THEN THE WHILE LOOP
# BRINGS THE PROMPT BACK UP************************************************
# -------------------------------------------------------------------------
# Using Flags
# -------------------------------------------------------------------------
# A flag - can be defined as one variable that determines whether or not a
# program is active.
# NOTE:WE CAN WRITE OUR PROGRAMS SO THEY RUN WHILE THE FLAGS IS SET TO 'TRUE'
# AND STOP WHEN SEVERAL EVENTS SETS THE VALUE OF THE FLAG TO FALSE.
# EX:
# active = True
# while active:
#    if message == "quit":
#        active = False
#    else:
#        print(message)
# Explaining:
# 1)First We create a variable(active) and set the value to equal  'True'
# 2)Then we create  a while-loop(while active:) which tells python
# to run as long as active is equal to 'True'.
# 3)The indented pieces of code within the while-loop:
# 3a)'if message == "quit":'; This tells python if the users input is 'quit'
# then set the variable(active) to 'False'.Which will end the program
# 4)'else:'; tells python that if 'quit' is not 'ENTERED' as a users input
# then keep printing the message.
# ------------------------------------------------------------------------
# Using Break To Exit A Loop
# -------------------------------------------------------------------------
# The 'break' statement lets you exit a program no matter the result of the
# the conditional test(True/False)
# In other word the 'break' statement directs the flow of your program.
# EX:
# prompt = "\nPlease enter the name of your dream car. "
# prompt+= "\nEnter quit to end program!"
# while True:
#    city=input(prompt)
#    if city == 'quit':
#        break
#    else:
#        print("I would love to go to that ," + city + "!")
# Explaining:
# NOTE:A WHILE-LOOP WILL CONTINUOSLY RUN WITHOUT BREAK STATEMENT
# 1)First we create a prompt asking the user  to enter:
# 1a)"the name of there dream car"
# 2)'while True:';Tells python to run the indented peices of code
# until the state of the loop changes to False('break')
# 3)The indented pieces of code:
# 3a)if city == 'quit':; Tells python if the users input is equal to quit
# then end('break') the program.
# 3b)else:; tells python that if the user 'does not' enter 'quit'
# then print the print() statement.
# NOTE:YOU CAN USE THE BREAK STATMENT IN ANY LOOP(FOR/WHILE)
# -------------------------------------------------------------------------
# Using Continue Statement In A Loop
# -------------------------------------------------------------------------
# The 'continue' statement - allows you to return to the begining of the loop
# based on the results of the conditional test(s).
# -------
# EX:A loop that counts from 1 to 10 but only odd numbers.
current_number = 0
print("1)Using While-loop To Generate Only Odd Numbers To 10:")
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
# Explaining :
# 1)First we create a variable(current_number) with a
# value(0) to tell python where the count will start
# 2)Then we create a while-loop that will run as long as the
# the value of 'current number' is less then '<10'
# 3)The indented pieces of code:
# 3a)current_number += 1; Tells python to add 1 to the
# the value in 'current_number' until the loop reaches '10';(1+1,2+1,etc...)
# 3b)if current_number % 2 == 0:(this is for even numbers); this tells python
# if the current_number and modulo of 2 is equal to 0 then skip and
# continue running loop starting at the begining (while current_number < 10:).
# 4)The print statement within the while loop tells python to print
# each odd number until the loop reachs '10'.
# -------------------------------------------------------------------------
# Advioding Infinite Loops
# NOTE:EVERY WHILE LOOP NEEDS A WAY OF STOP RUNNING
# EX:Infinite Loops
# Correct Way To Adviod a infinite loop:
print("------------------------------------------")
x = 1
print("\n2)Advioding A Infinite Loop:")
while x <= 5:
    print(x)
    x += 1
# The Infinite loop:
# x = 2
# while x <= 5:
#    print(x)
# Explaining:
# 1)If you accidentally delete 'x += 1' like shown being used
# in the 'correct way' the loop runs forever
# 2)The reason why is the value of 'x' will always be less then 5(while x <= 5:):
# so you will get a series of '2's'
# NOTE:THINGS TO DO IF YOUR PROGRAM GETS CAUGHT IN A INFINATE LOOP:
# 1)You can press "CTR + C" to end the loop.
# 2)Make sure at least one part of the program can make the loop condition
# turn 'False' or cause it to reach a 'break' statement.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using A While Loop With List and Dictionaries:
# -------------------------------------------------------------------------
# NOTE:A 'FOR-LOOP' IS MORE EFFECTIVE FOR LOOPING THROUGH LIST.
# You should not  modify list inside a for-loop because python
# Has a hard time keeping up with the items.
# Using while-loop(s) with list and dictionaires allows you to collect,
# store, and organize lots of input to examine and report.
# -------------------------------------------------------------------------
# Moving items from one list to  another:
# Taking the list of 'unconfirmed_users'  and putting them
# in the list confirmed users.
# EX:
unconfirmed_users = ["jerry", "reggie", "chris", "paul"]
confirmed_users = []
print("\n3)Moving Items From One List To Another:")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifing user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print("-" + confirmed_user.title())
# Explaining:
# 1)First We start with a list(unconfirmed_users)
# 2)Then we create a empty list(confirmed_users) to have a place to
# store the tranfered items from list 'unconfirmed_users'
# 3)Then We create a while-loop(while unconfirmed_users:) that tells
# python as long as there are items in 'unconfirmed_users' the while
# loop remains active.
# 4)The indented pieces of code:
# 4a)current_user = unconfirmed_users.pop(); tells python to
# remove the last(.pop()) item in the list(unconfirmed_users) each passing
# of the loop and store it in variable 'current_user'
# 4b)print("Verifing user: " + current_user.title());tells python  to print
# all the current users with .title() method.
# 4c)confirmed_users.append(current_user); Tells python to add all the items
# in current_users to the end(.append()) of the list of confirmed_users.
# 5)for confirmed_user in confirmed_users:; creates a for-loop with
# temporary variable 'confirmed_user'  to store all the items
# from 'confirmed_users' and then print them out:
# (print("-" + confirmed_user.title()))
# -------------------------------------------------------------------------
print("------------------------------------------")
# Removing All Instances Of  A  Specific Value From A List
# -------------------------------------------------------------------------
# Using the remove() method in a while loop to delete all occurances of 'frog'.
# EX:Removing 'frog'
print("4)Using The 'remove()' Method In A 'while-loop':")
pets = [
    "dog",
    "cat",
    "frog",
    "rat",
    "frog",
    "dog",
    "mouse",
    "frog",
]
print("\n4a)The Original List Of Pets:")
print(pets)
while "frog" in pets:
    pets.remove("frog")
print("\n4b)Removing The Pet Type;'frog':")
print(pets)
# Explaining:
# 1)First we create a list of pets then print the list
# to show you the original.
# 2)'while 'frog' in pets:';Tells python to keep running this
# 'while loop' as long as the word 'frog' is in the list(pets)
# 3)The indented pieces of code:
# 3a)pets.remove('frog'); Tells python to remove all the
# pet types that are a 'frog'.
# 4)We finally print the new list with all the 'frog' elements removed :
# 4a)print(pets)
# -------------------------------------------------------------------------
# Filling A Dictionary With User Input Using While-Loops
# -------------------------------------------------------------------------
# NOTE:You can prompt for as much user input as you need:
# Making a poll that each time we pass through the 'while-loop'
# we store the input into a dictionary.
# EX:
# responeses = {}
# polling_active = True
# while polling_active:
#                 prompt
# name = input("What is your name? ")
# response = input("Which mountain would you like to climb someday? ")
#   responeses[name] = response
# repeat = input("Would you like to let another person respond(yes/no) ")
# if repeat == "no":
#        polling_active = False
# print("\n---Poll Results ---")
# for name, response in responeses.items():
#    print(name + " would like to climb " + response + ".")
# Explaining:
# 1)First we create a empty dictionary(responeses)
# 2)Then create a flag that starts the 'while-loop' off in
# a active(= True) state.
# 3)Now we create the 'while-loop' which runs as long as
#'polling_active' is still equal to 'True' ;'while polling_active:'
# 4)The indented pieces of code:
# 4a)name = input("What is your name? ");Tells python to store the
# users input into variable "name" from the prompt('input()')
# 4b)response = input("Which mountain would you like to climb someday? ");
# Tells python to store the users input for this prompt(input()) into
# variable 'response'
# 4b)responeses[name] = response;Tells python to make a key 'name' and
# value 'response' pair for dictionary('responeses')
# 4c) repeat = input("Would you like to let another person respond(yes/no) ");
# tells python to store the users input for the prompt in 'input()' into variable
#'repeat'
# 4d)if repeat == "no":;Tells python if the users input is equal to 'no' then
# the indented piece of code;polling_active = False; ends the program.
# 5)print("\n---Poll Results ---");Tells python to print the a title we made
# to help users know where the 'poll results' are.
# 6)for name, response in responeses.items():;
# This for-loop uses two temorary variables(name,response)
# 6a)'name'-Tells python to store all the 'keys()' from dictionary(responeses) there
# 6b)'response'-Tells python to all  the 'values()' from dictionary(responeses) there
# ***The 'in responeses.items():' piece of code just tells python to return all the
# dictionaries(reponeses) items in a list format(.items())*************************
# 7)The indented piece of code:
# 7a)print(name + " would like to climb " + response + ".");
# Tells python to use the temporary variables('name','response') in this style.
# =========================================================================
#                       INTRO TO FUNCTIONS
print("==========================================")
print("          INTRO TO FUNCTIONS")
print("==========================================")
# =========================================================================
# Functions- are named blocks of code that are designed to do one specific job.
# #NOTE:THE INDENTED PIECES OF CODE IS WHAT MAKES UP 'THE BODY OF A FUNCTION'.
# EX:
def greet_user():
    """Display a simple Greating"""
    print("Hello!")


print("1)Using Creating a Function Called 'greet_users': ")
greet_user()
# Explaining
# 1)def greet_user():;This is called the 'function definition',which
# tells python the name of the function.
# 1a)Any additonal information the function needs to operate
# will be in the parentheses'()'.
# 1b)NOTE:WHEN EVER YOUR DONE DEFINING YOUR FUNCTION YOU MUST
# PUT A COLON AT THE END ':'
# 2)The indented pieces of code:
# 2a)"""Display a simple Greating""";This is called a 'docstring'
# which describes what the function does.
# 2b 'print("Hello!")';This just simplies print 'hello'
# 3)When we want to use the function we do what is known as a "function call"
# greet_user();Any additional info need for the function to operater
# properly will be in the parentheses'()'
# -------------------------------------------------------------------------
# Pass Info Into A Function
# -------------------------------------------------------------------------
# Parameters And Arugments:
# Parameter - is a piece of infromation the function needs to do its job.
# Argument- is a piece of informantion passed through the function from the
#'function call'.
# EX:
#          'Parameter#1'
def by_name(username):
    """Using A Parameter in a fucntion"""
    print("Hello, " + username.title() + "!")


print("\n1a)Passing Info Into A Function:")
#      'Argument#1'
by_name("kevin")
# Explaining
# 1)def by_name(username):; tells python to create a function(by_name)
# and when we make a call we need to give a argument for the parameter(username)
# 2)The indented pieces of code:
# 2a) """Using A Parameter in a fucntion""";The docstring tells you
# what this function does.
# 2b)print("Hello, " + username.title() + "!");Tells python with the
# parameter 'username' to create a print() statement in this style.
# 3)by_name("kevin");This is called a 'function call' which tells python
# to excute the code in the function.
# 3a)Seeing how the function is provided with a parameter when defining
# function;by_name(username); we need to provide a argument(by_name("kevin"))
# in order for this function(by_name) to operate.
# ------------------------------------------------------------------------
print("------------------------------------------")
# Passing Arugments.
# -------------------------------------------------------------------------
# There are two kinds of arugments you can pass through a function call:
# 1)Postional Arugments -  Needs to be in the same order as the parameter(s)
# is in.
# 2)Keyword Arugments -Consist of a variable and value ;or list/dictionaries
# as values.
# -------------------------------------------------------------------------
# Postional - Argument
# EX:
#                'parameter#1', 'parameter#2'
print("2)Using Postional_Arguments:")


def describe_pet(animal_type, pet_name):
    """Displaying information about a pet"""
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


#              A#1 , A#2         A=Arugment
describe_pet("dog", "Q")
# Explaining
# 1)First we define a function(describe_pets) with two parameters:
# (animal_type,pet_name)
# 2)The indented pieces of code:
# 2a)"""Displaying information about a pet""";Is a docstring that tells
# you what the function does.
# 2b)print("\nIhave a " + animal_type.title() + "."); tells python
# to print a message based off the type of pet you put as the first argument.
# 2c)print("My " + animal_type + "'s name is " + pet_name.title() + ".");
# Tells python to tell users what kind of pet you have and the name.
# 3)describe_pet("dog", "Q");This is the function call with two postional_arugments:
# 3a)"dog" = animal_type :parameter #1
# 3b)"Q" = pet_name :parameter#2
# NOTE:ORDER MATTERS IN POSITIONAL ARGUMENTS.
# -------------------------------------------------------------------------
# Keyword-Arguments
# -------------------------------------------------------------------------
# You directly associate the name and the value within the argument,so you dont
# have to worry about which order to put them in.
# EX:
def describe_pet(animal_type, pet_name):
    """Displaying information about a pet"""
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


print("\n2a)Using Keyword Arguments:")
#           parameter=argument#1, parameter#2=argument#2
describe_pet(pet_name="henery", animal_type="zombie")
# Explaining:
# 1)In the function call we have parameters(pet_name,animal_type)
# 1a)Then we have arguments(henery,zombie)
# 2)With your 'parameters=arugments' in the same function call
# python does not have to assume the postional order of the parameters
# when listing your arguments.
# -------------------------------------------------------------------------
print("------------------------------------------")
# Defult Values
# -------------------------------------------------------------------------
# A Default Value- is a arugment already assigned to one/both of the parameters
# When you call the function  you either have the option to use the
# default value as a arugment  or enter in your own value as a argument
# NOTE:IF YOU USE ONLY ONE DEFAULT VALUE THEN THE VALUE MUST BE LAST
# WHEN DEFINING THE FUNCTION EX: def pre_screened(first, last="doe"):
# WHICH TELLS PYTHON IT ONLY NEEDS A ARGUMENT FOR THE PARAMETER 'first'
#  EX:
print("3)Using Default Values:")

#               P#1 DV='john'  P#2 DV= 'doe'            P = parameter
def pre_screened(first="john", last="doe"):  #  DV = default value
    """Using Default Values"""
    print("Hello " + first + ", how are you? ")
    print("How may i help you Mr." + last + "?")


pre_screened()
print("\n3a)Now Using Postional Arguments:")
pre_screened("marc", "holy")
# Explaining:
# 1)First we define a function(def pre_screened) with two parameters:
# 1a)The first parameter(first) has a default value of 'john'
# 1b)The second parameter(last) has a default value of 'doe'
# 1c)This tell python that if there is no argument given in the 'function
# call'(pre_screened()) then the default values("john","doe") will be used
# in the indented pieces of code.
# 2)The indented pieces of code:
# 2a)print("Hello " + first + ", how are you? "); Tells python to use the
# parameter 'first' to ask "how are you?" by your first name('first').
# 2b)print("How may i help you Mr." + last + "?"); Tells python to
# print how may i help you? with the second parameter('last')
# 3)Calling the function 'pre_screened':
# 3a)pre_screened(); Tells python to use the default values('john','doe')
# 3b)pre_screened("marc", "holy");Shows you that you can still put in your own
# arguments instead of using defualt values.
# =========================================================================
#                      INTRO TO RETURN VALUES
print("==========================================")
print("      INTRO TO RETURNING VALUES")
print("==========================================")
# =========================================================================
# The 'return' statement - takes the value from inside a function
# and sends it back to the line that called the function.
# -------------------------------------------------------------------------
# Returning A Simple Value
# ------------------------------------------------------------------------
# A function that takes a first and last name, and 'return' a neatly
# fomatted name.
# EX:
print("1)Using the 'return' statement:")


def formatted_name(first_name, last_name):
    """Formatting a name"""
    full_name = first_name + " " + last_name
    return full_name.title()


employees = formatted_name("john", "peterson")
print(employees)
# Explaining:
# 1)First we define a function(formatted_name) with
# two parameters(first_name,last_name)
# 2)The indented pieces of code:
# 2a)"""Formatting a name"""; is the docstring that
# tells you want the function does
# 2b)full_name = first_name + " " + last_name;We create a
# variable(full_name) to store the first_name and last_name
# argument.
# 2c)return full_name.title();This tells python once
# the call for the function is recived return the arguments
# in this style(first_name + " " + last_name) with .title()
# method.
# 3)employees = formatted_name("john", "peterson");
# NOTE:WHEN YOU CALL A FUNCTION THAT HAS 'return',
# YOU NEED TO PROVIDE A VARIABLE WHERE THE RETURN VALUE
# CAN BE STORED.
# 4)print(employees);Show the ouput of the function call:
# (formatted_name("john", "peterson"))
# -------------------------------------------------------------------------
# Making An Argument Optional
print("------------------------------------------")
# -------------------------------------------------------------------------
# You can use default values to make a arguments opitional.
# Making the middle name optional
# EX:
print("\n2)Making Middle Name Arugment Optional:")


def formatted_name(first_name, last_name, middle_name=""):
    """Formatting a name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


print("\n2a)No Middle Name:")
employees = formatted_name("john", "peterson")
print(employees)
print("\n2b)With Middle Name:")
employees = formatted_name("john", "peterson", "allen")
print(employees)
# Explaining:
# 1)First we define a function(formatted_name) with three
# parameters(first_name,last_name,middle_name="")
# 1a)middle_name="";We give parameter 'middle_name' a emtpy string just
# to give it a simple 'default value'
# NOTE:ANY PARAMETER WITH A DEFAULT VALUE GOES LAST WHEN DEFINING
# A FUNCTION((first_name, last_name, middle_name=""):)
# 2)The indented pieces of code:
# 2a)"""Formatting a name""";This is a docstring that tells you
# what the function does.
# 2b)if middle_name:;The if statement tells python if theres
# a middle name argument provided then style the output like this:
# full_name = first_name + " " + middle_name + " " + last_name
# 2c)else:;The else block tells python if theres no middle name
# then style the output like this:
# full_name = first_name + " " + last_name
# 3)return full_name.title();This tells python to which ever condition is met
# then return the full_name format with .title() method back to the function call
# to be outputed correctly.
# 4)Finally we call the function two ways:
# 4a)With Out The Middle Name :
# employees = formatted_name("john", "peterson")
# 4b)With Middle Name:
# employees = formatted_name("john", "peterson", "allen")
# -------------------------------------------------------------------------
# Returning A Dictionary
print("------------------------------------------")
# -------------------------------------------------------------------------
# A function can return any type of data you need it too.
# EX:
print("3)Returning A Dictionary Using A Function:")


def build_person(minds, body_types):
    """Returning a Dictionary"""
    person = {"Mind": minds, "Body Type": body_types}
    return person


avatar = build_person("Creative", "Fit")
print(avatar)
# EX:
# 1)First we define a function(build_person) with two parameters(mind,body_type):
# 2)The indented pieces of code:
# 2a)"""Returning a Dictionary""";The docstring tells you what the function
# does.
# 2b)person = {'Mind':minds,'Body Type':body_types};We store a dictionary
# into a variable(person).Then we give the dictionary two Keys:values pairs:
# 2c)Key 'mind' stores the parameter 'minds' so when the argument for 'minds'
# is sent through the function call("creative")  it will be stored in the  key 'mind'.
# 2d)The key 'Body Type' stores the parameter 'body_types' which tells python
# when the argument for 'body_types' is given in the function call("Fit")
# it will be stored as a value for 'Body Type' in the dictionary(person)
# return person; This tells python once the arguments are given for
# function to operate return the output as the dictionary 'person'.
# 3)Finally We call the fucntion(build_person("Creative","Fit")) and
# store the call into the variable(avatar) then print;print(avatar);
# -------------------------------------------------------------------------
# Adding Another key:value pair to the dictionary 'person'
# EX:Adding a persons 'age':
print("\n3a)Adding A Keys:Value Pair To The Dictionary(person) Using Function:")


def build_person(minds, body_types, age=""):
    """Returning a Dictionary"""
    person = {"Mind": minds, "Body Type": body_types}
    if age:
        person["Age"] = age
    return person


print("-With out 'age': ")
avatar = build_person("Creative", "Fit")
print(avatar)
print("-With 'age': ")
avatar = build_person("Creative", "Fit", 18)
print(avatar)
# Explaining
# 1)First we define a function(build_person) with three parameters:
# (minds, body_types,age='')
# 1a)age='';The 'age' parameter has a empty string because it is a simple way
# of making the age argument optional
# 2)The indented pieces of code:
# 2a)"""Returning a Dictionary""";This docstring tells you what the function
# does.
# 2b)person = {"Mind": minds, "Body Type": body_types}; is the dictionary that
# stores the arguments for the parameters'minds, body_types, and/or age='' as the
# values for keys("Mind","Body Type", and/or "Age")
# 2c)if age:;Tells python if there is a 'age' argument given for parameter (age='')
# then add the key("Age") and the argument from the function call as the value(=age)
# 2d)return person; Tells python to return the format of the dictionary(person) with or
# without the 'age' to the function call(avatar = build_person()).
# Finally We call the function(avatar = build_person("Creative", "Fit",18))
# with 'age' argument to see if a new key-value pair will be added then print
# variable(avater)
# -------------------------------------------------------------------------
# Using A Function With A While-Loop
print("------------------------------------------")
# -------------------------------------------------------------------------
# Using Function 'formatted_name' in a 'while-loop'
# EX:
def formatted_name(first_name, last_name):
    """Formatting a name"""
    full_name = first_name + " " + last_name
    return full_name.title()


# while True:
#    print("\nPlease tell me your name.")
#    f_name = input("First Name: ")
#    if f_name == "quit":
#        break
#    l_name = input("Last Name: ")
#    if l_name == "quit":
#        break
#    formatted = formatted_name(f_name, l_name)
#    print("\nHello," + formatted + "!")

# Explaining:
# 1)First we define a function named 'formatted_name' which takes the
# first_name and last_name arguments and store them in variable
#'full_name'.
# 1a)full_name = first_name + " " + last_name;Tells python to format the arguments for
# these parameter(first_name,last_name) in that style.
# 1c)return full_name.title();Tells python to  return this format with .title() method
# back to the 'fucntion call'
# 2)We then create a While-loop(while True:) to run(True) as long as the condtions
# are met in the indented pieces of code.
# 3)The indented pieces of code:
# 3a)print("\nPlease tell me your name.");Prompts the user to get ready to
# type in there name.
# 3b)f_name = input("First Name: ");The variable 'f_name' stores the value
# from the users input of there first name(input("First Name: ")).
# 3c)if f_name =='quit':;Tells python if the users input stored in
# variable(f_name) is equal to 'quit' then end(break) the program
# 3d)l_name = input("Last Name"); Tells python to store the users input
# for there last name in variable 'l_name'.
# 3e)if l_name =='quit':;Tells python if the users input is equal to
#'quit' then end(break) the program.
# 3g)formatted = formatted_name(f_name,l_name);This piece of code stores
# the function call(formatted_name(f_name,l_name)) into variable 'formatted'
# NOTE:SINCE (f_name,l_name) ARE USERS INPUT WE JUST NEED THE VARIABLES NAME
# OF WHERE THE STORED DATA IS(f_name,l_name)
# print("\nHello," + formatted + "!");The print statement tells python to
# print "Hello" to the name that the user gives us.
# -------------------------------------------------------------------------
# Passing A List Through A Function Call
print("------------------------------------------")
# -------------------------------------------------------------------------
# EX:
def greeting(names):
    """Printing A greeting for Each user"""
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)


guest = ["josh", "eric", "steven", "paul"]
print("1)Passing A List Through A Function Call:")
greeting(guest)
# Explaining:
# 1)First We define a function(greeting) with one parameter(names)
# 2)The indented peices of code:
# 2a)"""Printing A greeting for Each user""";This is a docstring
# that tells python what the function does.
# 2b)for name in names:;This 'for-loop' loops through all the
# items in the list(names) and stores them in temp variable 'name',
# then prints out  a greeting message:
# ( msg = "Hello," + name.title() + "!") for each element in the list
# 3)Then we create a list of names(guest = ['josh','eric','steven','paul']);
# to put into the fucntion call(greeting(guest)) so the fucntion can print a greeting for
# each name in the list(guest)
# -------------------------------------------------------------------------
# Modifying A List In A Function Call
# -------------------------------------------------------------------------
# Creating two functions to simulate a company that creates phone cases.
# EX:
print("\n1a)Modifying A List In A 'Function Call'. ")
unprinted_design = ["robot", "dragon", "wolf"]
finished_cases = []
#     Function (  parameter#1  ,  parameter#2)
def print_cases(unprinted_design, finished_cases):
    """Simulate printing each design,until none left,
    then move each element from one list to the other"""
    while unprinted_design:
        current_design = unprinted_design.pop()
        print("Printing Design: " + current_design.title())
        finished_cases.append(current_design)


#    Function      (  parameter#1 )
def compeleted_list(finished_cases):
    """Showing all the the elements in finished_cases"""
    print("\nThe following orders are done: ")
    for finished_case in finished_cases:
        print("-" + finished_case)


# Function ( Argument#1     ,  Argument#2   )
print_cases(unprinted_design, finished_cases)
#  Function    (  Argument#1  )
compeleted_list(finished_cases)
# Explaining:
# 1)We first create a list of unfinished_designs and give the
# list three values(["robot", "dragon", "wolf"])
# 2)Then we create a empty list to store all the 'finished_cases'
# ********
#  The 'print_cases()' function:
# ********
# 1)First we define a function named 'print_cases' with two parameters:
# (unprinted_design,finished_cases)
# 2)The indented pieces of code:
# 2a)The comment(docstring) tells you what the function does.
# 2b)while unprinted_design:;This while-loop tells python to run
# as long as there are elements in the list(unprinted_design).
# The indented lines within the while-loop:
# 3)current_design = unprinted_design.pop(); Tells python to pull
# all the elements from the end of the list(unprinted_design) with the pop() method
# and store the elements into 'current_design'
# 3a)print("Printing Design: " + current_design.title());Tells python
# to print each value in the variable 'current_design'
# 3b)finished_cases.append(current_design);Tells python to add all the
# values in variable 'current_design' to the end of the list 'finished_cases'
# using the .append method
# ****************
# The compeleted_list() function
# ****************
# 1)First we define the function 'compeleted_list' with
# one parameter(finished_cases)
# 1a)The parameter 'finished_cases' tells python to use the
# items in the list(finished_cases) to generate a print statement
# using the items.
# 2)The indented pieces of code:
# 2a)"""Showing all the the elements in finished_cases""";Tells us
# what the function does.
# 2b) print("\nThe following orders are done: ");Tells python to print
# this print statement when 'compeleted_list' is called.
# 2c)for finished_case in finished_cases:;This 'for-loop' tells
# python for every item in 'finished_cases' store them in temporary
# variable 'finished_case'  and print them in this style:
#'("-" + finished_case)'
# ----------------------------
# Calling the functions :
# 1)print_cases(unprinted_design, finished_cases)
# 2)compeleted_list(finished_cases)
# -------------------------------------------------------------------------
# Preventing A Function From Modifying A List
# -------------------------------------------------------------------------
# How to copy a list with slicing in a function call:
# EX:If we didnt want for 'unprinted designs' to be empty after using the pop() method
# print("\nCopying a list in a function call:")
# print_cases(unprinted_design=[:],finished_cases)
# Explaining:
# Now when the pop() method is used in the function 'print_cases'
# it only uses a copy '[:]' of the list(unprinted_design) so instead
# being empty after using the pop() method ,'unprinted_design' still
# has all of its elements.
# =========================================================================
#         INTRO TO PASSING A 'ARBITRARY' NUMBER OF ARGUMENTS
print("      ==========================================")
print("   INTRO TO PASSING A 'ARBITRARY' NUMBER OF ARGUMENTS")
print("      ==========================================")
# =========================================================================
# Arbitrary-determined by chance,whim,or impluse,and not by necessity,
# reason,or princple.
# -------------------------------------------------------------------------
# NOTE:The asterisk(*) before a  parameters name when defining a function tells
# python to make a empty 'tuple' called the parameters name and to  pack
# what ever arguments it receives from the function call into that parameter.**
# -------------------------------------------------------------------------
# EX:
#   Function  (Parameter)
def make_pizza(*topping):
    """Printing A List Of Toppings"""
    print(topping)


print("1)Passing A Arbitrary Number Of Arguments:")
# Function (               Arguments                   )
make_pizza("turkey", "mushrooms", "exta-cheese", "peppers")
# Function (Argument)
make_pizza("turkey")

# Explaining:
# 1)First we define a function(make_pizza) with one parameter(*topping):
# 1a)(*topping):;Tells python for this parameter(*topping) accept as many
# arguments thats provided in the function call(make_pizza()) and store them into
# the empty tuple 'topping'.
# 2)The indented pieces of code:
# 2a)"""Printing A List Of Toppings""";This docstring tells you what the
# function does.qu
# 2b)print(topping);The print statement tells python to print every
# argument in the tuple  '*topping'.
# 3)The two function calls(make_pizza()) shows you the different amounts
# of arguments this function can accept:
# 3a)make_pizza("turkey","mushrooms","exta-cheese","peppers")
# 3b)make_pizza("turkey")
# -------------------------------------------------------------------------
# Changing The Print Statement To A For-Loop in Function 'make_pizza()'
# EX:
print("\n1a)Using A 'for-loop' In Function 'make_pizza' Instead Of Just 'print()'.")


def make_pizz(*topping):
    """Printing A List Of Toppings"""
    print("The List Of Made Pizzas:")
    for made_pizzas in make_pizz:
        print("-" + made_pizzas)


make_pizza("turkey", "mushrooms", "exta-cheese", "peppers")
# EX:
# 1)for made_pizzas in make_pizz:;THis for-loop tells python for
# every argument sent from the function call store in temporary
# variable(made_pizzas) and then print every element in this style:
# print("-" + made_pizzas).
# -------------------------------------------------------------------------
print("------------------------------------------")
# Using Arbitrary Keyword Arguments
# -------------------------------------------------------------------------
# The function build_profile() always takes the first and last name but
# it accepts an arbitrary number of keyword arguments as well.
# EX:
print("\n1b)Using Abritrary Number Of Keyword Arguments:")


def build_account(first, last, **user_info):
    """Building a dictionary containing 
       everything about the users account"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_account(
    "albert", "einstein", location="princeton", field="physics",
)
print(user_profile)
# Explaining
# 1)First we define a function(build_account) with three
# parameters(first,last,**user_info):
# 1a)**user_info;This parameter tells python to create a empty dictionary
# called 'user_info' and to pack whatever arugments you recieve from the
# function call(build_account()).
# 2)The indented peices of code:
# 2a)The docstring tells you what the function does.
# 2b)profile = {};This tells python to create a empty dictionary called
#'profile'
# 2c)profile["first_name"] = first;This tells python for dictionary
#'profile' create a key(first_name) and as the value the parameter
#'first'
# 2d)profile["last_name"] = last;This tells python to create a
# key("last_name") and  as the value the  parameter 'last' in
# dictionary 'profile'.
# 2c)for key, value in user_info.items():;Seeing how the double-
# asterick(**) tells python to create a dictionary called "user_info"
# we uses two temporary only to sperate the keys and values.
# The indented pieces of code in the for-loop:
# 3)profile[key] = value;This tells python to add all the items into
# the dictionary 'profile' with there key as the key  and  there value
# as the value.
# *******
# Explaining the function call stored in variable 'user_profile':
# build_account(
#    "albert", "einstein", location="princeton", field="physics",)
# 4)The arugment  "albert";Is stored as the parameter 'first' then assigned as value for the
# key 'First_name ' in dictionay 'profile'  :
# profile["first_name"] = first
# 4a)the argument "einstein"; Is stored as in parameter 'last' then assigned as the value for
# key 'last_name' in dictionary 'profile':
# profile["last_name"] = last
# 4b)location="princeton";This is a keyword argument which tells python to
# store the key'location' and the value'princeton' into dictionary(profile).
# 4c)field="physics";This also a keyword argument which tells python to
# store the key'field' and the value 'physcis' into the dictionary 'profile'.
# NOTE:YOU CAN MIX POSITIONAL,KEYWORD,AND ARBITRARY ARGUMENTS IN MANY DIFFERENT
# WAYS WHEN WRITTING YOUR OWN FUNCTION.
# ------------------------------------------------------------------------
