# Guessing-Game
# 🎯 Python Number Guessing Game

A beginner-friendly command-line Number Guessing Game built using Python. The player selects a difficulty level, chooses a number range, and tries to guess the randomly generated number within a limited number of attempts.

## 🚀 Features

- **Three Difficulty Levels**
  - Easy – 10 attempts
  - Medium – 7 attempts
  - Hard – 5 attempts
- **Custom Number Range** – Players can choose their own starting and ending numbers.
- **Random Number Generation** – Uses Python's `random` module.
- **Input Validation** – Handles invalid and non-numeric inputs.
- **Attempt Tracking** – Displays the remaining attempts after each valid guess.
- **Hints** – Tells the player whether their guess is too high or too low.
- **Win/Lose Conditions** – Displays the result when the player wins or runs out of attempts.
- **Replay Option** – Allows players to start a new game without restarting the program.

## 🛠️ Technologies Used

- Python 3
- Random Module
- Exception Handling
- Loops and Conditional Statements

## 📂 Project Structure

```text
python-number-guessing-game/
│
├── main.py
├── README.md
└── .gitignore
```

## ⚙️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/naveedhahamed23/Guessing-Game.git
```

**2. Navigate to the project directory**

```bash
cd python-number-guessing-game
```

**3. Run the program**

```bash
python main.py
```

No external packages are required.

## 🎮 Sample Output

```text
========== NUMBER GUESSING GAME ==========

Select Difficulty:
1. Easy
2. Medium
3. Hard

Enter your choice: 1

Enter the starting number: 1
Enter the ending number: 50

I have selected a number from 1 to 50!
You have 10 attempts to guess it.

Guess the number: 25
Attempts remaining: 9
Too Low! Try again!

Guess the number: 38
Attempts remaining: 8
Too High! Try again!

Guess the number: 32
Attempts remaining: 7

Congratulations! You guessed it in 3 attempts!
```

## 📚 Concepts Practiced

- Variables and Data Types
- Conditional Statements (`if`, `elif`, `else`)
- `while` Loops and Nested Loops
- `break` and `continue`
- Exception Handling (`try-except`)
- Random Number Generation
- Input Validation
- Basic Program Flow and Logic

## 🎯 Purpose

This project was developed as part of my Python learning journey to strengthen programming fundamentals and understand how different Python concepts work together in a practical application.

---

**Built with Python 🐍**
