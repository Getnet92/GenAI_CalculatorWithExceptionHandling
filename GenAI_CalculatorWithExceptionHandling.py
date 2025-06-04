import logging
def addition(x, y):# function that returns the sum of the 2 float parameters
    return x + y
def subtraction(x, y): # function that returns the difference of the 2 float parameters
    return x - y
def multiplication(x, y): # function that returns the product of the 2 float parameters
    return x * y
def division(x, y ): # function that returns the quotient of the 2 float parameters
    return x/y

logging.basicConfig(
    filename='error_log.txt',  # Log errors and info to this file
    level=logging.INFO,        # Set the logging level to INFO (this means INFO, WARNING, ERROR, CRITICAL messages will be logged)
    format='%(levelname)s:%(name)s:%(message)s:' #  format for logs
)

print("Welcome to the calculator app")
num1 = 0 # initializing values with zero
num2 = 0 # initializing values with zero
choice = 0 # default value to make sure the loop starts to run
while choice != 5:
    try:
        choice = int(input("Choose an option: \n 1. Addition \n 2. Subtraction \n 3 .Multiplication \n 4. Division \n 5. Exit \n")) # cast to into to make sure the choice is an integer and not anything else
        if(choice > 5 or choice < 1 ): # if statement to check if answer is within choice
            print("Make sure your number is between 1 - 5")
            logging.error("User entered invalid menu choice: "+ str(choice) +". Expected 1-5.") # Log warning for invalid choice
            continue
    except ValueError:
        print("Error: invalid input. please enter a whole number")
        logging.exception("ValueError occurred for menu choice input: " + str(choice))
    else:
        try:
                if(choice!=5):
                    num1 = float(input("Enter the first number: ")) # prompting and recieving the first number
                    num2 = float(input("Enter the second number: ")) # prompting and recieving the second number
        except ValueError: # error message when the variable type is wrong
            print("The number you entered is not a float. ")
            logging.error("The number you entered is not a float. ")
            continue # Starts another iteration sinve there is an error, makes sure the rest of the code doesn't run
        if choice == 1:
            print("The sum of " + str(num1) + " and " + str(num2)+ " is " + str(addition(num1, num2)))# displays the 2 numbers theh user inputed and the result after calculation
        elif choice == 2: 
            print("The difference between " + str(num1) + " and " + str(num2)+ " is " + str(subtraction(num1, num2))) # displays the 2 numbers the user inputed and the result after calculation
        elif choice ==3:
            print("The product of " + str(num1) + " and " + str(num2)+ " is " + str(multiplication(num1, num2))) # displays the 2 numbers the user inputed and the result after calculation
        elif choice == 4:
            try:# specific try/except for the division() function
                print("The quotient of " + str(num1) + " and " + str(num2)+ " is " + str(division(num1, num2))) # displays the 2 numbers the user inputed and the result after calculation
            except ZeroDivisionError:# error message when user tries to divide by zero, they assing num2 to 0 then run the divide() function
                print("The second number is zero, you can't divide by zero ")
                logging.error("The second number is zero, you can't divide by zero ")
            except ValueError: 
                print("The number you have entered isn't a whole number")
                logging.error("The number you have entered isn't a whole number")
        elif choice == 5:
            print("Exiting program......")
    finally: # displays the last pick to let user know what was their last option wheter the code runs or not
        if choice!=5: 
            print("You last picked: " + str(choice))

print("Program terminated restart to play again.") # message displayed if the loop is terminated the right way, the proper value "5" is entered
