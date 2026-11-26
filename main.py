import random

while True:

    print("\n========== NUMBER GUESSING GAME ==========")
    print("Select Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice!")
        continue

    if choice == 1:
        max_attempts = 10
    elif choice == 2:
        max_attempts = 7
    elif choice == 3:
        max_attempts = 5
    else:
        print("Invalid choice!")
        continue

    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
    except ValueError:
        print("Enter valid numbers!")
        continue

    if start > end:
        print("Invalid range! Ending number must be greater than or equal to starting number!")
        continue

    number = random.randint(start, end)

    print(f"\nI have selected a number from {start} to {end}!")
    print(f"You have {max_attempts} attempts to guess it.")

    tries = 0
    won = False

    while tries < max_attempts:

        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if guess < start or guess > end:
            print("Your guess is outside the selected range!")
            continue

        tries += 1

        print(f"Attempts remaining: {max_attempts - tries}")

        if guess == number:
            print(f"\nCongratulations! You guessed it in {tries} attempts!")
            won = True
            break

        elif guess < number:
            print("Too Low! Try again!")

        else:
            print("Too High! Try again!")

    if not won:
        print(f"\nGame Over! The correct number was {number}.")

    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()

        if play_again == "y":
            break
        elif play_again == "n":
            print("\nThanks for playing! See you again!")
            exit()
        else:
            print("Please enter either y or n.")