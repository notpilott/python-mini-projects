import random
import time
import random


def main():
    while True:
        secret = random.randint(1, 10)  # pick number 1-10
        guess = int(input("Guess the number (1-10): "))

        if guess == secret:
            print("Correct!")
        else:
            print(f"Wrong! The number was {secret}.")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break


print("Loading Guessing Game...")
time.sleep(3)
main()
