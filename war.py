import Deck as d
import Player as p
import CardTools as ctools

def game(computer=True, one_players=False, two_players=False, details=False):
    """Base Playing Card Game "WAR!":
       Modifiers:
          computer(default=True)
          one_players(default=False) set to True if one player

          two_players(defualt=False) set to True if two players
    """
    player_1 = p.Player()
    player_2 = p.Player()
    deck_1 = d.Deck().shuffle()
    pile_of_cards_1 = list()
    pile_of_cards_2 = list()
    for _ in range(26):
        pile_of_cards_1.append(deck_1.deal(face_up=False))
        pile_of_cards_2.append(deck_1.deal(face_up=False))

    player_1.collect(*pile_of_cards_1)
    player_2.collect(*pile_of_cards_2)

    def war():
        try:
            if one_players: 
                input("Press Enter to draw card\n")

            if two_players:
                input("Player 1 Press Enter to draw card\n\n")
            card_1 = player_1.draw()
            if (one_players and computer):
                print("Your card is\n\n")
                card_1.show()
                print("\n")
            if two_players:
                print("Player 1 drew\n\n")
                card_1.show()
                print("\n")

        except IndexError:
            game_over(winner='player_2',loser='player_1')
            input("Press Enter to Quit")
            exit()

        try:
            if two_players:
                input("Player 2 press Enter to draw card\n\n")
            card_2 = player_2.draw()
            if two_players:
                print("Player 2 drew\n\n")
                card_2.show()
                print("\n\n")
            if one_players:
                print("Computer drew\n\n")
                card_2.show()
                print("\n\n")
        except IndexError:
            save_card = [card_1]
            player_1.collect(*save_card)
            game_over(winner="player_1",loser="player_2")
            input("Press Enter to Quit")
            exit()

        card_1_converted = ctools.convert_card(card_1)
        card_2_converted = ctools.convert_card(card_2)
        card_pile_war = [card_1,card_2]

        if not computer:
            input("Press enter to enter combat!")

        if card_1_converted[1] == card_2_converted[1]:
            return True, card_pile_war
        elif card_1_converted[1] > card_2_converted[1]:
            if one_players:
                print("You won this round!")
            else:
                print("Player 1 won this round!")

            print("Displaying Cards Won:")
            for card in card_pile_war:
                card.show()
            print("End of Display\n\n")
            player_1.collect(*card_pile_war).shuffle()
            return False, list()
        else:
            if one_players:
                print("Computer won this round!")
                print("Displaying Cards Won:")
            else:
                print("Player 2 won this round!")
                print("Displaying Cards Won:")
            for card in card_pile_war:
                card.show()
            print("End of Display\n\n")
            player_2.collect(*card_pile_war).shuffle()
            return False, list()

    def create_burn_pile(old_burn_pile):
        new_burn_pile = old_burn_pile.copy()
        for _ in range(3):
            try:
                drawed_card = player_1.draw()
                new_burn_pile.append(drawed_card)
            except IndexError:
                player_2.collect(*new_burn_pile)
                game_over(winner='player_2',loser='player_1')
                input("Press Enter to Quit")
                exit()
            
            try:
                drawed_card_2 = player_2.draw()
                new_burn_pile.append(drawed_card_2)
            except IndexError:
                player_1.collect(*new_burn_pile)
                game_over(winner='player_1',loser='player_2')
                input("Press Enter to Quit")
                exit()
        return new_burn_pile
    
    def game_over(winner,loser):
        print(winner,"wins because",loser,"is out of cards!")
        if winner == "player_1" and details:
            player_1.hand_stats()
            player_1.show_hand()
        elif winner == "player_2" and details:
            player_2.hand_stats()
            player_2.show_hand()
        play_again = input("Do you want to play again? (y/n): ")
        play_again = True if play_again == 'y' else False
        if play_again:
            main()

    def start_war(old_burn_pile=list()):
        burn_pile = create_burn_pile(old_burn_pile)
        try:
            if one_players or two_players: 
                input("WAR! Press Enter to draw cards")
            new_card_1 = player_1.draw()
            if one_players:
                print("Your card is", end=" ")
                new_card_1.show()
            if two_players:
                print("Player 1 drew", end=" ")
                new_card_1.show()
                
        except IndexError:
            player_2.collect(*burn_pile)
            game_over(winner='player_2',loser='player_1')
            input('Press Enter to Quit')
            exit()

        try:
            new_card_2 = player_2.draw()
            if two_players:
                print("Player 2 drew", end=" ")
                new_card_2.show()
        except IndexError:
            player_1.collect(*burn_pile)
            save_card = [new_card_1]
            player_1.collect(*save_card)
            game_over(winner='player_1',loser='player_2')
            input("Press Enter to Quit")
            exit()

        new_card_1_converted = ctools.convert_card(new_card_1)
        new_card_2_converted = ctools.convert_card(new_card_2)
        burn_pile.append(new_card_1)
        burn_pile.append(new_card_2)
        if new_card_1_converted[1] > new_card_2_converted[1]: 
            print("Player one won the war!")
            new_card_1.show()
            new_card_2.show()
            print("Displaying Cards Won:")
            for card in burn_pile:
                card.show()
            print("End of display\n\n")
            player_1.collect(*burn_pile).shuffle()

        elif new_card_1_converted[1] < new_card_2_converted[1]:
            print("Player two won the war!")
            new_card_1.show()
            new_card_2.show()
            print("Displaying Cards Won:")
            for card in burn_pile:
                card.show()
            print("End of display\n\n")
            player_2.collect(*burn_pile).shuffle()
        else:
            return start_war(old_burn_pile=burn_pile.copy())
        
    while True:
        is_war, with_cards = war()
        if is_war:
            start_war(with_cards)
        else:
            continue
    

    

        

def one_player_vs_computer():
    game(one_players=True)

def two_player():
    game(two_players=True)

def test_mode():
    game(details=True)

def main():

    print("""
Welcome to the Playing Card Game "War!"
Choose from the playing options below.
1. One Player VS Computer
2. 2 Players
    """)
    while True:
        try:
            choice = input("Choice: \n")

            if choice == '1':
                print("vs computer selected\n")
                one_player_vs_computer()
            elif choice == '2':
                print("Two player selected")
                two_player()
            elif choice == 't':
                print("Test Mode: Computer Simulation")
                test_mode()
            else:
                print("Incorrect choice choose again!")
        except KeyboardInterrupt:
            exit()





if __name__ == "__main__":
    main()