import random

def display_question(question, options, amount):
    print(f"This question is for {format_amount(amount)}:")
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your choice (enter the corresponding number): ")
    return int(user_answer)

def format_amount(amount):
    if amount >= 10000000:
        return f"{amount / 10000000:.2f} crore"
    elif amount >= 100000:
        return f"{amount / 100000:.2f} lakh"
    else:
        return f"{amount}"

def play_kbc_game(questions):
    print("WELCOME TO KBC GAME!\n")

    total_questions = len(questions)
    current_question = 0
    amount_won = 0

    while current_question < total_questions:
        question, options, correct_answer_index, amount = questions[current_question]
        user_answer_index = display_question(question, options, amount)

        if user_answer_index == correct_answer_index:
            print("Correct!")
            amount_won += amount
            print(f"You have won {format_amount(amount_won)} so far.\n")
            current_question += 1  # Move this line here to advance the question after a correct answer
        else:
            print("Sorry, you chose the wrong option. Game Over!")
            break

        if current_question == total_questions:
            print("Congratulations! You've answered all questions correctly.")
            print(f"You won a total of {format_amount(amount_won)}")

# Sample Questions with specified amounts
questions_list = [
    ("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], 1, 700000),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2, 1000000),
    ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 2, 10000000),
    ("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], 1, 70000000),
    ("In which year was Python introduced?", ["1990", "1991", "1995", "2000"], 2, 100000000),  # Updated amount to 10 crore
    ("In what year was the first iPhone released?", ["2005", "2007", "2010", "2012"], 1, 120000000),  # Updated amount to 12 crore
]

# Shuffle the questions to make the game more dynamic
random.shuffle(questions_list)

# Start the game
play_kbc_game(questions_list)