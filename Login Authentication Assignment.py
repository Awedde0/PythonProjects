''' Login Authentication
Create a login system.
Conditions:
1. First check the username.
2. If the username is correct, check the password.
3. If both are correct, display Login successful.
4. If the username is incorrect, display Invalid username.
5. If the password is incorrect, display Invalid password
Ask the user to enter:
- ATM PIN
- Withdrawal amount
Conditions:
1. First verify the PIN.
2. If the PIN is correct, check the withdrawal amount.
3. If the amount is greater than the balance, display insufficient balance.
4. If the amount is valid, deduct it from the balance.
5. Display the remaining balance '''

Username = "Astra"
password = "astra123"

User = input("Enter your Username:")
if User==Username:
     print("Username Verified")
else:
    print("Invalid Username")
    exit()

Pass = input("Enter you password:")
if Pass ==password:
      print("Thank you, Login was successful")
else:
      print("Failed Login, Please Enter the Correct Credentials")
      exit()

Balance =5000
Check = input("please Enter Your PIN:")
if Check == Pass:
    print("Your PIN was verified you can check You're Balance now")
else:
    print("Invalid PIN")
    exit()
withdraw = int(input("Enter the amount for withdrawal:"))
if withdraw > Balance:
    print("Insufficient Balance of", Balance)
elif withdraw <= Balance:
     Balance = Balance - withdraw
     print("your balance is", Balance, " you have Successfully withdraw Your money")
     print("Your Money was deducted from bank")













