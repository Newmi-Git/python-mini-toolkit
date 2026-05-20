import random
import helpers
import time

answer = "yes"
BOLD = "\033[1m"
RED = "\033[31m"
RESET = "\033[0m"


while answer == "yes":
    print(
        f"\n-------------------\033[1;34mPYTHON_MINI_TOOLKIT\033[0m------------------------"
    )
    print("==============================================================")
    print("| Choose from the following options:                         |")
    print("| 1. Grade Calculator               5. Number Guessing Game  |")
    print("| 2. Even or Odd Number Checker     6. Study Planner         |")
    print("| 3. Simple Quiz Game               7. Budget Tracker        |")
    print("| 4. To Do List Manager             8. Daily Motivation      |")
    print("|                                                            |")
    print("| 9. Exit                                                    |")
    print("==============================================================")

    choice = input("Enter the number of your choice: ")

    if choice == "9":
        break

    elif choice == "1":
        print(
            f"\n-------------------\033[1;93mGRADE CALCULATOR\033[0m-------------------------"
        )
        helpers.grade_calculator()

    elif choice == "2":
        print(
            f"-------------------\033[1;92mEVEN OR ODD CHECKER\033[0m------------------------"
        )
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
            time.sleep(3)
        else:
            print(f"{number} is an odd number.")
            time.sleep(3)

    elif choice == "3":
        print(
            f"\n-------------------\033[1;95mQUIZ GAME\033[0m------------------------"
        )
        helpers.quiz()

    elif choice == "4":
        print(
            f"\n-------------------\033[1;96mTO DO LIST\033[0m------------------------"
        )
        helpers.to_do_list()

    elif choice == "5":
        print(
            f"\n------------------\033[1;91mNUMBER GUESSER\033[0m---------------------"
        )
        print(
            "Rules:\n-there will be a randomly generated 3 digit number,\n-Type a number from 1-999\n-It will tell u whether the number you've written is higher or lower than the random number \n-Accurately guess the number and you WIN!"
        )
        random_number = random.randint(0, 999)
        won = False
        attempt_number = 0

        while won == False:
            attempt = int(input("Type in a number 1-999: "))
            if attempt < 1000 and attempt > 0:
                if attempt == random_number:
                    won = True
                    print("=========================================")
                    print("Congrats, You Won!")
                    print(f"Attempts: {attempt_number}")
                    print("=========================================")
                    time.sleep(3)
                elif random_number > attempt:
                    print("Higher")
                    attempt_number += 1
                elif random_number < attempt:
                    print("Lower")
                    attempt_number += 1
            else:
                helpers.print_warning("Please Enter a Valid Number!")

        exit = False

    elif choice == "6":  # Study Planner
        print(
            f"\n-------------------\033[1;95mSTUDY PLANNER\033[0m------------------------"
        )
        helpers.study_planner()

    elif choice == "7":  # Budget Tracker
        print(
            f"\n-------------------\033[1;91mBUDGET TRACKER\033[0m------------------------"
        )
        helpers.budget_tracker()

    elif choice == "8":  # Daily Motivation Generator
        print(
            f"\n------------------\033[1;93mDAILY MOTIVATION\033[0m-----------------------"
        )
        helpers.motivations()
    
    elif choice not in ["1","2","3","4","5","6","7","8","9"]:
        helpers.print_error("INVALID INPUT")
        time.sleep(2)
