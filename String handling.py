# string handling
message = "There is a lion over there" # we can use double or single quotation for string handling
info = "here is a lion's family"
Greet = '"hello"'
print(message)
print(info)
print(Greet)
print(len(message))  # it finds the length of the message
print(Greet * 10)


#method .() it performs specific task----
print(info.upper())
print(Greet +" "+ info)
print("Greet \n info")  #escape sequence
print(info.lower())
print(info.title())
print(message.find("l"))
print(message.count("e"))
print(message.replace("e","a"))
print(message.isalpha())
print(message.isdigit())



