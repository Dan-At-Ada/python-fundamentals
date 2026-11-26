# Calculator starter: complete the missing parts using the tasks at the bottom.


def mainMenu():
    print("A)dd numbers")
    print("S)ubtract numbers")
    choice = input("Choose your option: ").upper()
    return choice


def enterNumber():
    number = int(input("Enter a number: "))
    return number


def add(x, y):
    pass  # Return the answer.


def subtract(x, y):
    pass  # Return the answer.


# Main program starts here.
print("Welcome to my calculator")
again = "y"
while again == "y":
    userChoice = mainMenu()

    if userChoice == "A":
        answer = add(enterNumber(), enterNumber())
        print("The answer is:", answer)
    elif userChoice == "S":
        answer = subtract(enterNumber(), enterNumber())
        print("The answer is:", answer)
    else:
        print("Sorry, that is not a valid menu choice.")

    again = "n"  # Temporary: replace this with a repeat question.


# TASK STEPS
# 1. Replace pass in add and subtract with code that returns the answer.
# 2. Write your own multiply(x, y) and divide(x, y) functions.
#    Add M)ultiply and D)ivide to mainMenu, then add the matching elif choices
#    in the main program to call the new functions and print their answers.
# 3. Replace the temporary again = "n" INSIDE the loop with an input question:
#    "Another calculation? (y/n): ". Store the response in again.
#    y should repeat the menu; n should end the program.
# 4. Test all four operations using the examples below.
# 5. Extension: add a loop inside mainMenu to reject invalid choices and
#    keep asking until the user chooses A, S, M or D.
# 6. Extension: add try/except ValueError and a loop inside enterNumber.
#    If the input is not a whole number, show a message and ask again.
#
# AS SUPPLIED
# Enter whole numbers. A and S display "The answer is: None" until their
# functions are completed. The temporary again value ends the program after
# one attempt. The input-validation loops have not been written for you.
#
# EXAMPLE / EXPECTED OUTPUT AFTER TASKS 1-3
# Welcome to my calculator
# A)dd numbers
# S)ubtract numbers
# M)ultiply numbers
# D)ivide numbers
# Choose your option: A
# Enter a number: 8
# Enter a number: 2
# The answer is: 10
# Another calculation? (y/n): n
#
# MORE CHECKS (use 8 and 2 each time)
# S -> The answer is: 6
# M -> The answer is: 16
# D -> The answer is: 4.0
# Enter y at the repeat question: the menu should appear again.
# After the extensions, an invalid menu choice or number should prompt a retry.
