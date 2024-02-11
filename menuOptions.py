import time
def viewStats():
    with open('playerfile.txt') as player_file:
            name = player_file.readline().strip('\n')
            balance = player_file.readline().strip('\n')
            wins = player_file.readline().strip('\n')
            history = list(player_file.readline().split(' '))
            history.pop()
    print(f"\n\n\n\n\n\n[Player Statistics]\n",
            f"Player: {name}\n",
            f"Balance: {balance}\n",
            f"Wins: {wins}")
    time.sleep(4)
    
def tutorial():
    print(f"\n\n\n\t✰✰✰ Welcome to Roulette! ✰✰✰\n",
            f"\nThis is a simple, terminal version of the real-life",
            f"\ncasino game. Playing roulette is simple: to earn money,",
            f"\nthe player must make a wager on a square or square type.",
            f"\nSquares include any number from 0-36 and 00. Square types",
            f"\ninclude Black, Red, Even, Odd, 1st12, 2nd12, 3rd12, Low, and High")
    input("\n\n[Press any key to continue...]")
    print(f"\n\n\n\n\n\n\nRoulette is a risk=reward game. This means the higher the risk, ",
            f"\nthe higher the payout. "
            f"\nIf you win by betting on black (1:2), you'll receive 2x your bet.",
            f"\nIf you win by betting on a 12 (1:3), you'll receive 3x your bet.",
            f"\nIf you win by betting on a number (1:36), you'll receive 36x your bet. ")
    input("\n\n[Press any key to continue...]")
    print(f"\n\n\n\n\n\n\nTo place a bet, use the following syntax: (bet amount) (square # or square type)",
            f"\nFor example, if you wanted to bet $100 on black, you'd type '100 Black' when prompted",
            f"\nIf you wanted to bet $25 on 27, you'd type '25 27' when prompted.",
            f"\n\nOdds are based on the past 100 rolls.")
    input("\n\n[Press any key to continue...]")

