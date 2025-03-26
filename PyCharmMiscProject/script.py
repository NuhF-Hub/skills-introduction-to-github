Errors = 8
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter)
        else:
            print("_")
        print("")

    guess = input(f"Allowed Errors Left {guesses},Next guess :")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        guesses -= 1
        if guesses == 0:
            break

        done = False
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    if done:
        print(f"You found the word ,it was {word}")
    else:
        print(f"Game Over ,the word was{word}")
