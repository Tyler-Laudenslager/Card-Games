def get_card_value(card_info, blackjack=False):

    if blackjack:
        card_value_set = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
                            'J':10,'Q':10,'K':10,'A':11}
    else:
        card_value_set = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
                            'J':11,'Q':12,'K':13,'A':14}

    return card_value_set[card_info[1]]


def convert_card(card, blackjack=False):

    card_1_info = list(card.info())
    card_1_info[1] = get_card_value(card_1_info,blackjack=blackjack)
    converted_card = tuple(card_1_info)
    
    return converted_card