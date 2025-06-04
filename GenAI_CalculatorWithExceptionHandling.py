def addition(x, y): # function that returns the sum of the 2 float parameters
    return x + y
def subtraction(x, y): # function that returns the difference of the 2 float parameters
    return x - y
def multiplication(x, y): # function that returns the product of the 2 float parameters
    return x * y
def division(x, y ): # function that returns the quotient of the 2 float parameters
    return x/y

print("Welcome to the Recursive Artist program !")
choice = 0 # default value to make sure the loop starts to run
while choice != 5:
    try:
        choice = int(input("Choose an option: \n 1. Addition \n 2. Subtraction \n 3 .Multiplication \n 4. Division \n 5. Exit \n")) # cast to into to make sure the choice is an integer and not a 
        if(choice > 5 or choice < 1 ): # if statement to check if answer is within choice
            choice = int(input(" please enter a whole number form 1 - 5: ")) # appears only if the choice is not from 1 -5 but is the right type, float
        else: # code to run if the choice picked is correct
            try:
                num1 = float(input("Enter the first number: ")) # prompting and recieving the first number
                num2 = float(input("Enter the second number: ")) # prompting and recieving the second number
            except ValueError:# causing an error when the value is the wrong data type
                    print("The number you entered is not a float. ") # error message
                    continue # reseting the while loop when the number is entered is the wrong type
            if choice == 1: # runs when user picks 1
                print("The sum of " + str(num1) + " and " + str(num2)+ " is " + str(addition(num1, num2))) # displays the 2 numbers teh user inputed and the result after calculation
            elif choice == 2: 
                print("The difference between " + str(num1) + " and " + str(num2)+ " is " + str(subtraction(num1, num2))) # displays the 2 numbers teh user inputed and the result after calculation
            elif choice ==3:
                print("The product of " + str(num1) + " and " + str(num2)+ " is " + str(multiplication(num1, num2))) # displays the 2 numbers teh user inputed and the result after calculation
            elif choice == 4:
                try: # specific exception handling for the division function
                    print("The quotient of " + str(num1) + " and " + str(num2)+ " is " + str(division(num1, num2))) 
                except ZeroDivisionError: # message displayed when user tries to divide by zero
                    print("The second number is zero, you can't divide by zero ") # message indicatig that the user assigned 0 to num2 causing the error
                except ValueError:
                    print("The number you have entered isn't a whole number") # messsage indecating the user didn't pick a number
            elif choice == 5: # exits the program since this is the while loop termination codition after displaying the message
                print("Exiting program.")
    except ValueError: # error caused if the user doesn't enter a number
        print("Error: invalid input. \n please enter a whole number form 1 - 5") # message to be displayed if the user doesn't input the right number

print("Program terminated restart to play again.")
