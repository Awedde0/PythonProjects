# Python Variables and Type Casting

# Assigning multiple variables
name, age, height = "Arun", 10, 127

print(age)

# Assigning the same value to multiple variables
san = dan = "tippu"

print(dan)


# Type Casting
# Common data types: int, str, float, bool

age = 12

# Convert integer to string
age = str(age)

print("Her age is " + age)
print(type(age))


# Integer conversion
count = 34

print(int(count) + 3)


# Float conversion to integer
height = 4.5

print(int(float(height)) + 1)

# Convert a number to Boolean
print(bool(height))