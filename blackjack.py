"""
Blackjack game - by Alex Krolick

Intermediate Python - Assignment 2
"""

import random
import sys

def main():
    print("\nWelcome to Blackjack! Think you can beat the dealer?")

    player_cards = []
    dealer_cards = []

    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 10))
        if len(player_cards) == 2:
            print(f"You drew a {player_cards[0]} and a {player_cards[1]}. Your total is {sum(player_cards)}.")

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 10))
        if len(dealer_cards) == 2:
            print(f"The dealer draws a {dealer_cards[0]} and a hidden card.")

    while sum(player_cards) < 21:
        new_card = str(input("Hit or stand? (h/s): "))
        if new_card == "h":
            player_cards.append(random.randint(1, 10))
            print(f"Hit! You draw a {player_cards[-1]}. Your total is {sum(player_cards)}.")
        elif new_card == "s":
            print(f"The dealer reveals the hidden card of {dealer_cards[1]} and has a total of {sum(dealer_cards)}.")
            break
        else:
            print("Selection must be hit or stand (h/s).")

    while sum(player_cards) > 21:
        print("There's something strange in your Blackjack cards, you're over 21...YOU BUSTED!")
        play_again()

    if new_card != "s":
        print(f"The dealer reveals the hidden card of {dealer_cards[1]} and has a total of {sum(dealer_cards)}.")

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.randint(1, 10))
        print(f"The dealer draws a {dealer_cards[-1]} and now has a total of {sum(dealer_cards)}.")

    if sum(dealer_cards) == 21:
        print("The dealer wins!")
        play_again()
    elif sum(dealer_cards) > 21:
        print("The dealer busted, you win!")
        play_again()

    if sum(player_cards) > sum(dealer_cards):
        print("You win!")
        play_again()
    else:
        print("The dealer wins!")
        play_again()


def play_again():
    new_game = str(input("Do you wish to start a new game? (y/n): "))
    if new_game == "y":
        main()
    elif new_game != "y":
        print("You'll be back... ;) ")
        sys.exit()


if __name__ == '__main__':
    main()
