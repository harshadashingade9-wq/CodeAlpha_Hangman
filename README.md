# CodeAlpha_Hangman

A text-based Hangman game built in Python as part of my CodeAlpha Python Programming Internship (Task 1).

## About the Game
The player first chooses a category, then the computer picks a random word from it. The player guesses the word one letter at a time and can make up to **6 incorrect guesses** before the game is over. Every wrong guess adds a part to the ASCII hangman drawing.

## Features
- 3 categories (Programming, Animals, Fruits) with 5 predefined words each
- Random word chosen from the selected category
- Maximum of 6 incorrect guesses
- ASCII hangman drawing that updates after every wrong guess
- Shows the word progress (e.g. `p y t h _ _`) after every guess
- Displays all letters guessed so far and the wrong guesses left
- Input validation: only a single letter is accepted, and repeated guesses don't cost a life
- Score system: 10 points per letter + 5 points for every unused guess
- High score saved in `highscore.txt` (created automatically)
- Option to play again after each game
- Simple console input/output, no external libraries needed

## Concepts Used
- `random` module
- `while` loop
- `if-else` conditions
- Strings
- Lists
- Dictionaries
- Functions
- File handling (high score)

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

High score: 0 | Your score: 0

Choose a category:
  1. Programming
  2. Animals
  3. Fruits
Enter number: 1

Category: Programming
I'm thinking of a 6-letter word. You have 6 wrong guesses.

  +---+
      |
      |
      |
     ===

Word: _ _ _ _ _ _
Guessed: -
Wrong guesses left: 6
Enter a letter: p
Good guess!

  +---+
      |
      |
      |
     ===

Word: p _ _ _ _ _
Guessed: p
Wrong guesses left: 6
Enter a letter: z
Wrong guess!

  +---+
  O   |
      |
      |
     ===

Word: p _ _ _ _ _
Guessed: p z
Wrong guesses left: 5
Enter a letter: y
Good guess!

...

Word: p y t h o n
Congratulations, you won! The word was 'python'.
You earned 85 points!
New high score: 85!

Play again? (y/n): n
Thanks for playing! Final score: 85
```

## Author
Harshada Shingade
Python Programming Intern at CodeAlpha
