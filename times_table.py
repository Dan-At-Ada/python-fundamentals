# Times-table starter: complete the missing parts using the tasks at the bottom.


def enterNumber():
    number = int(input("Which times table? Enter a whole number: "))
    return number


def timesTable(number):
    for multiplier in range(1, 11):
        pass  # Calculate and print one line of the table. This function is only half complete, think about what needs to be done


# Main program starts here.
print("Welcome to my times-table program")
number = enterNumber()
timesTable(number)


# TASK STEPS
# 1. The first loop is provided: multiplier goes from 1 to 10.
#    Replace pass with code that multiplies number by multiplier and prints
#    the calculation and answer on one line. Use the example below as a guide.
# 2. Write a second loop in the main program so the user can choose another
#    table. After each table, ask "Another table? (y/n): ".
#    y should ask for a new number and display that table; n should stop.
#    Put this loop around the number input and function call, outside the
#    function. Use the calculator's main loop as a guide.
# 3. Test with 5 and compare all ten lines with the example below.
#    Then try y at the repeat question and choose a different table.
# 4. Extension: add try/except ValueError and a loop inside enterNumber.
#    If the input is not a whole number, show a message and ask again.
#
# AS SUPPLIED
# Enter a whole number. The program prints no table until you replace pass.
# The repeat-program loop and input-validation loop are left for you to write.
#
# EXAMPLE / EXPECTED OUTPUT AFTER TASKS 1-2
# Welcome to my times-table program
# Which times table? Enter a whole number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# Another table? (y/n): n
#
# MORE CHECKS
# Enter y at the repeat question: you should be asked for a new table number.
# Enter n: the program should end.
# After the extension, entering a word instead of a number should prompt a retry.
