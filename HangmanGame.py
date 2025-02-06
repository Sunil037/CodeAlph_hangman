import random

# List of words
words = ["python", "hangman", "computer", "science", "engineering","student"]

# Select a random word
word = random.choice(words)
word_display = ["_"] * len(word)  # Display underscores for each letter
attempts = 6  # Maximum incorrect guesses
guessed_letters = set()  # Track guessed letters

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_display:
    print("\nWord:", " ".join(word_display))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    # Check if letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    # Check if guess is in the word
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
    else:
        print("Incorrect guess!")
        attempts -= 1

# Game over message
if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
