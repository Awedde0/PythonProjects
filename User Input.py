Name = input("what is your name: ")
print(Name)
Email = input("Please enter you Email id: ")
print(Email)
Phone_Number = input("Enter you Phone number:  ")

Email_Input = input("you're Email is " + Email)
Phone_Input = input("you're Phone number is" + Phone_Number)

Height = float(input("what is your height: "))
print("you're " + str(Height/2.54) + "Inches")

#formatting
height_inches = "{:.2f}".format(Height/2.54)
print(height_inches)

#Math operations# #math is module

import math

n = float(input("Enter a number: "))

log_value = math.log2(n)
cos_value = math.cos(n)
exp_value = math.exp(n)

print("Log2 of", n, "=", log_value)
print("Cos of", n, "=", cos_value)
print("e power", n, "=", exp_value)

# math operations are floor,ceil,abs,round,factorial, %

import math
a = 20

print("SEE", math.log2(a))

