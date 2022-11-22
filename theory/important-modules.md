# Important python modules:

## Regex (used for substitution of characters in a string)

```python
import re


# It is possible to use re libriary for substitution of characters in a string
string = 'I do not LOVE OLGA'
print(re.sub('[a-z]', '', string))
# Output:
# I   LOVE OLGA
print(re.sub('[^A-Z]', '', string))
# Output:
# ILOVEOLGA
```

## Random
```python
import random


# randrange()
# Generates a random number in a range between lowest and highest-1
num = random.randrange(10, 15) # Will return random int number from 10 to 14
print(num)
# Possible to set a step
num = random.randrange(10, 20, 3) # Will return random int number such as 13, 16, 19
print(num)

# Randint()
# Same but inclusive
num = random.randint(10,15) # Will return random int from 10 to 15
print(num)
# Cannot initialise step

# choice()
# Random element from a given sequence
num = random.choice(['A', 'B', 'C'])
print(num)

# choices()
# Random selection from the given sequence
num = random.choices(['A', 'B', 'C', 'D', 'E'])
print(num)

# shuffle()
# Returns a sequance in a random order
list = ['A', 'B', 'C']
random.shuffle(list)
print(list)

# sample()
# returns a sample of a custom length from given sequence
print(random.sample(list, 2))

# random()
# returns random float between 0 and 1
print(random.random())

# uniform()
# returns random float between 2 parameters
print(random.uniform(2, 6))

# And more complex, which are used in statistics ....
```

## Fernet (symmetric key encryption)
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('file.txt', 'rb') as file:
    contents = file.read()
    
with opeb('file.txt', 'wb') as file:
    file.write(Fernet(key).encrypt(contents))
    
# To decrypt
with open('file.txt', 'rb') as file:
    contents = file.read()
    
with opeb('file.txt', 'wb') as file:
    file.write(Fernet(key).decrypt(contents))
```
