# Python String Handling

message = "There is a lion over there"
info = "here is a lion's family"
greet = '"hello"'

# Printing strings
print(message)
print(info)
print(greet)

# Finding the length of a string
print(len(message))

# Repeating a string
print(greet * 10)

# Converting strings to uppercase and lowercase
print(info.upper())
print(info.lower())

# Converting the first letter of each word to uppercase
print(info.title())

# Joining strings
print(greet + " " + info)

# Escape sequence
print("Greet \n info")

# Finding a character
print(message.find("l"))

# Counting a character
print(message.count("e"))

# Replacing characters
print(message.replace("e", "a"))

# Checking whether all characters are letters
print(message.isalpha())

# Checking whether all characters are digits
print(message.isdigit())



