'''
## Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''

# WE chose this as our passcode
passcode = "12345"

# the player will have minimum attempts
tottal_atemps = 5

# the number of attempts in the start
attempts = 0

# using While loop so it keeps asking about the passcode
while attempts < tottal_atemps:
    # asking the player to enter the passcode
    entered_passcode = input("Enter the passcode: ")
    
    # checking if the entered password is correct
    if entered_passcode == passcode:
        print("YIPPIEE PASSCODE IS CORRECT, YOU MAY ENTER.")
        break
    else:
        # plus 1 to the attempts counter
        attempts += 1
        # Inform the player how many attempts they have left.
        remainingattempts = tottal_atemps - attempts
        if remainingattempts > 0:
            print(f"THE PASSCODE IS INCORRECT. You have {remainingattempts} attemps left.")
        else:
            print("YOUR ACCESS WAS DENIED PASSWORD IS INCORRECT, SYSTEM WILL BE INFORMED NOW.")
