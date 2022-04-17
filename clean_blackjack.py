#CLEAN VERSION
import random

card_face_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A' ]
card_values = list(range(1,12))
card_suit = ['Hearts','Spades','Clubs','Diamonds']

player1_cards = []
dealer_cards = []

def pvt(the_variable):
    print(the_variable)
    print(type(the_variable))

def assign_1_card_with_suit():
    return(random.randrange(2,15), random.choice(card_suit))

def deal_1_card():
    return random.choice(range(1,12))

def deal_initial_round(the_card_list = None):
    if the_card_list is None:
        the_card_list = []
    for _ in range(2):
        the_card_list.append(deal_1_card())

def determine_blackjack_or_bust(the_card_list):
    if sum(the_card_list) == 21:
        print(f'BLACKJACK - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}')
        player_keeps_being_able_to_hit_or_stand = False
    elif sum(the_card_list) > 21:
        print(f'BUST - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}')
        player_keeps_being_able_to_hit_or_stand = False
    else:
        player_keeps_being_able_to_hit_or_stand = True
    return player_keeps_being_able_to_hit_or_stand


def determine_blackjack_bust_hit_or_stand(the_card_list):
    blackjack = bust = hit_or_stand_world = False
    if sum(the_card_list) == 21:
        print(f'BLACKJACK - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}')
    elif sum(the_card_list) > 21:
        print(f'BUST - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}')
    else:
        print(f'HIT or STAND - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}')
        hit_or_stand_world = True
        while hit_or_stand_world == True:
            hit_1_more_card = input("Do you want to hit or stand? type h[lower case] for hit, type s[lower case] for stand: ")
            if hit_1_more_card == 'h':
                the_card_list.append(deal_1_card())
                print(f"You chose HIT so appending one more card - card_values = {the_card_list}, sum_card_values = {sum(the_card_list)}")
                hit_or_stand_world = determine_blackjack_or_bust(the_card_list)
            else:
                hit_or_stand_world = False
                print(f"You chose STAND so we are moving on. hit_or_stand = {hit_or_stand_world}")
        print(f'Player\'s turn has ended')


print(player1_cards)

deal_initial_round(player1_cards)
print(player1_cards)
determine_blackjack_bust_hit_or_stand(player1_cards)





