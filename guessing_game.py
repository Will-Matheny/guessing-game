import random

run_code = 'yes'

best_score=None

def start():
    print("/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ")
    print("|           Number Sort Game           |")
    print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")


def end():
    print("/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ")
    print("|        Thank you for playing         |")
    print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")



while run_code.lower() == 'yes':
  start()
  num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
  guess = 0
  answer = random.randint(1, 10)
  print(f'The current high score is {best_score}.')
  name = input("Hello! What shall I call you? ")
  print(f'Howdy, {name} I am Guessing a number between 1 and 10.')
  print('Please enter your first guess: ')
  number_of_guesses = 0
  while guess != answer:
    guess = input()
    number_of_guesses += 1
    while guess not in num_list:
      print('Please enter a number between 1-10')
      guess = input()
    guess = int(guess)
    if guess < answer:
      print('Your guess is too low')
    if guess > answer:
      print('Your guess is too high')
    if guess == answer:
      print(f'You guessed the number in {number_of_guesses} tries.')
      if best_score == None or number_of_guesses < best_score:
        best_score = number_of_guesses
        print(f"Your new best score is {best_score} tries.")
        break
      else:
        print(f" No new high score the current high score is {best_score}.")

  run_code = input('Would you like to play again? Please type yes or no:')

  end()
