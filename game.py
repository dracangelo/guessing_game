import random

number = random.randint(1, 10)  # Random number

player_name = input("Hello, What's your name? ")  # Player name prompt
print('Okay! ' + player_name + ', I am guessing a number between 1 and 10.')

number_of_guesses = 0  # Initialize the number of guesses to 0

# While loop for logical guesses
while number_of_guesses < 5:
    guess = int(input("Take a guess: "))
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

# Conditional statements
if guess == number:
    print('Congratulations, ' + player_name + '! You guessed the number in ' + str(number_of_guesses) + ' tries.')
else:
    print('Sorry, ' + player_name + '. You did not guess the number. The number was ' + str(number) + '.')
