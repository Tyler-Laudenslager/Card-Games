import random

class Card():
    """Card class makes playing card objects"""
    
    def __init__(self,suit,value):
        self._suit = suit
        self._value = value
        self._hidden = False
        self._suit_value = self._suit, self._value

    def flip(self):

        if self._hidden:
            self._hidden = False
            self._suit_value = self._suit, self._value
            return self
        else:
            self._hidden = True
            self._suit_value = "hidden"
            return self

    def display(self):
        print(self._suit_value)
        return self

    def info(self):
        if self._hidden:
            self.flip()
            return self._suit_value
        else:
            return self._suit_value

    def show(self):
        if self._hidden:
            self.flip().display().flip()
        else:
            self.display()

        return self

class Deck():
    """Deck class creates a standard playing card deck"""
    def __init__(self):
        self._suit_set = set(['heart','club','diamond','spade'])
        self._value_set = set(['2','3','4','5','6','7','8','9','10',
                            'J','Q','K','A'])
        self._deck = [Card(suit, value) for suit in self._suit_set
                                            for value in self._value_set]
    
    def __add__(self, other):

        self._deck += other._deck
        return self
    def __len__(self):

        return len(self._deck)

    def __getitem__(self,position):
        
        return self._deck[position]

    def display(self):
        """display the cards in the deck"""
        for card in self._deck:
            print(card.display())

    def shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self._deck)
        return self
    
    # Make deal function to deal face down (default) or face up
    def deal(self, face_up = False):
        """Deal one card to a player face down (default) or face up"""

        hand = list()
        try:
            chosen = random.choice(self._deck)
            hand.append(chosen) if face_up else hand.append(chosen.flip())
            self._deck.remove(chosen)
        except IndexError:
            raise IndexError

        return hand[0]


if __name__ == "__main__":

    two_decks_combined = Deck().shuffle() + Deck().shuffle()

    two_decks_combined.shuffle()

    players = dict()

    player_names = ['rob','sue','tony','ralph','mike',
                    'john','mazy','tyler','alex','eric'
                    ,'jordan','walter','gerald','frank'
                    ,'veronica','tom','gary']

    num_of_players = len(player_names)

    for index in range(num_of_players):
        hand = list()
        try:
            card_face_up = two_decks_combined.deal(face_up=True)
            card_face_down = two_decks_combined.deal(face_up=True)
            hand.append(card_face_down)
            hand.append(card_face_up)
            
        except IndexError:
            two_decks_combined += Deck()
            num_of_players += 1
            continue

        players[player_names[index]] = hand
        two_decks_combined.shuffle()

    for player, hand in players.items():
        print(player)
        for card in hand:
            print(card.display())

    print("\n\n")
    print("Display all the cards left in deck")
    two_decks_combined.display()

