from random import randint
from numberguessing_art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#function that check the user value against the actual answer
def check_answer(guess, answer, turn):
    if guess > answer:
        print("Too high")
        return turn -1
    elif guess < answer:
        print("Too low")
        return turn -1
    else:
        print(f"You got it. the answer is {answer}")

def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm Thinking of the number between 1 to 100")
    answer = randint(1,100)
    #print(f'Psssst. The right answer is {answer}')

    turn = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turn} attempt remaining to guess the number")
#user input value
        guess = int(input("Guess a number in digits: "))
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("You run out of guesses, YOU LOSE.")
        elif guess !=answer:
            print("Guess Agian.")


game()