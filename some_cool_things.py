'''
1) Guess My Number:
Overview:
The computer randomly generates a number. The user inputs a number, and the computer will tell you if you are too high, 
or too low. Then you will get to keep guessing until you guess the number.
'''

# main
from random import randint

guessesNum = 0
number = randint(0,9)

print('Welcome strange pal, I am thinking of a number between 0 and 9, inclusive. You have 5 chances' )
while guessesNum < 5:
	print('Take a guess')
	guess = input()
	guess = int(guess)

	guessesNum = guessesNum + 1

	if guess < number:
		print('Incorrect, your guess is too low')
	if guess > number:
		print('Incorrect, your Guess is too high')

	if guess == number:
		break

if guess == number:
	print('Good job, Stranger. You guessed my number in {} times'.format(guessesNum))

if guess!=number: 

	print('Nah fam, I was thinking of {}'.format(number))

for i in range(0,8):
	print('\n')
print('That was some cool things eh')
