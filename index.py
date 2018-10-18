# Get player 1 input
print("Welcome to the hangman game!")
key = input("User 1 goes first. Hide the screen from User 2 and enter a word:\n")

# Clear Screen
print("\n" * 50)

# split the key into an array and display the number of blanks
print("_ " * len(key))
  
# Ask player 2 for their guess
attempts = 5

def guess(guesses_left):
  print("You have "+ str(guesses_left) +" attempts left")
  guess = input("Guess away!\n")
  # Check if element exists in array
  if key.index(guess) > -1:
    print('you got it!')
    for letter in key:
      if letter == guess:
        print(guess, end ="")
      else:
        print("_ ", end ="")
  else:
    guesses_left = guesses_left - 1 

# If the user guesses the word, display "You won! Player 2 wins!"
# If the user runs out of attempts and the answer hasn't been guessed, respond with "You lose... Player 1 wins!"
