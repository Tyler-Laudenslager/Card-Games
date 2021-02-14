import Deck as d
import Player as p
import CardTools as ctools

def game():

    deck = d.Deck().shuffle() + d.Deck().shuffle()
    deck.shuffle()
    player_1 = p.Player()
    dealer = p.Player()

    intro_screen = """
Welcome to the playing card game BlackJack
"""

    player_1.collect(deck.deal(face_up=True))
    dealer.collect(deck.deal(face_up=True))
    player_1.collect(deck.deal(face_up=True))
    dealer.collect(deck.deal(face_up=False))

    print(intro_screen)

    def hit():
        print("Your hand: ")
        player_1.show_hand(blackjack=True)
        print("card total: ", count_cards(player_1))
        print("dealer's hand")
        dealer.show_hand(blackjack=True)

        choice = input("Do you want to add another card to your hand: ")
        if choice == 'yes' or choice == 'y':
            return True
        else:
            return False

    def count_cards(player):
        count = 0
        for card in player:
            _ , value = ctools.convert_card(card, blackjack=True)
            count += value
        return count

    def over(player):
        count = count_cards(player)
        if count > 21:
            return True
        if count <= 21:
            return False

    def hand_is_21(player):
        count = count_cards(player)
        if count == 21:
            return True
        else:
            return False

    def play_again():
        choice = input("Play Again?: ")
        if choice == 'y' or choice == 'yes':
            return True
        else:
            return False

    def game_over():
        print("dealer's hand")
        dealer.show_hand()
        print("card count: ", count_cards(dealer))
        print("The dealer has won the game!")
        if play_again():
            return
        else:
            exit()

    def game_won():
        print("You have won the game!")
        print("Dealer had the hand of")
        dealer.show_hand()
        if play_again():
            return
        else:
            exit()

    while hit():
        player_1.collect(deck.deal(face_up=True))
        if not over(player_1):
            continue
        else:
            break

    if over(player_1):
        print("You have gone over 21!")
        print("card count: ",count_cards(player_1))
        player_1.show_hand()
        game_over()
        return

    while not over(dealer):
        count = count_cards(dealer)
        if count <= 17:
            dealer.collect(deck.deal(face_up=True))
        elif count in range(18,22):
            break

    if hand_is_21(dealer) and hand_is_21(player_1):
        game_over()
    
    elif hand_is_21(player_1) and not hand_is_21(dealer):
        
        game_won()
    
    elif (count_cards(player_1) > count_cards(dealer)):
        
        game_won()

    elif not over(dealer):
        game_over()
    else:
        game_won()

def main():
    while True:
        game()

if __name__ == "__main__":
    main()


