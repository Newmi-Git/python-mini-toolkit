import random
import time


def ask_question(question, correct_answer, questions, removed_questions, score):
    answer = input(question)
    removed_questions.append(question)
    questions.remove(question)

    if answer.lower() == correct_answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

    return score


def change_expense(name_expenses):
    keys = list(name_expenses.keys())

    for i in range(len(keys)):
        print(i, keys[i], name_expenses[keys[i]])

    choice = int(input("Which expense do you want to change? "))
    new_value = int(input("Enter new value: "))

    name_expenses[keys[choice]] = new_value


def motivations():
    motivational_quotes = [
        "The only way to do great work is to love what you do. — Steve Jobs",
        "Believe you can and you're halfway there. — Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. — Confucius",
        "Act as if what you do makes a difference. It does. — William James",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
        "Never let the fear of striking out keep you from playing the game. — Babe Ruth",
        "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. — C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
    ]
    selected_motivation = random.choice(motivational_quotes)
    print(f"{selected_motivation}!")
    time.sleep(5)


def print_warning(text):
    print(f"\033[33m{text}\033[0m")


def print_success(text):

    print(f"\033[1;32m{text}\033[0m")


def print_error(text):
    """Prints text in bold bright red."""
    print(f"\033[1;91m{text}\033[0m")


def print_pretty(text):
    print(f"\033[35m{text}\033[0m")


def grade_calculator():
    try:
        score = int(input("Enter your score (0-100): "))
        if score >= 0 and score <= 100:
            if 90 <= score <= 100:
                print(f"Your grade is: \033[1;32mA\033[0m")
                time.sleep(2)
            elif 80 <= score <= 89:
                print(f"Your grade is: \033[1;34mB\033[0m")
                time.sleep(2)
            elif 70 <= score <= 79:
                print(f"Your grade is: \033[1;35mC\033[0m")
                time.sleep(2)
            elif 60 <= score <= 69:
                print(f"Your grade is: \033[1;36mD\033[0m")
                time.sleep(2)
            elif 50 <= score <= 59:
                print(f"Your grade is: \033[1mE\033[0m")
                time.sleep(2)
            elif 0 <= score <= 49:
                print(f"Your grade is: \033[1;31mF\033[0m")
                print("Going to main menu...")
                time.sleep(2)
            else:
                print_warning("Please enter a Valid Number!")
                print("Exiting Program.")
                time.sleep(1)
                print("Exiting Program..")
                time.sleep(1)
                print("Exiting Program...")
                time.sleep(1)
    except ValueError:
        print_error("Invalid Character Caused by ValueError, Exiting to Main Menu...")
        time.sleep(2)


def study_planner():
    study_exit = False
    study = {"Subject": "From-To"}
    while study_exit == False:
        print("================================================")
        print("What would you like to do with your Study Planner?")
        print("1. View Study Planner")
        print("2. Edit Study Planner")
        print("3. Exit")
        study_planner_choice = input("Enter the number of your choice: ")
        exit2 = False

        if study_planner_choice == "1":
            
            print("=================Study Planner:=================")
            for key, value in study.items():
                print(f" {key:>20} : {value:>10} ")

        if study_planner_choice == "2":
            exit2 = False
            while exit2 == False:
                print("================================================")
                print("Please select how you would like to edit: ")
                print("1. Add a study time")
                print("2. Edit a session")
                print("3. Exit")
                new_choice = input("Input the number of your choice: ")

                if new_choice == "1":
                    print("================================================")
                    new_study_subject = input(
                        "Please enter the subject of the session: "
                    )
                    new_study_time = input("Please enter the time of the session: ")

                    study[new_study_subject] = new_study_time
                    
                if new_choice == "2":
                    count_dict = 0
                    print("================================================")
                    for key, value in study.items():
                        print(f"{count_dict}. {key} : {value}")
                        count_dict += 1
                    print("================================================")
                    target_key = input(
                        "\nEnter the key you want to edit (e.g., 'name'): "
                    ).strip()
                    if target_key not in study:
                        print(f"Error: '{target_key}' not found in dictionary.")
                    else:
                        choice = (
                            input(
                                "Do you want to change the [K]ey or the [V]alue? (K/V): "
                            )
                            .strip()
                            .lower()
                        )

                        if choice == "k":
                            new_key = input("Enter the new key name: ").strip()
                            study[new_key] = study.pop(target_key)
                            print(f"Subject changed! New Session: {study}")
                            time.sleep(3)

                        elif choice == "v":
                            new_val = input("Enter the new value: ").strip()
                            study[target_key] = new_val
                            print(f"Value updated! New Dictionary: {study}")
                            time.sleep(3)

                        else:
                            print(
                                "Invalid choice. Please run again and enter 'K' or 'V'."
                            )
                            time.sleep(2)
                
                if new_choice == "3":
                    exit2 = True

        if study_planner_choice == "3":
            study_exit = True


