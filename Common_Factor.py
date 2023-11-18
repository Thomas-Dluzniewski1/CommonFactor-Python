import random

def find_divisors(random_number, divisors):
    i = 1
    while i <= random_number:
        if random_number % i == 0:
            divisors.append(i)
        i += 1
    user_input_loop(divisors, random_number)

def user_input_loop(divisors, random_number):
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
   max_num = int(input("Enter the maximum range for the number you wish to find the common multiples of: "))
   random_number = random.randint(0, max_num)
   i = 1
   print(random_number)
   divisors = []
   find_divisors(random_number, divisors)
   repeat = "y"
   while repeat == "y":
    if len(divisors) == 0:
        repeat = input("Would you like to find another random number? (enter y to continue enter n to end the program) ")
        if repeat == "y":
            max_num = int(input("Enter the maximum range for the number you wish to find the common multiples of: "))
            random_number = random.randint(0, max_num)
            find_divisors(random_number, divisors)
        if repeat == "n":
           print()

if __name__ == '__main__':
   enter_prompt()