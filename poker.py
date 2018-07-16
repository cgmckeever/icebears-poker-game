#Poker card game for Python
import random
deck = ['2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', 'J of clubs', 'Q of clubs', 'K of clubs', 'A of clubs', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts', '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', 'J of hearts', 'Q of hearts', 'K of hearts', 'A of hearts', '2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', '6 of diamonds', '7 of diamonds', '8 of diamonds', '9 of diamonds', '10 of diamonds', 'J of diamonds', 'Q of diamonds', 'K of diamonds', 'A of diamonds', '2 of spades', '3 of spades', '4 of spades', '5 of spades', '6 of spades', '7 of spades', '8 of spades', '9 of spades', '10 of spades', 'J of spades', 'Q of spades', 'K of spades', 'A of spades']
user_cards = []
user_money = 50
player1_cards = []
global player1_money
player1_money = 50
player2_cards = []
global player2_money
player2_money = 50
player3_cards = []
global player3_money
player3_money = 50
betting_choices = [5,10,15]
welcome = """Welcome to Python Poker! here you will play a text-based version of 5-card poker, written in python code!
There will be three other players in the game. You will now receive your five cards."""
choices = ['calling', 'raising', 'folding']
def play():
    global player1_money
    global player2_money
    global player3_money
    user_cards = []
    player1_cards = []
    player1_money = 50
    player2_cards = []
    player2_money = 50
    player3_cards = []
    player3_money = 50
    print welcome
    random.shuffle(deck)
    user_cards.append(random.choice(deck))
    user_cards.append(random.choice(deck))
    user_cards.append(random.choice(deck))
    user_cards.append(random.choice(deck))
    user_cards.append(random.choice(deck))
    player1_cards.append(random.choice(deck))
    player1_cards.append(random.choice(deck))
    player1_cards.append(random.choice(deck))
    player1_cards.append(random.choice(deck))
    player1_cards.append(random.choice(deck))
    player2_cards.append(random.choice(deck))
    player2_cards.append(random.choice(deck))
    player2_cards.append(random.choice(deck))
    player2_cards.append(random.choice(deck))
    player2_cards.append(random.choice(deck))
    player3_cards.append(random.choice(deck))
    player3_cards.append(random.choice(deck))
    player3_cards.append(random.choice(deck))
    player3_cards.append(random.choice(deck))
    player3_cards.append(random.choice(deck))
    player1_money -= 5
    player2_money -= 5
    player3_money -= 5
    print 'You have paid your ante, now you can receive your cards.'
    print user_cards
    print 'The first betting round will now commence. You have $45 to bet. The ante was 5.'
    betting_round()
def choosing_betting(player_money, player):
    global player1_money
    global player2_money
    global player3_money
    global last_call
    global pot
    last_call = 5
    pot = 0
    pot += 20
    if random.choice(choices) == 'calling':
        if player == '1':
            global player1_money
            global player2_money
            global player3_money
            call_random = random.choice(betting_choices)
            player_money -= call_random
            lastcall = call_random
            pot += call_random
        else:
            global player1_money
            global player2_money
            global player3_money
            player_money -= last_call
            pot += last_call
    elif random.choice(choices) == 'raising':
        global player1_money
        global player2_money
        global player3_money
        player_money -= last_call
        pot += last_call
        raise_random = random.choice(betting_choices)
        player_money -= raise_random
        pot += raise_random
        last_call = raise_random
    elif random.choice(choices) == 'folding':
        random_num = random.randint(0,100)
        if random_num <= 10:
            print 'One player folded'
            player_money = 0
        else:
            call_random = random.choice(betting_choices)
            global player1_money
            global player2_money
            global player3_money
def betting_round():
    global player1_money
    global player2_money
    global player3_money
    choosing_betting(player1_money, '1')
    choosing_betting(player2_money, '2')
    choosing_betting(player3_money, '3')
    user_bet = raw_input('Do you call, raise, or fold? ')
    global pot
    global last_call
    user_money = 45
    if user_bet.lower() == 'call':
        user_money -= last_call
        drawingRound()
    elif user_bet.lower() == 'raise':
        user_money -= last_call
        user_raise = raw_input('How much would you like to raise, on top of the last call? $5, $10, or $15? ')
        if user_raise == '5':
            user_money -= 5
            pot += int(user_raise)
            last_call = int(user_raise)
            drawingRound()
        elif user_raise == '10':
            user_money -= 10
            pot += int(user_raise)
            last_call = int(user_raise)
            drawingRound()
        elif user_raise == '15':
            user_money -= 15
            pot += int(user_raise)
            last_call = int(user_raise)
            drawingRound()
        else:
            print 'You can only raise $5, $10, or $15 at a time.'
            user_raise = raw_input('How much would you like to raise, on top of the last call? $5, $10, or $15? ')
    elif user_bet.lower() == 'fold':
        print 'Thanks for playing!'
        exit()
    else:
        print 'Thats not valid!'
        user_bet = raw_input('Do you call, raise, or fold? ')
def drawingRound():
    print 'The drawing round will now commence. '
    cards_discarded = int(raw_input('What cards would you like to discard? Check your cards list, and '))
