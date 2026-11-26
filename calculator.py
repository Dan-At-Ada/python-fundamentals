# Calculator starter: input, selection, and functions.


def add(a, b):
    pass  # Complete this function using the tasks below.


def subtract(a, b):
    pass  # Complete this function using the tasks below.


first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = input("Choose + or -: ")

if operation == "+":
    print("Result:", add(first_number, second_number))
elif operation == "-":
    print("Result:", subtract(first_number, second_number))
else:
    print("That operation is not available yet. Choose + or -.")


# TASK STEPS
# 1. Replace pass in add with code that returns the sum of a and b.
# 2. Replace pass in subtract with code that returns a minus b.
# 3. Write your own multiply(a, b) and divide(a, b) functions above the inputs.
#    Each function should return its answer.
# 4. Change the operation prompt to "Choose +, -, * or /: ".
#    Add elif choices for * and / that call your new functions.
# 5. Run the program with the examples below and check the results.
# 6. Extension: add a loop so the user can do another calculation.
#    After each result, ask "Another calculation? (yes/no): ".
#    If they enter yes, ask for two new numbers and an operation.
#    If they enter no, end the program. Write this loop yourself.
#
# AS SUPPLIED
# Choosing + or - prints "Result: None" because the functions contain pass.
# This is expected until you complete the functions.
#
# EXAMPLE / EXPECTED OUTPUT AFTER STEPS 1-4
# First number: 8
# Second number: 2
# Choose +, -, * or /: +
# Result: 10.0
#
# MORE CHECKS (use 8 and 2 each time)
# Choose -  ->  Result: 6.0
# Choose *  ->  Result: 16.0
# Choose /  ->  Result: 4.0
#
# EXPECTED BEHAVIOUR AFTER THE EXTENSION
# "yes" starts another calculation in the same run; "no" ends the program.
