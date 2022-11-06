# Imports are done at the top of the file and each module is imported at a new line
import os
import sys 
from sys import displayhook, last_type # import of components are done separated by comma
# There should be two blank lines after import statements

# Maximum number of characters in line is 79 characters

# Sometimes it is necessary to split parameters to keep code readable
def my_function(one, two, 
                three, four,
                five, six):
    print('Hello world')


# Should be 2 blank lines between functions
def second_function():
    pass


# Lists can also be splited in order to keep them readable
my_list = [1, 2, 3, 4, 5,
            6, 7, 8, 9, 10]

# There should be space after a comma
print('Hello', 'Hi')

# Math equations should have space around lower priority operators
x = 7*7 + 8*9

# If statements should not be written in one line
check = True

if check:
    print("It's true")

# Functions should be called on different lines
my_function()
second_function()
