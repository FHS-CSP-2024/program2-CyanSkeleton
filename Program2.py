# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input("What is your name?\n\t")
print(name)
print(name)


print()
## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
name = input("What is your name?\n\t")
print("!" + name + "!" + name + "!")

print()
## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
name = input("What is your first and last name?\n\t")
nameArray = name.split()
streetAddress = input("What is your street address?\n\t")
capc = input("What is your city and postal code?\n\t")
print("First name: " + nameArray[0])
print("Last name: " + nameArray[1])
print("Street Address: " + streetAddress)
print("City and postal code: " + capc)

print()
## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
threeWords = input("Give me 3 words?\n\t")
wordArray = threeWords.split()
print(wordArray[0] + "-" + wordArray[1] + "-" + wordArray[2])

print()
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
name = input("What is your name\n\t")
print("this is a completely original game by the big game studio bugthesda")
print(name + " is a guy being executed by the imperial empire")
print(name + " escapes and kills a dragon and learns that they have magic powers")
print("then " + name + " finds a secret organization dedicated to killing dragons")
print("they have to stop a dragon from reviving dragons and causing the end of the world")
print(name + " meets with a wise peaceful dragon that teaches them how to beat the evil dragon")
print(name + " then kills the evil dragon and saves the world")
