#!/usr/bin/python


#Poker card game for Python
import random
    
starting_bankroll = 50
ante = 5

def play():
    global pot
    global last_call
    global user_money
    global player1_money
    global player2_money
    global player3_money

    welcome()

    bankroll = starting_bankroll - ante
    user_money = bankroll
    player1_money = bankroll
    player2_money = bankroll
    player3_money = bankroll
    
    pot = 4 * ante
    last_call = ante

    print 'You have paid your ante, your cards are:'
    
    print deal()

    print 'The first betting round will now commence. You have ${0} to bet. The ante was 5.'.format(user_money)
    betting_round()


def welcome():
    print "Welcome to Python Poker! here you will play a text-based version of 5-card poker, " \
    "written in python code!There will be three other players in the game. You will now receive your five cards."

def deal():
    global deck
    global user_cards
    global player1_cards
    global player2_cards
    global player3_cards

    deck = ['2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', 
    '8 of clubs', '9 of clubs', '10 of clubs', 'J of clubs', 'Q of clubs', 'K of clubs', 
    'A of clubs', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts', 
    '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', 'J of hearts', 'Q of hearts', 
    'K of hearts', 'A of hearts', '2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', 
    '6 of diamonds', '7 of diamonds', '8 of diamonds', '9 of diamonds', '10 of diamonds', 'J of diamonds', 
    'Q of diamonds', 'K of diamonds', 'A of diamonds', '2 of spades', '3 of spades', '4 of spades', '5 of spades', 
    '6 of spades', '7 of spades', '8 of spades', '9 of spades', '10 of spades', 'J of spades', 'Q of spades', 
    'K of spades', 'A of spades']
    random.shuffle(deck)

    user_cards = []
    player1_cards = []
    player2_cards = []
    player3_cards = []

    for x in range(0, 4):
        user_cards.append(deal_card())
        player1_cards.append(deal_card())
        player2_cards.append(deal_card())
        player3_cards.append(deal_card())

    return user_cards


def deal_card():
    global deck
    return deck.pop(0)


def bot_turn(player_money, player):
    global last_call 
    global pot

    bet_amounts = [5, 10, 15]
    action = random.choice(['calls', 'raises', 'folds'])

    player_name = "Player {0}".format(player)

    if action == 'folds':
        action_amount = ""
    else:
        player_money -= last_call
        pot += last_call
        amount = last_call

        if action == 'raises':
            amount = random.choice(bet_amounts)
            player_money -= amount
            pot += amount
            last_call = amount

        action_amount = " for ${0}".format(amount)

    print player_name + " " + action + action_amount

    return player_money


def betting_round():
    global user_money
    global player1_money
    global player2_money
    global player3_money

    player1_money = bot_turn(player1_money, '1')
    player2_money = bot_turn(player2_money, '2')
    player3_money = bot_turn(player3_money, '3')

    # choosing_betting(player1_money, '1')
    # choosing_betting(player2_money, '2')
    # choosing_betting(player3_money, '3')
    # user_bet = raw_input('Do you call, raise, or fold? ')
    # global pot
    # global last_call
    # user_money = 45
    # if user_bet.lower() == 'call':
    #     user_money -= last_call
    #     drawingRound()
    # elif user_bet.lower() == 'raise':
    #     user_money -= last_call
    #     user_raise = raw_input('How much would you like to raise, on top of the last call? $5, $10, or $15? ')
    #     if user_raise == '5':
    #         user_money -= 5
    #         pot += int(user_raise)
    #         last_call = int(user_raise)
    #         drawingRound()
    #     elif user_raise == '10':
    #         user_money -= 10
    #         pot += int(user_raise)
    #         last_call = int(user_raise)
    #         drawingRound()
    #     elif user_raise == '15':
    #         user_money -= 15
    #         pot += int(user_raise)
    #         last_call = int(user_raise)
    #         drawingRound()
    #     else:
    #         print 'You can only raise $5, $10, or $15 at a time.'
    #         user_raise = raw_input('How much would you like to raise, on top of the last call? $5, $10, or $15? ')
    # elif user_bet.lower() == 'fold':
    #     print 'Thanks for playing!'
    #     exit()
    # else:
    #     print 'Thats not valid!'
    #     user_bet = raw_input('Do you call, raise, or fold? ')


# def drawingRound():
#     print 'The drawing round will now commence. '
#     cards_discarded = int(raw_input('What cards would you like to discard? Check your cards list, and '))
