"""
Task 3: Number Guessing Game
The computer selects a random number. The player receives higher/lower hints
and can play multiple rounds.
"""

import random


def play_round():
    """Run one round of the guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number from 1 to 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return


def main():
    print("=== Number Guessing Game ===")

    while True:
        play_round()
        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
