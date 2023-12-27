# """
# 1.1. Write a Python program that takes user input for their first name, last name, and age.
# Then, use an f-string to print a message in the format: "Hello,[first name] [last name]! 
# You are [age] years old."
# """

# name=input("enter your name ")
# lastName=input("enter your last name ")
# age=input("enter your age ")
# print(f"hey my name is {name} and the last name is {lastName} and age is {age}")

# """
# 1.2. Create a function that accepts the name and profession of a person as arguments and returns an 
# f-string greeting them,such as "Greetings, [name]! As a [profession], you contribute to society."
# """
# name=input("enter your name: ")
# profession=input("enter your profession!!")


# def greetings(name="xyz", profession="doctor"):
#     getString = f"Hey, your name is {name} and your profession is {profession}"
#     return getString

# result = greetings()
# print(result)

# """
# 2.1. Given the string word = "Python", write a function that takes an index as an argument and prints
# the character at that index in the string.
# """


# word="python"
# checkCharIndex=int(input("enter index value:"))
# def check(checkCharIndex):
#     checkVal=word[checkCharIndex];
#     return checkVal;


# print(check(checkCharIndex))


"""
2.2. Create a program that prompts the user to enter a word and an index. Print the character at 
the specified index in the entered word.
"""

word=input("enter a word: ");
indexVal=int(input("enter the index val : "))

def wordAndIndex(word,indexVal):
     checked=word[indexVal];
     return checked;   


print(wordAndIndex(word,indexVal));



















