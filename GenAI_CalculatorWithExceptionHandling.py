def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y ):
    return x/y

print("Welcome to the Recursive Artist program !")
choice = 0 # default value to make sure the loop starts to run
while choice != 4:
    try:
        choice = int(input("Choose an option: \n 1. Addition \n 2. Subtraction \n 3 .Multiplication \n 4. Division \n 5. Exit")) # cast to into to make sure the choice is an integer and not a 
        if(choice > 5 or choice < 1 ): # if statement to check if answer is within choice
            choice = int(input(" please enter a whole number form 1 - 5: "))
        else:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                    print("The number you entered is not a float, please enter a float")
            if choice == 1:
                print("The sum of " + str(num1) + " and " + str(num2)+ " is " + str(addition(num1, num2)))
            elif choice == 2: 
                print("The difference between " + str(num1) + " and " + str(num2)+ " is " + str(subtraction(num1, num2)))
            elif choice ==3:
                print("The product of " + str(num1) + " and " + str(num2)+ " is " + str(multiplication(num1, num2)))
            elif choice == 4:
                try:
                    print("The quotient of " + str(num1) + " and " + str(num2)+ " is " + str(division(num1, num2)))
                except ZeroDivisionError:
                    print("The second number is zero, you can't divide by zero ")
                except ValueError:
                    print("The number you have entered isn't a whole number")
            elif choice == 5:
                print("Exiting program.")
    except ValueError:
        print("Error: invalid input. please enter a whole number form 1 - 5")

print("Program terminated restart to play again.")