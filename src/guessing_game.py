import random


def guessing_game() -> str:
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

    difficulty = input(
        "Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts:")
    if difficulty == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5

    right_number = random.randint(1, 100)

    for i in range(number_of_attempts):
        print(f"You have {number_of_attempts-i} attemps left.")
        guess = int(input("Guess a number: "))
        if guess == right_number:
            return f"You got it! The answer was {right_number}."
        elif guess > right_number:
            print("Too high.")
        else:
            print("Too low.")

    return f"You've run out of guesses, you lose. The answer was {right_number}."


if __name__ == "__main__":
    print(guessing_game())
