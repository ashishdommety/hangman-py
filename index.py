def all_guesses(guesses_left):
  print("Welcome to the hangman game!")
  key = input("User 1 goes first. Hide the screen from User 2 and enter a word:\n")
  print("\n" * 50)
  answer = list("_" * len(key))
  key = list(key)
  print('\nHello Player 2!\n')

  while guesses_left != 0:
    guess = input("Your guess:")
    # Check if element exists in key
    if (guess in key):
      # you already entered this answer
      if (guess in answer):
        print("you already entered this letter")
      else:
        # check for repeating letter
        for i in range(len(key)):
          if key[i] == guess:
            answer[i] = guess

        if("_" not in answer):
          print('you win!!!!!')
          return
        print("".join(answer))
    # if it doesn't, ask user to try again
    else:
      print("oops, wrong guess...You have "+ str(guesses_left - 1) +" attempts left\n")
      guesses_left = guesses_left - 1
  
  print('You lose')

all_guesses(5)
