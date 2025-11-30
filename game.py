#!/usr/bin/env python3
"""
Number Guessing Game
- Player guesses a randomly chosen number within a range.
- Shows hints and tracks attempts and history.
"""

import random
import sys

def get_int(prompt, min_val=None, max_val=None):
    """Prompt until a valid integer in optional range is entered."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return value
        except ValueError:
            print("That's not a valid integer. Try again.")

def play_game():
    print("=== Number Guessing Game ===")
    print("Choose a difficulty or enter your custom range.")
    print("1) Easy (1-10)\n2) Medium (1-50)\n3) Hard (1-100)\n4) Custom range")
    choice = get_int("Select option (1-4): ", 1, 4)

    if choice == 1:
        low, high = 1, 10
    elif choice == 2:
        low, high = 1, 50
    elif choice == 3:
        low, high = 1, 100
    else:
        low = get_int("Enter lower bound (>=0): ", 0)
        high = get_int("Enter upper bound (> lower bound): ", low+1)

    secret = random.randint(low, high)
    attempts = 0
    history = []

    print(f"\nI've picked a number between {low} and {high}. Try to guess it!")

    while True:
        guess = get_int(f"Enter your guess ({low}-{high}): ", low, high)
        attempts += 1
        history.append(guess)

        if guess == secret:
            print(f"🎉 Correct! The number was {secret}.")
            print(f"You took {attempts} attempts.")
            print("Your guesses:", history)
            break
        elif guess < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        # optional hint every 5 attempts
        if attempts % 5 == 0:
            dist = abs(secret - guess)
            if dist <= 3:
                hint = "very close"
            elif dist <= 10:
                hint = "close"
            else:
                hint = "far"
            print(f"Hint: You're {hint} (based on your last guess).")

    # Play again?
    again = input("Play again? (y/N): ").strip().lower()
    if again == "y":
        print("\nRestarting...\n")
        play_game()
    else:
        print("Thanks for playing! Goodbye.")
        sys.exit(0)

if __name__ == "__main__":
    play_game()


