

# It is possible to pass an unlimited number of arguments to a function using *
def printer(*strings):
    for string in strings:
        print(string)

printer('My', 'Name', 'is', 'Ilya')
#Output:
#My
#Name
#is
#Ilya