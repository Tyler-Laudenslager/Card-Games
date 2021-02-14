import random

class Player():
    """creates a player that is able to draw and collect playing
       cards"""

    def __init__(self):
        self._hand = list()
        self._count = 0

    def __getitem__(self,position):

        return self._hand[position]
    
    def collect(self,*pile_of_cards):
        for card in pile_of_cards:
            self._hand.append(card)
            self._count += 1
        return self

    def draw(self):
            if self._count > 0:
                self._count -= 1
                new_card = self._hand.pop()
            else:
                raise IndexError
            return new_card
    
    def show_hand(self,blackjack=False):
        if blackjack:
            for card in self._hand:
                card.display()
        else:
            for card in self._hand:
                card.show()
        print("Cards in Hand:", self._count)
    
    def hand_stats(self):

        hearts = 0
        clubs = 0
        diamonds = 0
        spades = 0

        heart_cards = list()
        club_cards = list()
        diamond_cards = list()
        spade_cards = list()

        for card in self._hand:
            card_info = card.info()
            if card_info[0] == "heart":
                hearts += 1
                heart_cards.append(card.info())
            elif card_info[0] == "club":
                clubs += 1
                club_cards.append(card.info())
            elif card_info[0] == "diamond":
                diamonds += 1
                diamond_cards.append(card.info())
            else:
                spades += 1
                spade_cards.append(card.info())
        
        print("Hand Statistics:")
        print("*" * 10)
        print("Heart count: ", hearts)
        print(*heart_cards,sep='\n')
        print("Spade count: ", spades)
        print(*spade_cards,sep='\n')
        print("Club count: ", clubs)
        print(*club_cards,sep='\n')
        print("Diamond count: ", diamonds)
        print(*diamond_cards,sep='\n')
        print("Cards in Hand", self._count)
        print("End of Statistics")
        print()
        

    
    def shuffle(self):

        random.shuffle(self._hand)
        return self

if __name__ == "__main__":

    import Deck as d 
    deck_1 = d.Deck().shuffle()
    player_1 = Player()
    card_pile = list()

    for i in range(5):
        card_pile.append(deck_1.deal(face_up=True))
    player_1.collect(*card_pile).shuffle()
    player_1.show_hand()
