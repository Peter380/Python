from random import shuffle

# Variables
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
         "Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,
          "Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}

# Classes for Blackjack

class Dealer():
    
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.value = 0
    
    def get_card(self,card):
        self.hand.append(card)
        if card.rank == "Ace" and (self.value + 11) <= 21:
            self.value += 11
        elif card.rank == "Ace" and (self.value + 11) > 21:
            self.value += 1
        else:
            self.value += values.get(card.rank)      
                    
    def release_cards(self):
        self.hand = []
        self.value = 0

class Player(Dealer):
    
    def __init__(self,name):
        self.name = name
        self.amount = 100
        self.hand = []
        self.value = 0
    
    def get_card(self,card):
        self.hand.append(card)
        if card.rank == "Ace":
                
            valid_input = False
            while valid_input == False:
                try:
                    ace_value = int(input("Shall the Ace be one or eleven? (1/11)"))
                    
                    if ace_value != 1 and ace_value != 11:
                        print("Please type in 1 or 11")
                    else:
                        valid_input = True
                except:
                    print("Please type in a number")
                    
                self.value += ace_value
        else:
            self.value += values.get(card.rank)
            
    #def release_cards(self):
    #    self.hand = []
        
    def placing_bet(self,bet):
        if (self.amount - bet) >= 0:
            self.amount -= bet
            print(f"You have {self.amount} € left.")
        else:
            print("Not enough money left.")
        
        #return (self.amount - amount) >= 0
    
    def win_money(self,bet):
        self.amount += bet
        print(f"You now have {self.amount} €.")
        
    #def check_black_jack(self):
     #   pass
    
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"The {self.rank} of {self.suit}"
    
class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
            
    def shuffle_deck(self):
        shuffle(self.deck)
