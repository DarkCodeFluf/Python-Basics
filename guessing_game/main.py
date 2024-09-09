from random import randint
import time


# --- Introduction && Selecting game mode ---
game_mode = input("Let's play a game of \n~~~ Guess the Number ~~~ \nSelect the difficulty (easy, normal or hard): ")

while game_mode != "easy" or game_mode != "normal" or game_mode != "hard":
    time.sleep(1)
    if game_mode.lower() == "easy":
        print("In the easy mode, you have unlimited attempts to guess the number I have thought of. \nI'm thinking of a number between 0 and 50.")
        guess_this_number = randint(0, 50)
        number_of_attempts = 99999
        print("--------------------------------------------------")
        break
    elif game_mode.lower() == "normal":
        print("In the normal mode, you have 30 attempts to guess the number I have thought of. \nI'm thinking of a number between 0 and 100.")
        guess_this_number = randint(0, 100)
        number_of_attempts = 30
        print("--------------------------------------------------")
        break
    elif game_mode.lower() == "hard":
        print("In the hard mode, you have 10 attempts to guess the number I have thought of. \nI'm thinking of a number between 0 and 100.")
        guess_this_number = randint(0, 100)
        number_of_attempts = 10
        print("--------------------------------------------------")
        break
    else:
        game_mode = input("Please select a valid game difficulty (easy, normal or hard): ")
guess_count = 1
print(guess_this_number)

# --- Validating initial user input ---
while True:
    try:
        user_guess = int(input("Try to guess the number: "))
        # --- Gameplay loop && Win/Lose condition ---
        while user_guess != guess_this_number:

            if guess_count >= number_of_attempts:
                time.sleep(1)
                print("--------------------------------------------------")
                print(f"Game Over! \nUnfortunately, You have reached your limit of tries. \nI was thinking about the number {guess_this_number}.")
                break

            guess_count += 1
            time.sleep(1)

            if int(user_guess) > guess_this_number:
                if (int(user_guess) - guess_this_number) >= 10:
                    user_guess = input("The number I thought of is way smaller... \nTry again: ")
                else:
                    user_guess = input("The number I thought of is a little smaller... \nTry again: ")
            elif int(user_guess) < guess_this_number:
                if (guess_this_number - int(user_guess)) >= 10:
                    user_guess = input("The number I thought of is way bigger... \nTry again: ")
                else:
                    user_guess = input("The number I thought of is a little bigger... \nTry again: ")
        else:
            print(f"You Win! \nCongratulations, You guessed it in only {guess_count} tries!")

        break
    except:
        print("Please input a valid number.")
        continue