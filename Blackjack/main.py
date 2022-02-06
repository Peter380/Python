blackjack_pays = 3/2
hands_played = 5 #to know when to shuffle

#Blackjack game logic

import classes
from functions import display_players_cards
from functions import get_players_bet
from functions import clear

if __name__ == "__main__":
    
    #Define player and dealer
    player_name = input("Welcome to Blackjack! Who is playing? ")
    
    blackjack_player = classes.Player(player_name)
    dealer = classes.Dealer()
    blackjack_player.release_cards()
    dealer.release_cards()
    
    '''
    Game begins
    '''
    game_on = True
    first_game = True
    while game_on:
        
        #Play anouther round
        if first_game == False:
            valid_input = False
            
            while valid_input == False:
                decision = input("Continue? (Y/N)").lower()
                if decision == "y" or decision == "n":
                    valid_input = True
                else:
                    print("Please type 'Y' or 'N'")
                    
            if decision == "n":
                print("Thank you for playing!")
                game_on = False
                break
            
        #Placing bet
        if first_game:
            print(f"You have {blackjack_player.amount} €.")
            first_game = False
        else:
            clear() #clear screen
            print(f"You have {blackjack_player.amount} € left.")
        
        if blackjack_player.amount == 0:
            print("You don't have any money left. The game is over.")
            game_on = False
        else:
            bet = get_players_bet()
            
        #Don't execute rest of the while loop
        if game_on == False:
            break
                
        bet_placed = False
        while bet_placed == False:
            
            if blackjack_player.amount - bet < 0:
                print("Sorry not enough money left. Bet differently.")
                bet = get_players_bet()
            elif blackjack_player.amount >= 0:
                blackjack_player.placing_bet(bet)
                bet_placed = True
                
        #Don't execute rest of the while loop
        if game_on == False:
            break
        
        #Dealing cards
        if hands_played == 5:
            print("New deck")
            deck = classes.Deck()
            deck.shuffle_deck()
            hands_played = 0
        
        '''
        Start round
        '''
        playing_round = True
        while playing_round:
        
            #clear()
            blackjack_player.get_card(deck.deck.pop())
            print(f"Your card: {blackjack_player.hand[0]}")
            dealer.get_card(deck.deck.pop())
            print(f"Dealer: {dealer.hand[0]}")
            blackjack_player.get_card(deck.deck.pop())
            dealer.get_card(deck.deck.pop())
            print(f"Your card: {blackjack_player.hand[1]}")
            hands_played += 1
            
            if blackjack_player.value == 21 and dealer.value != 21:
                print("Backjack! You win")
                print("Dealers cards:")
                display_players_cards(dealer)
                blackjack_player.win_money(bet+(bet*blackjack_pays))
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
            elif blackjack_player.value == 21 and dealer.value == 21:
                print("Tie! Nobody wins")
                print("Dealers cards:")
                display_players_cards(dealer)
                blackjack_player.win_money(bet)
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
                
            if playing_round == False:
                break
                
            next_move = "h"
            while next_move == "h":
                valid_input = False
                while valid_input == False:
                    next_move = input("Hit or Stand (H/S)").lower()
                    if next_move == "h" or next_move == "s":
                        valid_input = True
                    else:
                        print("Sorry, not an option")
                
                #Don't execute rest of the while loop
                if next_move == "s":
                    break
                
                blackjack_player.get_card(deck.deck.pop())
                print(blackjack_player.hand[-1])
                #display_players_cards(blackjack_player)
                
                if blackjack_player.value > 21:
                    print("Bust! You loose")
                    print(f"You have {blackjack_player.amount} € left.")
                    print("Dealers cards:")
                    display_players_cards(dealer)
                    blackjack_player.release_cards()
                    dealer.release_cards()
                    playing_round = False
                    break
                
            #Don't execute rest of the while loop
            if playing_round == False:
                break
                    
            print("Dealers cards:")
            display_players_cards(dealer)
            
            while dealer.value < 17:
                dealer.get_card(deck.deck.pop())
                print(dealer.hand[-1])
                
            if dealer.value > 21:
                print("Dealer busts! You win")
                blackjack_player.win_money(bet*2)
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
            elif blackjack_player.value > dealer.value:
                print("You win!")
                blackjack_player.win_money(bet*2)
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
            elif blackjack_player.value < dealer.value:
                print("You loose!")
                print(f"You have {blackjack_player.amount} € left.")
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
            elif blackjack_player.value == dealer.value:
                print("Tie! Nobody wins")
                blackjack_player.win_money(bet)
                blackjack_player.release_cards()
                dealer.release_cards()
                playing_round = False
            