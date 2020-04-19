# Here we will start war card game
from Deck import Deck
from Player import Player
from Hand import Hand
suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# At first we need to add the deck to the field
d = Deck()
# Then we need to re-order the cards randomly
d.shuffle()
# Now let's split the whole cards into two halves 
half1,half2 = d.split_in_hlaf()

# Now let's give computer its cards and the player his cards
comp = Player("Computer", Hand(half1))

# Now let's ask the user(player) to add his or her name
name = input("Please enter your name to start playing!!! ")
user = Player(name, Hand(half2))

# Now let's counting total rounds and wars by starting with initial zero 0

total_rounds = 0
war_count = 0

while comp.still_has_cards and user.still_has_cards:
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(comp.name + " has the count: " + str(len(comp.hand.cards)))
    print("play a card! ")
    print("\n")

    table_cards = []
    if(len(comp.hand.cards) == 0 or len(user.hand.cards) == 0 ):
        break

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    # In c_card and p_card we use index one because we defined cards as tuple (suite, rank)
    # So we need rank not suite
    if c_card[1] == p_card[1]:
        war_count +=1
        print("War !")
        # Here we will remove 3 cards from both computer and player and add them to table cards
        table_cards.extend(comp.remove_war_cards())
        table_cards.extend(user.remove_war_cards())
        
        # Here we will check who wins computer or player then use add from hand
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    
    # The last bigger if was checking if there is a war but if there are no wars then 
    # The game will be normal by else
    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

# Here we will just print at the end of the game how many rounds and wars happened
print("Game Over !")
print("Total number of rounds are: " + str(total_rounds))
print("Number of wars happened are: " + str(war_count) + " times")