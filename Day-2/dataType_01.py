
# ⁡⁢⁣⁢𝗙𝗼𝗿𝗺𝗮𝘁𝘁𝗲𝗱 𝗦𝘁𝗿𝗶𝗻𝗴 𝗟𝗶𝘁𝗲𝗿𝗮𝗹𝘀 (𝗳""):
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 𝗰𝗵𝗮𝗿𝗔𝘁 (𝗜𝗻𝗱𝗲𝘅𝗶𝗻𝗴 𝗮 𝗦𝘁𝗿𝗶𝗻𝗴):

my_string = "Hello, World!"
char_at_index_7 = my_string[7]
print(f"Character at index 7: {char_at_index_7}")

# 𝗨𝗽𝗽𝗲𝗿 𝗮𝗻𝗱 𝗟𝗼𝘄𝗲𝗿 𝗖𝗮𝘀𝗲:

text = "Python Programming"
upper_case_text = text.upper()
lower_case_text = text.lower()
print(f"Original: {text}\nUppercase: {upper_case_text}\nLowercase: {lower_case_text}")


# 𝗦𝘁𝗿𝗶𝗽 (𝗥𝗲𝗺𝗼𝘃𝗲 𝗟𝗲𝗮𝗱𝗶𝗻𝗴 𝗮𝗻𝗱 𝗧𝗿𝗮𝗶𝗹𝗶𝗻𝗴 𝗪𝗵𝗶𝘁𝗲𝘀𝗽𝗮𝗰𝗲𝘀):
input_string = "   This is a string with whitespaces.   "
stripped_string = input_string.strip()
print(f"Original: '{input_string}'\nStripped: '{stripped_string}'")


# 𝗥𝗲𝗽𝗹𝗮𝗰𝗲
sentence = "I like cats, but I prefer dogs."
updated_sentence = sentence.replace("cats", "rabbits")
print(f"Original: '{sentence}'\nUpdated: '{updated_sentence}'")

# 𝗦𝗽𝗹𝗶𝘁 𝗮𝗻𝗱 𝗝𝗼𝗶𝗻:
csv_data = "apple,orange,banana,grape"
list_of_fruits = csv_data.split(",")
joined_fruits = "-".join(list_of_fruits)
print(f"Original CSV: '{csv_data}'\nList of Fruits: {list_of_fruits}\nJoined with '-': '{joined_fruits}'")


# 𝗶𝗻 𝗮𝗻𝗱 𝗻𝗼𝘁 𝗶𝗻

# Exercise: Membership Test

# Task 1: Check if 'elephant' is present in the given string.
my_string = "The quick brown fox jumps over the lazy dog."
# Your code here
if 'elephant' in my_string:
    print("'elephant' is present in the string.")
else:
    print("'elephant' is not present in the string.")

# Task 2: Check if the number 7 is present in the given list.
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
# Your code here
if 7 in numbers:
    print("The number 7 is present in the list.")
else:
    print("The number 7 is not present in the list.")

# Task 3: Check if the word 'apple' is not present in the given sentence.
sentence = "I like bananas and oranges, but not apples."
# Your code here
if 'apple' not in sentence:
    print("'apple' is not present in the sentence.")
else:
    print("'apple' is present in the sentence.")






# Integer and float examples
integer_number = 5
float_number = 2.5

# Basic arithmetic operations
addition_result = integer_number + float_number
subtraction_result = integer_number - float_number
multiplication_result = integer_number * float_number
division_result = integer_number / float_number

print(f"Addition: {integer_number} + {float_number} = {addition_result}")
print(f"Subtraction: {integer_number} - {float_number} = {subtraction_result}")
print(f"Multiplication: {integer_number} * {float_number} = {multiplication_result}")
print(f"Division: {integer_number} / {float_number} = {division_result}")

# Built-in functions
absolute_value = abs(subtraction_result)
rounded_result = round(division_result, 2)

print(f"Absolute Value of Subtraction Result: {absolute_value}")
print(f"Rounded Division Result: {rounded_result}")

# Using the math module for advanced functions
import math

sqrt_result = math.sqrt(integer_number)
power_result = math.pow(integer_number, 2)
sin_result = math.sin(math.radians(90))  # Converting degrees to radians for trigonometric functions

print(f"Square Root of {integer_number}: {sqrt_result}")
print(f"{integer_number} to the Power of 2: {power_result}")
print(f"Sine of 90 degrees: {sin_result}")

