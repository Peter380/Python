import os

#Functions for Blackjack
def display_players_cards(Player):
    for card in Player.hand:
        print(card)
        
def get_players_bet():
    valid_input = False
    while valid_input == False:
        try:
            bet = int(input("How much are you betting? Please insert a number: "))
            valid_input = True
        except:
            print("This is not a number. Please insert a number")
    
    return bet

def clear():
    os.system('cls')
    