def to_do_list():
    to_do_list = []
    exit = False

    while exit == False:

        print("What would you like to do:")
        print("1. Display List")
        print("2. Add Items to List")
        print("3. Edit Items in list")
        print("4. Delete Items in list")
        print("5. Exit To Do List")
        list_choice = input("Enter: ")

        if list_choice == "1":
            print("================================================")
            print("TO-DO-LIST:")
            for item in to_do_list:
                print(f"- {item}")
            time.sleep(3)
            
            exit = False

        if list_choice == "2":
            print("================================================")
            new_item = input("What would you like to add to the list? ")
            to_do_list.append(f"{new_item}")
            print("Operation successful!")
            time.sleep(2)
            exit = False

        if list_choice == "3":
            print("================================================")
            print("\nCurrent To-Do List:")
            for i, item in enumerate(to_do_list, 1):
                print(f"{i}. {item}")

            position = int(input(f"Which position is the item you want to edit?: "))
            position -= 1

            if position >= 0 and position < len(to_do_list):

                to_do_list[position] = input("New item: ")
                print("Done!")
            else:
                print("Number out of range.")

            exit = False

        if list_choice == "4":
            print("================================================")
            print("\nCurrent To-Do List:")
            for i, item in enumerate(to_do_list, 1):
                print(f"{i}. {item}")

            del_item = int(input("Which item do you wish to delete?: "))
            del_item -= 1
            removed_item = to_do_list.pop(del_item)
            print(f"You removed {removed_item}")
            print(f"Your new list: \n{to_do_list}")
            print("================================================")
            time.sleep(3)

            exit = False

        if list_choice == "5":
            exit = True


def quiz():
    questions = [
        "What is the capital of France? ",
        "Who painted the Mona Lisa? ",
        "What is 5 + 7? ",
        "Which planet is known as the Red Planet? ",
    ]
    start_game = True
    removed_questions = []
    score = 0

    print("=====================================")
    while start_game == True:
        try:
            question_length = len(questions)
            print(f"There are a total of {question_length} questions")
            number_of_questions = int(
                input("How many questions do you want to answer? ")
            )

            if number_of_questions > question_length:
                print_warning(
                    "Your number of questions exceeds the number of questions available!!!"
                )
                start_game = True
            elif number_of_questions <= question_length:
                start_game = False
        except ValueError:
            print_error("ValueERROR: Incorrect Character Inserted")
            time.sleep(1)

    print("=====================================")
    print("Welcome to the Quiz Game!")
    print("=====================================")

    for number in range(number_of_questions):
        question = random.choice(questions)

        if question == "What is the capital of France? ":
            score = ask_question(question, "Paris", questions, removed_questions, score)
            print("=========================================")

        elif question == "Who painted the Mona Lisa? ":
            score = ask_question(
                question, "Leonardo Da Vinci", questions, removed_questions, score
            )
            print("=========================================")

        elif question == "What is 5 + 7? ":
            score = ask_question(question, "12", questions, removed_questions, score)
            print("=========================================")

        elif question == "Which planet is known as the Red Planet? ":
            score = ask_question(question, "Mars", questions, removed_questions, score)
            print("=========================================")

    print(f"Your final score is: {score}/{number_of_questions}")
    time.sleep(3)

    questions.extend(removed_questions)
    removed_questions.clear()


def budget_tracker():
    print("----------BUDGET TRACKER----------")
    expenses = 0
    name_expenses = {"Name of Expense": "Cost"}
    print("===================================")
    budget = float(input("Enter Your Budget: "))
    print("===================================")
    budget_loop = True
    while budget_loop == True:
        print("===================================")
        print(f"Current Budget: R{budget}")
        print(f"Current Expenses: R{expenses}")
        print("What would you like to do?")
        print("1. Add an Expense")
        print("2. Remove an Expense")
        print("3. Change Budget")
        print("4. Get Budget Slip")
        print("5. Clear Budget and Expenses")
        print("6. Exit")
        print("===================================")
        budget_choice = input("Type your answer(1-6): ")

        if budget_choice == "1":
            print("===================================")
            expense_name = input("Name of Expense: ")
            expense_price = float(input("Cost of Expense: "))

            expenses += expense_price

            name_expenses[expense_name] = expense_price
            print(f"Current Total Cost: {expenses}")
            percentage = (expenses / budget) * 100
            
            if expenses > budget:
                print_error("WARNING: YOU ARE OVER-BUDGET")
                time.sleep(3)
            elif percentage > 80 and percentage < 100:
                print("\033[1;33m WARNING: You have spent over 80% of your budget!\033[0m")
                print(f"Current usage: {percentage:.1f}%")
                time.sleep(3)
            else:
                print(f"You are within budget. Spent: {percentage:.1f}%")
                time.sleep(3)

        if budget_choice == "2":
            print("=============================================")
            keys = list(name_expenses.keys())
            
            for i in range(len(keys)):
                print(f"{i}. {keys[i]}: {name_expenses[keys[i]]}")

            choice = int(input("Which number to delete? "))
            
            key = keys[choice]
            val = name_expenses[key]

            expenses -= val
            del name_expenses[key]
            
            print("Deleted!")

        if budget_choice == "3":
            budget = float(input("Whats the new budget? "))

        if budget_choice == "4":
            print("=========Total Budget Slip=========")
            for key, val in name_expenses.items():
                print(f"{key:<20} : {val:>10}")
            print("-----------------------------------")
            print(f"Total Expenses: {expenses}")
            time.sleep(5)
        

        if budget_choice == "5":
            budget_answer = input("Are you sure you would like to clear budget(Y/n)? ")
            budget_answer = budget_answer.lower()

            if budget_answer == "y":
                name_expenses.clear()
                budget = 0
                expenses = 0
                print("Budget Cleared!")
                time.sleep(3)
            elif budget_answer == "n":
                print("Budget and Expenses NOT cleared.")
                time.sleep(3)
            else:
                print_warning("Invalid Character!")
                time.sleep(3)

        if budget_choice == "6":
            budget_loop = False
