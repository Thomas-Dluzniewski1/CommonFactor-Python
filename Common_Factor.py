import random

def find_divisors(random_number, divisors):
    """Finds all of the factors of the randomly generated number and stores them in a list.

    Args:
        random_number (int): The random generated number imported from enter_prompt()
        divisors (list): The list containing all of the numbers that multiply evenly into the 
        randomly generated number.
    """
    i = 1
    while i <= random_number:
        if random_number % i == 0:
            divisors.append(i)
        i += 1
    user_input_loop(divisors, random_number)

def user_input_loop(divisors, random_number):
    """This function contains the body of the program as it is where the user will spend time
    finding the factors of the randomly generated number.

    Args:
        divisors (list): The list containing all of the numbers that multiply evenly into the 
        randomly generated number.
        random_number (int): The random generated number imported from enter_prompt()
    """
    guessed_correctly = []
    while len(divisors) > 0:
     print("\nFind all of the common multiples of:", random_number)
     choice = int(input("Common multiple: "))
     j = 0
     picked = False
     while j < len(divisors) and picked == False :
        if divisors.count(choice) > 0:
            picked = True
            print("You are correct.")
            divisors.remove(choice)
            guessed_correctly.append(choice)
            print("You have", len(divisors), "factors left\n")
        if divisors.count(choice) == 0 and picked == False and guessed_correctly.count(choice) > 0:
            picked = True
            print("You have already selected this factor.")
            print("You have", len(divisors), "factors left\n")
        if divisors.count(choice) == 0 and picked == False and guessed_correctly.count(choice) == 0:
            picked = True
            print("You are wrong.")
            print("You have", len(divisors), "factors left\n")

def enter_prompt():
   """The beginning process for the program where the user is asked for the maximum range
   for the random number generator.
   """
   max_num = int(input("Enter the maximum range for the random number generator: "))
   random_number = random.randint(0, max_num)
   i = 1
   print(random_number)
   divisors = []
   find_divisors(random_number, divisors)
   repeat = "y"
   while repeat == "y":
    if len(divisors) == 0:
        repeat = input("Would you like to find another random number? (y - continue, n - end) ")
        if repeat == "y":
            max_num = int(input("Enter the maximum range for the random number generator: "))
            random_number = random.randint(0, max_num)
            find_divisors(random_number, divisors)
        if repeat == "n":
           print()

if __name__ == '__main__':
   enter_prompt()
