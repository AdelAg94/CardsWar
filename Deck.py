import random
suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck():
    """This class will be as a deck where both players will take from, this will have 
    something like 26 card for each one. """
    # As initiation we will start with giving the class all cards of H,D,S,C
    def __init__(self):
        self.allcards = [(s,r) for s in suite for r in ranks]
    
    # Here we will make random ordering of all cards each time you make an instance
    def shuffle(self):
        random.shuffle(self.allcards)    

    # This will split all cards into 26 for each player where they will be in tuple
    def split_in_hlaf(self):
        return (self.allcards[:26], self.allcards[26:])