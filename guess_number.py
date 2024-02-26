number = 10
guesses = 3

print("I'm thinking of a number...")
while(guesses > 0):
    guesses -= 1
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        if int(guess) > number:
            print(f"Lower! {guesses} guesses left.")
        else:
            print(f"Higher! {guesses} guesses left.")
