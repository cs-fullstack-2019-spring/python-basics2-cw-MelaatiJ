import random #i need to add this in order for my random integer to work
def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()




def problem1():
    randomNumber = random.randint(0,100) # picking a random number from 0 to 100
    print(randomNumber) #printing the random number
    # Create a random number. Print the number.


def problem2():

    userInput = "" #leaving it open to add whatever the userinput will  be
    while(True):
        if(userInput != "quit"): #while the function does not equal quit it will keep asking them to add something
            userInput = input("Enter anything you like or 'quit' when your tired")
            if(userInput == "quit"): #if they enter quit it will break and stop
                break




    # Create a function that has a loop that quits with ‘q’.
    # If the user doesn't enter 'q', ask them to input another string.



def problem3():
    userinput = ""# making a function where it will ask the user for a number
    # userNumber=0
    while(True):
        if(userinput != 0): #if they dont enter 0 then it will keep running
            userinput = int(input("Enter a positive number enter'0' to stop"))
            userNumber = userinput
            for userNumber in range(0,(userNumber +1)): #im adding one so it will include the number that they added and starting the count from 1
                print(userNumber)

        else:
            break


# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.
#
#


def problem4():

    randomNumber = random.randint(0,100) # picking a random number from 0 to 100
    userInput = "" #declaring the user input
    while(userInput != randomNumber):      #if the number doesnt equal what they put in then it will keep asking
        userInput = int(input("guess the number"))
        if(userInput > randomNumber):   #if its greater then the number it will tell them to guess lower
            print("Next guess has to be lower")
        if(userInput< randomNumber):  #if its lower then the number ill tell them to guess lower
            print("Next number has to be higher")


# Create a function that creates a random number.
    # Ask the user to guess the random number.
    # Keep letting the user guess until they get it right, then quit.
    # If they don't get it right, tell them if their next guess has to be higher or lower.














































if __name__ == '__main__':
    main()