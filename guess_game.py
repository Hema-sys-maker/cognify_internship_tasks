import random

def guess_game():
    number = random.randint(1, 10)
    attempts = 3

    print("🎮 Welcome to Guess the Number!")
    while attempts > 0:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("🎉 Correct! You win!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1

    if attempts == 0:
        print(f"😢 Game Over! The number was {number}")

guess_game()