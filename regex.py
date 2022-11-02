import re


# It is possible to use re libriary for substitution of characters in a string
string = 'I do not LOVE OLGA'
print(re.sub('[a-z]', '', string))
# Output:
# I   LOVE OLGA
print(re.sub('[^A-Z]', '', string))
# Output:
# ILOVEOLGA