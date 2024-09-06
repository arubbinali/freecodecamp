"""
بسم الله الرحمان الرحيم


https://www.youtube.com/watch?v=rfscVS0vtbw
 02:41:20 of 04:27:04
"""
from math import *
"""
------------
Vocabulary
------------
1. Render > Provide
2. Assign > Allocate or designate aside (for a specific purpose)
3. Declare > Statement or Announcement
4. Append > Add (in a list or group or the like)
5. Concatenation > Process of taking a string and appending another string onto it
6. Specify > To define or indicate a particular value, variable, or condition within a function or expression
7. Index > A position number used to access elements in a sequence like a list, tuple, or string
8. Character > A single symbol or letter from a string
9. Modify > To change or update the value of a variable, data structure, or object
10. Immutable > A property of data types (e.g., strings, tuples) where their value cannot be changed after creation
11. Function > A collection of code which performs a specific task and later can be called when required
12. Parameter > A piece of information that we give to the function (Reserved)
13. Dictionary > A special structure in Python which allows us to store information in key value pairs
14. Key > Key to the definition of a specific
15. While Loop > Repeats a bunch of code until a certain given condition is false
16. For Loops > Loops over different collections of items
17. Exponent Function > Raises a certain number to a specific power
------------
Formulae
------------
1) print
2) Assign variables
3) Comma and Addition sign difference when included in print statements
4) Data Types: String, Boolean, Float, Real, Char
5) /n [Next line]
6) /" [BackSlash before quotation mark to use quotation marks in a print statement]
7) Add 2 statements by "+" or ","
8) .upper() > Convert text to upper case
9) .lower() > Convert text to lower case
10) .isupper() > Get to know of text is upper case or not, response is boolean
11) .islower() > Get to know of text is lower case or not, response is boolean
12) .upper().isupper() / .upper().islower() > Convert text to upper case and see if it's upper or not
13) .lower().islower() / .lower().isupper() > Convert text to lower case and see if it's lower or not
14) len() > To get the length of the phrase or sentence or text
15) Index starts from 0 and this corresponds to Place 1 [Use squared brackets and specify the index number in em to access that value]
16) .replace > Replace certain words or letters [2 Parameters given, replace the old with new by .replace(x,y)]
17) ** > Raise to the power
18) // > Answer excluding the remainder
19) % > Remainder
20) str() > Convert data type of a variable to String
21) abs() > Absolute a number, abs(-5) = 5
22) pow() > Power, pow(2,3) = 8
23) max & min > Gets the max/min number of all from a list of numbers
24) round() > Rounds number, round(3.2) = 3
25) floor() > Rounds number down, Removes the part of the number after the decimal point, floor(4.7) = 4
26) ceil() > Rounds number up, ceil(4.2) = 5
27) sqrt() > Square Root
28) input() > give a prompt and store the value in a variable
29) Lists() > Index starts from 0, but when opposite(right to left), then starts from -1
30) Calling List >  To call index 0, 1 and 2, we use 0:3! Basically, one more index value to cover the range
31) .extend() > To extend a list by another list or elements (Multiple elements)
32) .append() > Append (Add) an element in a list (Single element)
33) .insert() > Insert an element by specifying index number and then element, rest push ahead, .insert(2, "Arub")
34) .remove() > Remove an element in "" in a list
35) .clear() > Clears the list
36) .pop() > Excludes the last element of a list
37) .index() > Enter element and get to know the index value
38) .count() > Count number of same elements in the list
39) .sort() > Sorts the elements of a list in lexicographical order if strings, or ascending order if numbers
40) .reverse() > Reverses the order of arrangement 
41) .copy() > Copies the entire list
42) Tuples use parenthesis instead of squared brackets and elements are immutable
43) def > Define a function
44) return > allows us return a value back to the caller, any instruction after return will not be executed, breaks out of code(function)
45) if > Start a condition
46) elif > Else if during a condition
47) else > Else, if all conditions above are false
48) or > Or between 2 conditions, either is true
49) and > And between 2 conditions, both are true
50) not() > Negates the statement/instruction/other in the parenthesis
51) == > Check if left hand condition equals right hand condition, single = is to assign a value
52) != > Not equals to, used in assigning and checking both
53) {} > Content of a dictionary is inside of these curly brackets 
54) .get() > Pass in name of the key to get its value. If key undefined, replies with "None", also, assign a default value after comma
55) += > += is the same as x = x + 1, basically increment of 1
56) range(x,y) > x is start, y is stop, but y will not be included

"""


