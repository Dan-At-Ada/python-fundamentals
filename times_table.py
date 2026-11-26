# Times-table starter: input, a function, and a loop.


def times_table(number):
    for multiplier in range(1, 11):
        pass  # Complete the loop body using the tasks below.


number = int(input("Which times table? Enter a whole number: "))
times_table(number)


# TASK STEPS
# 1. The first loop is provided: multiplier goes from 1 to 10.
#    Replace pass with code that multiplies number by multiplier.
# 2. Print each calculation and its answer on one line, as shown below.
#    Keep this code inside the loop so it runs for every multiplier.
# 3. Run the program, enter 5, and check all ten lines against the example.
# 4. Extension: write a second loop so the user can choose another table.
#    After each table, ask "Another table? (yes/no): ".
#    If they enter yes, ask for a new number and call times_table again.
#    If they enter no, end the program. This loop belongs around the input
#    and function call, outside the function. Write it yourself.
#
# AS SUPPLIED
# The program asks for a number but prints no table until you replace pass.
#
# EXAMPLE / EXPECTED OUTPUT AFTER STEPS 1-2
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
#
# EXPECTED BEHAVIOUR AFTER THE EXTENSION
# "yes" lets you choose another table in the same run; "no" ends the program.
