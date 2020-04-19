suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Player():
    """ This will be a player with name and hand object"""

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    
    # This will print on terminal that player has placed card number and will return drawn card
    def play_card(self):
        drawn_card = self.hand.removeCard()
        print(f"{self.name} has placed : {drawn_card}")
        print("\n")
        return drawn_card
    
    # This will affect when war happens and will remove 3 cards and return them as war cards
    def remove_war_cards(self):
        war_cards = []
        if(len(self.hand.cards) == 1):
                war_cards.append(self.hand.removeCard())
        elif(len(self.hand.cards) == 2):
            for x in range(2):
                war_cards.append(self.hand.removeCard())
        else:
            for x in range(3):
                war_cards.append(self.hand.removeCard())
        return war_cards
    
    # This will return true if the player still has cards in pocket
    def still_has_cards(self):
        return len(self.hand.cards) != 0