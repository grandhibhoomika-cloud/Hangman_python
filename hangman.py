word = "python"
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Hangman Game")

while wrong_guesses < max_wrong:

    # ---- Drawing only in OUTPUT ----
    print("------")
    print("|    |")

    if wrong_guesses >= 1:
        print("|    O")
    else:
        print("|")

    if wrong_guesses == 2:
        print("|    |")
    elif wrong_guesses == 3:
        print("|   /|")
    elif wrong_guesses >= 4:
        print("|   /|\\")
    else:
        print("|")

    if wrong_guesses == 5:
        print("|   /")
    elif wrong_guesses >= 6:
        print("|   / \\")
    else:
        print("|")

    print("|")
    print("--------")

    # ---- Word display ----
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed ⚠️")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct ✅")
    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("Wrong ❌")

if wrong_guesses == max_wrong:
    print("😢 Game Over! Word was:", word
