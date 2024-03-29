# Roulette, by Evan "Tinlia" Kimpton

import random
import time
from collections import Counter
from dicts import square_types, squares

history = []
temphist = ""


def save(name, bal, wins, history):
    with open('playerfile.txt', 'w') as player_file:
        player_file.write(name)                 # Name
        player_file.write('\n' + str(bal))      # Balance
        player_file.write("\n" + str(wins))     # Wins
        temphist = ""
        for item in history:
            temphist += item + " "
        player_file.write('\n' + temphist)  # History


# Displays the odds based on the past 100 rolls before each bet
def print_odds():
    print("")
    num_of_entries = len(history)/5
    nums = []
    # Creates a list of all numbers to perform .most_common on
    for i in range(0,int(len(history)/5)):
        if history[(i*5)-1] != '': nums.append(history[(i*5)-1])
    top_num = Counter(nums).most_common(1)[0]

    # Compute odds using num_of_entries and occurrences in history
    print("============={ ODDS }=============")
    print(f"Even:  {int((history.count('even')/num_of_entries)*100)}% "
          f"\tOdd:   {int((history.count('odd')/num_of_entries)*100)}%")
    print(f"Low:   {int((history.count('low')/num_of_entries)*100)}% "
          f"\tHigh:  {int((history.count('high')/num_of_entries)*100)}%"
          f"\tTop#:  {top_num[0]}")
    print(f"1st12: {int((history.count('1st12')/num_of_entries)*100)}% "
          f"\t2nd12: {int((history.count('2nd12')/num_of_entries)*100)}% "
          f"\t3rd12: {int((history.count('3rd12')/num_of_entries)*100)}%")
    print(f"Red:   {int((history.count('red') / num_of_entries) * 100)}% "
          f"\tBlack: {int((history.count('black') / num_of_entries) * 100)}%"
          f"\tGreen: {int((history.count('green')/num_of_entries)*100)}%")
    print("==================================")


# Time to spin the wheel!
def start(bal, wins):
    wins = int(wins)
    while True:
        print("\n")
        # If history is not empty, print the odds
        if len(history) != 0: print_odds()
        else: print("\n\n\n\nSquare Types: Black, Red, Even, Odd, 1st12, 2nd12, 3rd12, Low, High, Any # from 0-36, 00")
        # Ask player for bet
        print(f"Total Balance: ${bal}")
        print("[E] to Exit to Title Screen")
        bet = input("Please enter a bet (bet) (square/type):\n> ")

        # Store bet, then split into amount and type
        bet_square = bet.split(' ')
        valid = True

        # If the player is trying to exit, save data and return
        if bet_square[0].upper() == 'E':
            print("Saving...")
            save(name, bal, wins, history)
            return

        # Checks if two arguments have been passed
        if len(bet_square) == 2:
            # Catches a ValueError in the event a person enters a String
            # as a bet instead of an integer
            try:
                amount = int(bet_square[0])
            except ValueError:
                valid = False

            # Convert balance to an int
            bal = int(bal)
            bet_value = bet_square[1].lower()
            # More checks!
            if valid:
                # Check if bet amount is valid
                if amount <= 0: valid = False
                # Check if square is valid
                if not (bet_value in square_types): valid = False
                # Check if player can afford the bet
                if amount > bal: valid = False
        # If bet has more or less than two arguments, set validity to False
        else:
            valid = False

        # Validity Check
        print("\n\n\n\n\n\n")
        if not valid:
            print("Invalid input, spin cancelled.\n\n")
            time.sleep(2)
        # Spin if valid
        else:

            # Subtract amount from balance
            bal -= amount
            # Roll a random choice from the squares dict
            selected_square = list(random.choice(list(squares.items())))
            # Announce the square chosen
            num = selected_square[0]
            num_values = selected_square[1]
            print(f"The ball has landed on {num}, {num_values[0].title()}")

            # Add roll info into a history list
            for value in num_values:
                history.append(value)

            # If there are more than 100 rolls in the history list, pop the oldest 5
            if len(history) > 500:
                for i in range(5):
                    history.pop(0)

            # Check for bet_type in square's list
            if bet_value in num_values:
                # If the bet_type is in the list
                # Add amount*multiplier to balance
                if bet_value == 'even' or bet_value == 'odd' or bet_value == 'high' or bet_value == 'low' or \
                        bet_value == 'red' or bet_value == 'black':
                    bal += 2*amount
                    print(f"Congratulations! You've won ${2 * amount}!")
                    wins += 1
                elif bet_value == '1st12' or bet_value == '2nd12' or bet_value == '3rd12':
                    bal += 3*amount
                    print(f"Congratulations! You've won ${3 * amount}!")
                    wins += 1
                elif bet_value in square_types[9:]:
                    bal += 36*amount
                    print(f"Congratulations! You've won ${36 * amount}!")
                    wins += 1
                else: print("I don't even know how this would happen")
                print("\n\n")
            else:
                # Inform player they lost
                print("Better luck next time!")
                print("\n\n")
            time.sleep(2)
        save(name, bal, wins, history)


# Player initializing
while True:
    new = input("Are you a new player? (Y/N)\n> ")
    if new.upper() == 'Y':
        with open('playerfile.txt', 'w') as player_file:
            name = input("Please enter your name: ").strip('\n')
            balance = 1000
            wins = 0
            save(name, balance, wins, history)
            print("\n")
            print(f"--=== Welcome To Roulette, {name}! ===--\n")
            break
    elif new.upper() == 'N':
        with open('playerfile.txt') as player_file:
            name = player_file.readline().strip('\n')
            balance = player_file.readline().strip('\n')
            wins = player_file.readline().strip('\n')
            history = list(player_file.readline().split(' '))
            history.pop()
            print("\n")
            print(f"\n\n--=== Welcome Back To Roulette, {name}! ===--\n")
            break
    else:
        print("Invalid input.\n")


# Title Screen
while True:
    print("\n\n\n\nPlease Select an option below:\n",
          "[S]tart Roulette\n",
          "[V]iew Player Stats\n",
          "[T]utorial\n",
          "[C]redits\n",
          "[E]xit")
    selection = input("> ").upper()

    from menuOptions import viewStats, tutorial

    # Starts Roulette, passing the current balance and wins
    if selection == 'S': start(balance, wins)
    elif selection == 'V':
        viewStats()
    elif selection == 'T':
        tutorial()
    elif selection == 'C':
        print(f"\n\n\n\n\n\n\n\nCredits:\n\tRoulette V1, created by Evan 'Tinlia' Kimpton\n")
        time.sleep(3)
    elif selection == 'E':
        print("Thank you for playing!")
        break
    else:
        print("Invalid Selection.\n")
        time.sleep(3)
