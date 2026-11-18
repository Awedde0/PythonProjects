
#conditional statement if stmt(control flow stmt)
num = int(input("Pass me a num:"))
if num % 2 == 0:
    print("Given Num is Multiple of 2" + str(num))
else:
    print("Given Num is not Multiple of 2" + str(num))

#elif ladder

Mom_Cooking = 3
if Mom_Cooking >= 8:
    print("it was a awesome")
elif Mom_Cooking <=7:
    print("it was a good taste")
elif Mom_Cooking <=4:
    print("Not so bad")
else:
    print("It was a bad")

print("Thank You")

#Nested if
# with the logic operators/// task is to the given num is three digit and it is even num

Num = int(input("Enter a Num:"))
if num > 99 and num <= 999:        #or if num > 99 and num <= 999 and num % 2 == 0:
    if num % 2 == 0:
        print(str(Num) + "yes it is a even Num ")

else:
    print(str(Num) + " given num is not a even Num")

Name = "Samudra"
if  Name [0] == "S" or Name [0] == "s":
    print("The Name starts with given Characters")
else:
    print("Sorry, Name doesn't start with the given characters")

print("*/n**/n***/n****/n*****")

