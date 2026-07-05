import random

words = ["python", "apple", "orange", "school", "computer"]

word = random.choice(words)
guessed = []
wrong = 0
limit = 6

print("Welcome to Hangman!")

while wrong < limit:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        wrong += 1
        print("Wrong guess!")
        print("Remaining chances:", limit - wrong)

if wrong == limit:
    print("\nGame Over!")
    print("The correct word was:", word)