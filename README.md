# Roulette
## Introduction
This is a simple, terminal version of the real-life casino game. Playing roulette is simple: to earn money, the player must make a wager on a square or square type. Squares include any number from 0-36 and 00. Square types include Black, Red, Even, Odd, 1st12, 2nd12, 3rd12, Low, and High.

Roulette is a risk=reward game. This means the higher the risk, the higher the payout. 
If you win by betting on black (1:2), you'll receive 2x your bet. 
If you win by betting on a 12 (1:3), you'll receive 3x your bet. 
If you win by betting on a number (1:36), you'll receive 36x your bet. 

To place a bet, use the following syntax: (bet amount) (square # or square type) 

For example, if you wanted to bet $100 on black, you'd type `100 Black` when prompted, and if you wanted to bet $25 on 27, you'd type `25 27` when prompted. 

The odds displayed on the betting screen are based on the past 100 rolls.

## Files
For this application, there are two files. 
### main.py
`main.py` contains all the code required to run roulette.
### playerfile.txt
`playerfile.txt` stores all player data that is written throughout playing.
This includes the player's `Name`, `Balance`, `# of Wins`, and up to the past 100 rolls, respectively.

The information in this file can be freely edited, but it is recommended to avoid editing the history of `rolls` (Line 4).
playerfile.txt has been pre-populated with 100 rolls in its history to accurately represent the odds. 

If you wish to create your own file instead of the premade one, simply select "Y" when
prompted with *"Are you a new player?* (Y/N)"
Otherwise, if you wish to use the data provided, select "N" when prompted.

## Credits
Roulette V1, created by Evan Kimpton