array = ["a", "b", "c"]
array.remove(array[0:2])
print(array)


"""
#Setup & Hello World
print("Arub")

#Drawing Shapes
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#VARIABLES AND DATA TYPES-------------------------------------------------------
name = "Arub"
print("I am", name)
print("I am " + name) #Space needed after text ends if addition is used
#Data Types > String, Boolean, Float, Real, Char

#WORKING WITH STRINGS-------------------------------------------------------
    #\n & Quotations b/w text
print("Arub")
print("Arub\nbin Ali") #Next line
print("Arub said: \"Wassup\"") #Use a quotation mark b/w text, BackSlash before quotation mark

    #Concatenation
phrase1 = "Arub is a trouble maker"
print(phrase1 + " , is true")

    #OR

phrase2 = "Arub is a trouble maker"
print(phrase2, ", is true")

    #Convert Text to upper or lower case
phrase3 = "Arub is OverConfident"
print(phrase3.upper())
print(phrase3.lower())

    #Get to know if text is upper or lower case, response will be in boolean form
phrase4 = "Arub is OverConfident"
print(phrase4.isupper())
print(phrase4.islower())

phrase5 = "I DONT KNOW WHAT PROBLEM ARUB IS"
print(phrase5.isupper())
print(phrase5.islower())

phrase6 = "i dont know what problem arub is"
print(phrase6.isupper())
print(phrase6.islower())

    #First convert text, then "Get to know if text is upper or lower case, response will be in boolean form"
phrase7 = "I dont know what problem Arub is"
print(phrase7.upper().isupper())
print(phrase7.upper().islower())
print(phrase7.lower().isupper())
print(phrase7.lower().islower())

    #Get length of a text
phrase8 = "I dont know what problem Arub is"
print(len(phrase8))

    #Extract one of the characters from a string by entering index in 2 squared brackets
phrase9 = "I dont know what problem Arub is"
print(phrase9[0])

    #Use .index function, tells us where a specific character or string is a located in a string
phrase10 = "Arub is OverConfident"
print(phrase10.index("i"))
print(phrase10.index("Confi"))
print(phrase10.index("O"))

    #2 Parameters given, replace the old with new by .replace(x,y)
phrase11 = "Arub is OverConfident"
print(phrase11.replace("OverConfident", "Trouble Maker"))
print(phrase11.replace("Ar", "N"))
print(phrase11.replace("Arub is", "I am"))


#WORKING WITH NUMBERS-------------------------------------------------------
print(2)
print(2.0235)
print(-2.0235)
print(3+4)
print(3-4.234)
print(3*4)
print(3/4)

    #Raise to the power, Rem, Removed Rem
print(2**4)
print(13//4)
print(13%4)

    #String
num = 5
print(str(num), "is a number")

    #Absolute
negativeNum = -5
print(abs(negativeNum))

    #Power
print(pow(2, 3))

    #Max & Min
print(max(34, 234))
print(max(2, 3, 99, 2323, 4, 0.44))
print(min(34, 234))
print(min(2, 3, 99, 2323, 4, 0.44))

    #Max & Min with lists
list1=[23,29,34,45,1,32]
print(min(list1))
print(max(list1))

    #Round
print(round(3.2))
print(round(3.5))

    #Floor
print(floor(4.5))
print(floor(24.0024))
print(floor(434.745))

    #Ceil
print(ceil(4.5))
print(ceil(24.0024))
print(ceil(434.745))

    #Square Root
print(sqrt(9))


#GETTING INPUT FROM USERS-------------------------------------------------------

    #Strings
myname = input("Enter your name:   ")
myAge = input("Enter your age:   ")
print("Your name is", myname, "and you are", myAge)


#BUILDING A BASIC CALCULATOR-------------------------------------------------------
    #Integers & Float
num1 = input("Enter number 1:   ")
num2 = input("Enter number 2:   ")

sum1 = int(num1) + int(num2)
print("The sum of the two numbers is", sum1)
sum2 = num1 + num2
print("The sum of the two numbers is", sum2)

#MAD LIBS GAME-------------------------------------------------------
print("Roses are Violet")
print("Violets are blue")
print("I love you")

color = input("Enter a color:   ")
pluralNoun = input("Enter a Plural Noun:   ")
celebrity = input("Enter a celebrity:   ")

print("Roses are", color)
print(pluralNoun, "are blue")
print("I love", celebrity)


#LISTS-------------------------------------------------------
developers = ["Arub", "Shariq", "Umar"]
print(developers)
print(developers[0])
print(developers[2])
print(developers[-1])
print(developers[0:3]) #To call index 0, 1 and 2, we use 0:3! Basically, one more index value to cover the range

    #Modifying
developers[0] = "Me"
print(developers[0])


#LIST FUNCTIONS-------------------------------------------------------
    #Extend
numbers = [3, 4, 42, 17, 52, 9]
developers = ["Arub", "Shariq", "Umar"]
print(developers)
developers.extend(numbers)
print(developers)

    #Append
developers.append(1000)
print(developers)

    #Insert
developers.insert(1, "Shrek")
print(developers)

    #Remove
developers.remove("Shrek")
print(developers)

    #Clear
developers.clear()
print(developers)

    #Pop
people = ["Arub", "Shariq", "Umar"]
people.pop()
print(people)

    #Index
print(people.index("Shariq"))

    #Count
people2 = ["Arub", "Arub", "Arub", "Umar", "Umar"]
people.extend(people2)
print(people.count("Arub"))

    #Sort
people.sort()
print(people)

numbers.sort()
print(numbers)

    #Reverse
people.reverse()
print(people)
numbers.reverse()
print(numbers)

    #Copy
people2 = people.copy()
print(people)
print(people2)


#TUPLES-------------------------------------------------------
coordinates = (4, 5)
print(coordinates[1])


#FUNCTIONS-------------------------------------------------------
def message(name, age):
    print("Halla", name, "you are", age)
message("Arub", "16")
message("Shariq", "15")
message("Umar", "15")


#RETURN STATEMENT-------------------------------------------------------
def cube(number):
    return number*number*number

print(cube(3))

def cube(number):
    return number*number*number

result = cube(4)
print(result)


#IF STATEMENT-------------------------------------------------------
male = True
tall = False

if male and tall:
    print("You are male or tall or both")
elif male and not(tall):
    print("You are a short male")
elif not(male) and tall:
    print("You are a tall female")
else:
    print("You are neither male nor tall")


#IF STATEMENTS AND COMPARISONS-------------------------------------------------------
def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print(max_num(3, 14, 5))


#BUILDING A BETTER CALCULATOR-------------------------------------------------------
number1 = float(input("Enter first number:   "))
op = input("Enter operator:   ")
number2 = float(input("Enter second number:   "))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
else:
    print("Invalid operator")


#DICTIONARIES-------------------------------------------------------
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr:": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Mar"])
print(monthConversions.get("Sep"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))



#WHILE LOOPS-------------------------------------------------------
i = 1
while i <= 10:
    print(i)
    i = i + 1

    

#BULDING A GUESSING GAME-------------------------------------------------------
secret_word = "coffee"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess:   ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses == True:
    print("Out of guesses! YOU LOSE!")
else:
    print("You win!")


#FOR LOOPS-------------------------------------------------------
friends = ["Arub", "Shariq", "Umar"]
for friend in friends:
    print(friend, friends)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first iteration")


#EXPONENT FUNCTION-------------------------------------------------------
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))


#2D LISTS & Nested Loops-------------------------------------------------------
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#Numbers in ascending order
a = (1, 11, 2, -34, 944)
x = sorted(a)
print(x)
#Numbers in descending order
b = (1, 11, 2, -34, 944)
x = sorted(b, reverse=True)
print(x)
#Alphabets in ascending order
c = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(c)
print(x)
#Alphabets in descending order
d = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(d, reverse=True)
print(x)
"""