a= 34
b = 45
c = 34>45
print (c)

print (type (c))
d = 10>=20
print(d )

number = input("enter number")
print ('square of', number, 'is', int(number)* int(number))
name= 'Abhishek,Pundeer'
print (name)
#  to print a character from a string
print (name [0])
print (name [1])

 
# strings slicing
print (name [7])

print (name[0:8])

print (len(name)) 

print (name [-7:-2])

nm = 'harry bhai'
print (nm [-4:-2])
#  to check how many character in a sting
for character in nm:
 print (character)

#  to know the lenght of the variable
print (len(nm))
#  changing strings into uppper case
print (nm.upper())


# replace strings
a= 'abhishek,pundeer'
print (a.replace ("shek","nav"))


# split:
# split is used for spliting strings into list

print (a.split(" "))


# center() :
# The center() method aligns the string to the center as per the parameters given by the user.

# Example:
str1 = "Welcome to the Console!!!"
# print(str1.center(50))
# Output:
#             Welcome to the Console!!!
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.

# Example:
# str1 = "Welcome to the Console!!!"
# print(str1.center(50, "."))
# Output:
# ............Welcome to the Console!!!.............

# count () :
# count ()  . we use this method to know how many times a value has occured 

print (a.count ("e"))

# endswith() :

# endswith(): we use this to check if the string ends with the given value

print(a.endswith("r"))
print(a.endswith(' '))

# We can even also check for a value in-between the string by providing start and end index positions.

str1 = "Welcome to the Console !!!"
print(str1.endswith("to" ,0, 10))

print(a.endswith("er",0,16))


# find() :
# the find() :method searches for the first occurrence of the given value and returns the index where it is present.
#  If given value is absent from the string then return -1.
print(a.find('p'))


# index() :
# The index() :method searches for the first occurrence of the given value and returns the index where it is present. 
# If given value is absent from the string then raise an exception.

ab = 'abhishek is a man'
print(ab.index('is'))
print(ab.index('man'))

# As we can see, this method is somewhat similar to the index() method.
#  The major difference being that index() raises an exception if value is absent whereas find() does not.


# isalnum() :
# The isalnum() : method returns True only if the entire string only consists of A-Z, a-z, 0-9.
#  If any other characters or punctuations are present, then it returns False. Even it has space in it

b = 'Abhishek'
print(b.isalnum())


# isalpha() :
# The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(b.isalpha())


# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(b.islower())
print(ab.islower())


# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
#  print ('hii my name is Abhishek\n')   here we have added (\n ) so now it is not a printable variable
print(b.isprintable())


# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# Example:

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())


# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# Example:
str1 = "World Health Organization" 
print(str1.istitle())





# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

# Example :
str = "WORLD HEALTH ORGANIZATION" 
print(str.isupper())



# startswith() :
# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.

# Example :
st = "Python is a Interpreted Language" 
print(st.startswith("Python"))




# swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# Example:
s = "Python is a Interpreted Language" 
print(s.swapcase())
# Output:
# pYTHON IS A iNTERPRETED lANGUAGE




# title() :
# The title() method capitalizes each letter of the word within the string.

# Example:
s1 = "He's name is Dan. Dan is an honest man."
print(s1.title())
# Output:
# He'S Name Is Dan. Dan Is An Honest Man.