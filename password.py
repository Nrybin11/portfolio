import random

n = input('What length do you want your password to be? \n')

upperCaseLetter = chr(random.randint(65, 90))
lowerCaseLetter = chr(random.randint(97,122))
numberChar = chr(random.randint(48,57))
specialChar1 = chr(random.randint(33,47))
specialChar2 = chr(random.randint(58,64))


print(upperCaseLetter, lowerCaseLetter, numberChar, specialChar1, specialChar2)

