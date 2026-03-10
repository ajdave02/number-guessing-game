'''
Number Guessing Game
Author: David Ajala Davis 
Description: Command Line Interface game where the user guesses a randomly generated number within a customizable range.
'''

import random


def main_menu():
    '''
    Handles user setup, validates range input, and manages replay functionality
    '''
    print("=== THE GUESSING GAME ===")
    user_name = input('Please enter your username: ')
    print(f'Hello {user_name} \nPlease choose the range of numbers you want')
    while True:
        try:
            min_value = int(input("Range 1: "))
            max_value = int(input("Range 2: "))
            if min_value >= max_value:
                print("Invalid. The Mininum value must be less than the maximum value \nPlease Try again.")
                continue
            game_logic(min_value, max_value)

            play_again = input("Do you wish to play again?  Y/N : ").strip().upper()
            if play_again != "Y":
                print("Game Terminated.")
                break
        except ValueError:
            print("Invalid input. Please try again.")

  
def game_logic(min_value, max_value):
    '''
    Runs the gueessing loop until the user correctly guesses the number
    '''
    computer_choice = random.randint(min_value, max_value)
    attempts = 0
    while True:
        try:
            user_choice = int(input(f'Guess the number between {min_value} and {max_value}: '))
            if user_choice < min_value or user_choice > max_value:
                print("Your guess is outside of the range.")
                continue
             
            attempts += 1
                
                    
            if user_choice > computer_choice:
                print("Too High. Please Try again.")
            elif user_choice < computer_choice:
                print("Too low. Please Try again.")
            else:
                print(f"You won in {attempts} attempts! Congrats! \nThanks for playing.")
                break
    
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main_menu()
