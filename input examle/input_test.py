


# this line takes an input from the console 
# these two inputs will only take values of type string which in python can not be added they can be concatenated
from typing import cast


a = input("im nothing special but tell me what a is -> ") 
b = input("im also nothing special but tell me what b is -> ")


# this line here converts the strings of a and b before adding them together whitch allows them to be added like numbers so a + b 
# would be the sum of a + b instead of the string "ab" with a and b being what ever you type into the console respectively
c = int(a)+int(b)




# this prints out the sum however because we converted a and b to a number or more formally known as an integer or int for short
# we have to now convert c the sum of a nd b back to a string so taht it can be concatinated to the print statment
print("the value of a is " + a + " b is " + b + " and a + b is " + str(c))


# Optional tips and tricks below you could just as easily skip it if its confusing then please do skip it


# this is an f string or what is known as a string literal when you prefix a string with the letter f it becomes a string literal
# a string literal allows you to pass variables into the string between the { } and what is inside will be automatically converted
# to a string this is also why I personally prefer to use them rather than concatination but its a preference thing just remember
# though a normal string does not automatically convert int to string where a string literal does
print(f"the value of a is {a} the value of b is {b} and the sum of both a and b is {c}")

# you can also comput values inside of the inside of the { } of a string literal and after computed they will be converted to a string
# the "\n" is a special character for a new line I have 2 in a row because I want it two lines below the previouse print statements
# this is just because I want it to look like that. notice that I had to convert a and b to an integer before multiplying them this
# is because the a and b inputs from ealier are still a string so inside of the { } it can convert them to a string but it cannot convert
# them to an integer
print(f"\n\nthe product of a multiplied by b is {int(a) * int(b)}")







# definately ignore this unless your looking for something you havent yet learned

# this here is some special stuff using a function with the argument of a string that will input get and input of a string
# and convert and return it as an int so basically its an input() function that only takes integers and keeps asking your for
# input until you give it an integer but this is some special magical logic here 
def input_that_is_an_int(input_msg):
    string_of_int = input(input_msg)
    int_value = None
    while int_value == None:
        try:
            int_value = int(string_of_int)
        except:
            string_of_int = input(f"that value was not a number!\n{input_msg}")
    return int_value
d = input_that_is_an_int("What is the value of d? ")
e = input_that_is_an_int("What is the value of e? ")

print(f"\n\nthe sum of d and e is {d+e}")
print(f"the product of d and e is {d*e}")