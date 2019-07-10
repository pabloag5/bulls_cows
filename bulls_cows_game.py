"""
Guess a 4-digit number with no repeating digits.
For every digit the user guesses correctly in the correct place,
is a "bull"; for every digit the user guesses correctly in the
wrong place is a "cow".
"""
import pandas as pd
import random

# function to ask user for 4-digit number.
# It has three validations:
# 	1. The number must be  numeric, no letter.
# 	2. The length of the number must be 4 digits.
# 	3. The number must have unique digits, no repeat values


def guess_number():
    guess_n = input("Guess the number: ").strip()
    digit_dict = {}

    # validate if number is numeric
    if not guess_n.isnumeric():
        print("Number must be 4 - digit number.")
        return guess_number()

    # validate if number is 4 digits
    if not len(guess_n) == 4:
        print("Number must be of 4 digits")
        return guess_number()

    # validate repeated digits
    for digit in guess_n:
        digit_dict[digit] = guess_n.count(digit)
    if max(digit_dict.values()) != 1:
        print("Number must be of 4 different digits")
        return guess_number()

    return guess_n


# set the secret number
# secret_number = str(4268)
secret_number = random.sample(range(10), 4)
secret_number = ''.join(str(dg) for dg in secret_number)
# print(secret_number)

# initialize number of rounds and guessed number
guessed_number = ''
round = 0

hist_rounds = pd.DataFrame(columns=[
    'round',
    'guessed_number',
    'cows',
    'bulls'])

print("")
# start the game guessing the number
while secret_number != guessed_number:
    cows = ''
    bulls = ''
    round += 1
    print('*' * 50)
    guessed_number = guess_number()

    # compare both strings
    for i in range(len(guessed_number)):
        if guessed_number[i] == secret_number[i]:
            bulls += '|'
        elif secret_number.find(guessed_number[i]) != -1:
            cows += '|'

    hist_rounds = hist_rounds.append(
        {
            'round': round,
            'guessed_number': guessed_number,
            'cows': cows,
            'bulls': bulls},
        ignore_index=True)
    print("")
    print(hist_rounds)
    print("")


print("\nFinally you guessed the number!")
print("It took you " + str(round) + " rounds to win.")
print("")
