# CodeAlpha_Hangman

A simple text-based Hangman game built in Python as part of my CodeAlpha Python Programming Internship (Task 1).

## About the Game
The computer picks a random word from a small list, and the player guesses it one letter at a time. The player can make up to **6 incorrect guesses** before the game is over.

## Features
- Random word chosen from a list of 5 predefined words
- Maximum of 6 incorrect guesses
- Shows the word progress (e.g. `k e y _ o a r d`) after every guess
- Displays all letters guessed so far and the wrong guesses left
- Input validation: only a single letter is accepted, and repeated guesses don't cost a life
- Option to play again after each game
- Simple console input/output, no external libraries needed

## Concepts Used
- `random` module
- `while` loop
- `if-else` conditions
- Strings
- Lists
- Functions

## How to Run
1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python hangman.py
```

## Sample Gameplay
```
=== HANGMAN ===
I'm thinking of a 8-letter word. You have 6 wrong guesses.

Word: _ _ _ _ _ _ _ _
Guessed: -
Wrong guesses left: 6
Enter a letter: a
Good guess!
```

## Author
Harshada Shingade
Python Programming Intern at CodeAlpha
