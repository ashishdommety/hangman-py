def all_guesses(guesses_left):
  print("Welcome to the hangman game!")
  key = input("User 1 goes first. Hide the screen from User 2 and enter a word:\n")
  print("\n" * 50)
  answer = list("_" * len(key))
  key = list(key)

  print('\nHello Player 2!\n')

  while guesses_left != 0:
    guess = input("You have "+ str(guesses_left) +" attempts left")
    # Check if element exists in key
    if (guess in key):
      print('you got it!\n')
      # print(answer[key.index(guess)])
      answer[key.index(guess)] = guess
      if("_" not in answer):
        print('you win!!!!!')
        return
      print("".join(answer))
    # if it doesn't, ask user to try again
    else:
      print('oops, wrong guess... try again\n')
      guesses_left = guesses_left - 1 
  
  print('You lose')

all_guesses(5)
