"""
Brenna Trout
CIS 156 (Spring 2019)

Desc: Do you wanna play a game? 
Start by guessing a number, then:
1. Listen
2. Adapt
3. Profit (jk there is no reward other than personal satisfaction)
"""

import random

# constants
max_tries = 10
num_range_lower_bound = 1
num_range_upper_bound = 100

# generate a random number
num_generated = random.randint(num_range_lower_bound, num_range_upper_bound)

# assign placeholder
num_guessed = -1

# play the game
num_attempts = 0
while(num_guessed != num_generated):
    if num_attempts == max_tries:
        print("Exceeded the maximum guess attempts")
        break
    while True:
        try:
            num_guessed = int(input("Guess a number from {0} to {1} (inclusive)".format(num_range_lower_bound, num_range_upper_bound)))
        except (ValueError, TypeError):
            print("An int")
        else:
            if num_guessed >= num_range_lower_bound and- num_guessed <= num_range_upper_bound:
                break
            else:
                print("Nope; the number we are looking for should be equal to or between {0}-{1}".format(num_range_lower_bound, num_range_upper_bound))
    if num_guessed > num_generated:
        print("Lower; you have {0} guesses remaining".format(max_tries - num_attempts))
    elif num_guessed < num_generated:
        print("Higher; you have {0} guesses remaining".format(max_tries - num_attempts))
    else:
        print("""
        【☆】★【☆】★【☆】★【☆】★【☆】

             You got it dude! 
             in {0} guess(es)

        【☆】★【☆】★【☆】★【☆】★【☆】
        """.format(num_attempts))
    num_attempts += 1