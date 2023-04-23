'''
If the dealer has less than 17, he must draw again
IF tney draw, it's a draw.
If the player busts, game over. If the dealer busts, the player wins.
Need to implement loop for drawing cards, and need to trace the logic for win determination better.
'''
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cont_play = input("Would you like to play a game of blackjack? y/n\n")

def keep_drawing(player_cards, cards):
    player_cards.append(random.choice(cards))
    print(player_cards)
    fail_check = 0
    for i in player_cards:
        fail_check += i
    if fail_check > 21:
        print("You went bust!")
        return player_cards 


def play():
    bot_cards = []
    player_cards = []
    for i in range(2):
        bot_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
        #print(bot_cards)
        #print(player_cards)
    print(f"Dealers cards: [{bot_cards[0]}], []")
    print(f"Your cards: [{player_cards[0]}], [{player_cards[1]}]")
    cont = input("Would you like to draw or pass? d/p\n")
    if cont.lower() == "d":
        keep_draw_loop = True
        while keep_draw_loop:
            keep_drawing(player_cards, cards)
            cont_2 = input("Draw again? y/n\n")
            if cont_2 == "y":
                print("Okay.")
            elif cont_2 == "n":
                print("Okay. You won't draw again.")
                keep_draw_loop = False
            else:
                print("An error code has occurred. Exiting")
                return
    elif cont.lower() == "p":
        print("Okay, you won't draw again")

    dealer_total = 0
    player_total = 0

    for i in bot_cards:
        dealer_total += i
    for i in player_cards:
        player_total += i

    print(f"Dealer cards: {bot_cards}")

    if dealer_total < 17:
        bot_cards.append(random.choice(cards))
        print("Dealer draws again.")
        print(f"Dealer cards: {bot_cards}")
    if dealer_total > 21:
        win_cond = True
        print("Dealer went bust! You win!")
        return win_cond
    print(f"Your cards: {player_cards}")
    if player_total > 21:
        win_cond = False
        print("You went bust!")
        return win_cond
    elif player_total > dealer_total:
        win_cond = True
        print("You win!")
        return win_cond
    elif player_total < dealer_total:
        win_cond = False
        print("The dealer's score beats yours. You lose!")
        return win_cond
    else:
        print("An error has occurred in calculation of scores. Exiting")
        return


play()
