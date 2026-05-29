This is the Pyton programming class.

# String variables can hold text data;concatenation is the process of combining strings
first_name = "Balaji"
last_name = "Bondar"

full_name = first_name + " " + last_name
len(full_name)
print(full_name)

# Boolean variables can only be True or False
has_permission = True
print(has_permission)

is_admin = False
print(is_admin)


# Output: You are eligible to drive.
age = 25
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# This code demonstrates the use of f-strings in Python to create a formatted string.
first_name = "Balaji"
output_string = f"Hello, {first_name}!"
print(output_string)


# String fuctions
first_name = "John"

first_name = first_name.upper()
first_name = first_name.lower()
first_name = first_name.capitalize()
first_name  = first_name.title()


# find and replace function
sentence = "The quick brown fox jumps over the lazy dog"
sentence.replace("fox", "cat")
sentence.find("fox")
sentence.count("brown")


# if-else statement
temperature = 30
if temperature > 25:
    print("It's a hot day")
else:
    print("It's a cold day")

# if-elif-else statement
temperature = 15
if temperature > 25:
    print("It's a hot day")
elif temperature > 15:
    print("It's a warm day")
else:
    print("It's a cold day")


# loops in python
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)

    # data structures
age = 30
has_license = True

my_list = ["Balaji", age, 25, has_license]
my_list[0] = "Balaji Bondar"
my_list.append("Python Developer")

person = {"name": "Balaji Bondar", "age": 30, "has_license": True}

person["age"] = 31
person["profession"] = "Python Developer"

number_set = {1, 2, 3, 4, 5}
number_set.add(6)
number_set.remove(3)


def add_numbers(a, b):
    # 'a' and 'b' are parameters
    return a + b

# 5 and 3 are arguments passed to the function
result = add_numbers(5, 3)
print(f"Sum: {result}")  # Output: Sum: 8




