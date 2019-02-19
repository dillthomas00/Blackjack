import random

card_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen"]
card_types = ["Spades", "Clubs", "Diamonds", "Hearts"]
duplicates = []


#Works
def random_card():
    selected_card = card_numbers[random.randint(0, 12)]
    selected_card_type = card_types[random.randint(0, 3)]
    card_picked = selected_card + selected_card_type
    if card_picked in duplicates:
        random_card()
    else:
        duplicates.append(card_picked)

def get_value(card):
    if "Spades" in card:
        card_value = card.replace("Spades","")
    elif "Clubs" in card:
        card_value = card.replace("Clubs","")
    elif "Diamonds" in card:
        card_value = card.replace("Diamonds","")
    else:
        card_value = card.replace("Hearts", "")
        
    if card_value == "Ace":
        card_value = 11
    elif card_value == "Jack" or card_value == "King" or card_value == "Queen":
        card_value = 10

    return card_value
    
def player_calculate():
    card_1 = duplicates[0]
    card_2 = duplicates[1]
    card1_value = get_value(card_1)
    card2_value = get_value(card_2)
    player_total = int(card1_value) + int(card2_value)

    while player_total < 21:
        print ("hit me or stick?")
        choice = input()
        if choice == "h":
            random_card()
            another_card = duplicates[-1]
            another_card_value = get_value(another_card)
            player_total = player_total + int(another_card_value)
            print ("new total " + str(player_total))
        else:
            break
    computer_calculate(player_total)

    
    


def computer_calculate(player_total):
    if player_total >= 22:
        print ("Player has gone bust")
    else:
        
        random_card() #Dealer
        random_card()
        card_1 = duplicates[-2]
        card_2 = duplicates[-1]
        card1_value = get_value(card_1)
        card2_value = get_value(card_2)
        computer_total = int(card1_value) + int(card2_value)
        print (computer_total)
        print (player_total)
        if computer_total >= player_total:
            print ("Dealer Wins")
        else:
            print ("Player Wins")
            
    

random_card() # player
random_card()

player_calculate()


    
