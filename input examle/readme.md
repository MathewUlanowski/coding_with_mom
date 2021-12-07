<!-- this is the actual raw readme file that is the behind the scenes that makes all the cool stuff at the bottom of the repo work -->
<!-- I say this because if your here at this repo your probably very new to coding in general and curious what this is -->

# Inputs and variable assignment
1. there is a function `input()` that will take an input from the console but it will only take the input as a string so be careful if your putting in integers as it is a string character of integers not a literal Integer
    ```python
    input("your input is? ")
    ```
    the above code would do something like this and be prompting you for an input
    ```bash
    your input is? |
    ```
    with variable assignment and print statments
    ```python
    name = input("what is your name? ")
    print("My name is " + name)

    # alternatively you could use an string literal AKA f string in python to do the same thing
    name = input("what is your name? ")
    print(f"My name is {name}")
    ```
* Strings can be concatinated but not added
* integers also called int can be added but not concatinated
```python
# adding two integers and the result
a = 5
b = 10
c = a + b
print(c)
# This would output 15
```
```python
# concatinating strings
a = "5"
b = "10"
c = a + b
print(c)
# This would output 510
```
* there is a convert function for converting int to string and string to int str(int) and int(str) respectively
    * keep in mind that a number can always be converted to a string
    * a string however may not be able to be converted to an int if it has any characters besides numbers in it 

    ```python
    # this would error out because this string has characters other than numbers
    x = "some string with an int 42"
    int(x)
    ```
    ```python
    # this will work fine because it has only numbers
    x = "42"
    int(x)
    ```
    ```python
    # this is an int and as such can always be converted to a string
    x = 456456
    str(x)
    ```
| Conversion | can it be done? |
|---|---|
| int -> str | always
| str -> int | only if string contains exclusively numbers
