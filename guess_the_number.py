import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    count = 0

    while guess != random_number:
        guess = int(input(f"\nGuess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again.Too low\n")
        elif guess > random_number:
            print("Sorry, guess again.Too high\n")
        count = count + 1
        
    print(f"Yay, congrats. You have guessed the number {random_number} correctly\n In {count} attempts.\n")


x = int(input("Enter any big number to play the game: "))
guess(x)
