# Written by Adam Kennedy

# Main program function
def mtc():
    print ("Marginal Tax Calculator: for single filers")
    print ("Enter 'quit' at any time to end the program.")
    # wages stores the users input
    wages = input("What are your wages for the entire year before taxes: ")

    print ("Your wages are: " + wages + ".")

    # if statemnent checks to see if the user enter the quit
    # command to close the program
    if wages != 'quit':

        # if a valid command is entered the program matches the amount against
        # the if and elif statements and performs the proper calculations
        # the variable "to" is short for taxes owed and the "tp" variable is short for tax percentage
        try:
            w = float(wages)

            if w > 1 and w <= 9700.00:
                to = w * .10
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "%, you owe: $", to)

            elif w > 9700.00 and w <= 39475.00:
                to = 970 + ((w - 9700.00) * .12)
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "% , you owe: $", to)

            elif w > 39475.00 and w <= 84200.00:
                to = 4543 + ((w - 39475.00) * .22)
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "% , you owe: $", to)

            elif w > 84200.00 and w <= 160725.00:
                to = 14382.50 + ((w - 84200.00) * .24)
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "% , you owe: $", to)

            elif w > 160725.00 and w <= 204100.00:
                to = 32748.50 + ((w - 160725.00) * .32)
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "% , you owe: $", to)

            elif w > 204100.00:
                to = 46628.50 + ((w - 204100.00) * .35)
                tp = (to / w) * 100.00
                print ("Your tax rate is, " + str(round(tp, 2)) + "% , you owe: $", to)
            # if the user enters improper charcaters the else statement below performs error correction and...
            # prompts the user to try again. ie user enters data types other than ints or floats.
            else:
                print("try again! Number must be positive.")
                mtc()
                # re-runs the main program
            mtc()

        # This runs if somthing goes really wrong in the try statment.
        finally:
            print ("something went wrong!")

    # This runs if 'quit' is entered by user.
    else:
        done()


# Function that closes program
def done():
    print("You'er done!")

# This runs the main program
mtc()




