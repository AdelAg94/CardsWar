suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Hand():
    """ This will be the hand of the player where what cards he has on his pocket
    and will check if adding or removing from it """
    # This will add cards from class of deck as an argument
    def __init__(self,cards):
        self.cards = cards
    
    # This to print how many cards that are in hand of the player
    def __str__(self):
        return f"Contains {len(self.cards)} cards"
    
    # You can change add to addcards, this will add card or cards to all cards you have
    def add(self,added_cards):
        self.cards.extend(added_cards)
    
    # This will remove the very last card on the list
    def removeCard(self):
        return self.cards.pop()