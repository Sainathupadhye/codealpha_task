import random

# List of possible words
word_list = ['python', 'hangman', 'challenge', 'programming', 'openai']

# Choose a random word from the list
word_to_guess = random.choice(word_list)
guessed_letters = set()
attempts_remaining = 6

# Create a display version of the word with underscores
display_word = ['_' for _ in word_to_guess]

print("Welcome to Hangman!")

# Game loop
while attempts_remaining > 0 and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Attempts remaining: {attempts_remaining}")
    
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print("Correct!")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[index] = guess
    else:
        print("Incorrect.")
        attempts_remaining -= 1

# Game over message
if '_' not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over. The word was:", word_to_guess)
