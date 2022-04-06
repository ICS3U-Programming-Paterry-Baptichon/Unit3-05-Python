# Created by: Paterry Baptichon Junior
# Created on: 2022 - 04-06
# This is a program which tells you the name of the month you input.


def main():
    # This is what tells you the name of the month you input.

    # User enters an input
    number_of_month = int(input("Input the number of a month (1-12): "))

    # Process for the first month
    if number_of_month == 1:
        # Output and the display
        print("")
        print("January")
    # Process of the second month
    elif number_of_month == 2:
        # Output and display
        print("")
        print("February")
    # Process of the third month
    elif number_of_month == 3:
        # Output and display
        print("")
        print("March")
    # Process of the fourth month
    elif number_of_month == 4:
        # Output and display
        print("")
        print("April")
    # Process of the fifth month
    elif number_of_month == 5:
        # Output and display
        print("")
        print("May")
    # Process of the sixth month 
    elif number_of_month == 6:
        # Output and display
        print("")
        print("June")
    # Process of the seventh month
    elif number_of_month == 7:
        # Output and display
        print("")
        print("July")
    # Process of the eighth month 
    elif number_of_month == 8:
        # Output and display
        print("")
        print("August")
    # Process of the ninth month
    elif number_of_month == 9:
        # Output and display
        print("")
        print("September")
    # Process of the tenth month
    elif number_of_month == 10:
        # Output and display
        print("")
        print("October")
    # Process of the eleventh month
    elif number_of_month == 11:
        # Output and display
        print("")
        print("November")
    # Process of the twelfth month
    elif number_of_month == 12:
        # Output and display
        print("")
        print("December")
    # Processes if user input is higher than 12 months
    elif number_of_month > 12:
        # Output
        print("")
        print("That's not a month")
    # Processes if user input is lower than 1 
    elif number_of_month < 1:
        # Output
        print("")
        print("That's not a month")
    # Process
    else:
        # It is impossible to get here because of the int(input) so if you do
        # here you most likely did something wrong.
        print("Error, check you number and try again.")


if __name__ == "__main__":
    main()