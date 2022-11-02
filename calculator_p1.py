# Developing of the advanced python calculator by using eval()

# importing re for substitution of charachters in a string
import re


# Defining two global variables that are going to be used to perform calculations
# run will be used to control the while loop
# previous is to store the value of previous calculations
run = True 
previous = 0

print('Advanced Calculator')
print('Enter "q" to exit\n')

def do_math():
    global run
    global previous

    # User inputs an equation
    if previous == 0:
        equation = input('Please, enter the equation: ')
    else:
        equation = input(str(previous))

    # Check wether user wants to quit. If no, removes dangerous characters from the input
    if equation != 'q':
        equation = re.sub('[A-Z,a-z:;"]', '', equation)
        # Evals the equation
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)

    else:
        run = False


while run:
    do_math()