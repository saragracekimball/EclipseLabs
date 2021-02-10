# Higher/Lower Game
The number to guess is a randomly generated number between 1 and 99. The user will have 10 guesses. On each turn, the program accepts one guess from the user. If the user guesses right, it will say “You win!”. If the user’s guess is higher or lower than the correct answer, the program will say “The number is higher than that.” (or “The number is lower than that.”). 

If after 10 guesses the user still hasn’t guessed right, print “You lose; the number was x.”, where x is the number the user was trying to guess.

The following line of code will get a random number between 1 and 99.

<code>val = random.randint(1, 100)</code>
