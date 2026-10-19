"""
CodeAlpha Python Internship - Task 1: Hangman Game
Features: ASCII hangman drawing, word categories, score + saved high score.
"""

import os
import random

MAX_WRONG = 6
HIGHSCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "highscore.txt")

# 3 categories, 5 predefined words each (no file/API needed)
CATEGORIES = {
    "Programming": ["python", "hangman", "keyboard", "program", "computer"],
    "Animals": ["elephant", "giraffe", "dolphin", "penguin", "kangaroo"],
    "Fruits": ["mango", "banana", "orange", "papaya", "pineapple"],
}

# One drawing for each number of wrong guesses (0 to 6)
STAGES = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]


def load_highscore():
    """Read the saved high score; return 0 if file is missing or broken."""
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (OSError, ValueError):
        return 0


def save_highscore(score):
    """Save the high score to a text file."""
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
    except OSError:
        print("(Could not save high score.)")


def choose_category():
    """Show the category menu and return the chosen category name."""
    names = list(CATEGORIES.keys())
    print("\nChoose a category:")
    for i, name in enumerate(names, start=1):
        print(f"  {i}. {name}")

    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]
        print(f"Please enter a number between 1 and {len(names)}.")


def show_progress(word, guessed):
    """Return the word with unguessed letters hidden, e.g. p y t h _ n"""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play(category):
    """Play one round. Return the points earned (0 if the player loses)."""
    word = random.choice(CATEGORIES[category])
    guessed = []          # all letters the player has tried
    wrong = 0

    print(f"\nCategory: {category}")
    print(f"I'm thinking of a {len(word)}-letter word. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", show_progress(word, guessed))
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed for letter in word):
            points = len(word) * 10 + (MAX_WRONG - wrong) * 5
            print(STAGES[wrong])
            print("\nWord:", show_progress(word, guessed))
            print(f"Congratulations, you won! The word was '{word}'.")
            print(f"You earned {points} points!")
            return points

    print(STAGES[MAX_WRONG])
    print(f"\nGame over! You ran out of guesses. The word was '{word}'.")
    return 0


def main():
    print("=== HANGMAN ===")
    highscore = load_highscore()
    total = 0

    while True:
        print(f"\nHigh score: {highscore} | Your score: {total}")
        category = choose_category()
        total += play(category)

        if total > highscore:
            highscore = total
            save_highscore(highscore)
            print(f"New high score: {highscore}!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print(f"Thanks for playing! Final score: {total}")
            break


if __name__ == "__main__":
    main()
