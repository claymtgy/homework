import random

'''
Number guessing game:
done    Determine the number to be guessed.
done    Determine the game mode
done    Determine the number of guesses based on game mode
    Take a guess
    Return if guess is too high or too low
    or correct
    If correct, game over,
    If incorrect, take away a guess
'''

def game(mode):
    if mode.lower() == "hard":
        p_guesses = 5
    elif mode.lower() == "easy":
        p_guesses = 10
    else:
        print("Invalid game code entered. Exiting.")
    print(f"You selected {mode}. You have {p_guesses} guesses")

    n_to_guess = random.randint(1,100)
    guesses_left = p_guesses 
    print(n_to_guess)

    for i in range(p_guesses):
        n_guess = int(input("What is your guess?\n"))
        guesses_left -= 1
        if n_guess > n_to_guess:
            print(f"Too high. You have {guesses_left} guesses left")
        elif n_guess < n_to_guess:
            print(f"Too low. You have {guesses_left} guesses left")
        elif n_guess == n_to_guess:
            print("You win!")
            return
    print("You have run out of guesses.")
    return
    

game(input("Select your game difficulty: easy/hard:\n"))


