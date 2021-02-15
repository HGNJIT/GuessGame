""" Number Guessing Game
----------------------------------------
"""
import random

attempts_history = []


def play_game():
    if len(attempts_history) <= 0:
        wanna_play = input("Would you like to play a round? (Enter \"Yes/No\"): ")
    else:
        wanna_play = input("Would you like to play another round? (Enter \"Yes/No\"): ")

    if wanna_play.lower() == "yes":
        show_score()
        return wanna_play.lower()


def show_score():
    if len(attempts_history) <= 0:
        print("There is currently no high-score. Go for it!")
    else:
        print("Your current high score is {}!".format(min(attempts_history)))


def end_game():
    print("Hope you had fun! Goodbye!")


def start_game():
    random_number = int(random.randint(1, 10))
    attempts = 0

    print("Hello, and welcome to my guessing game!")

    play = play_game()

    while play == "yes":
        try:
            guess = input("Pick a number between 1 and 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError()
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_history.append(attempts)
                print("It took you {} attempts".format(attempts))
                play = play_game()
                attempts = 0
                random_number = int(random.randint(1, 10))
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
    else:
        end_game()


if __name__ == '__main__':
    start_game()
