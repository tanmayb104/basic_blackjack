

import random
import time

def deal_card():
    card=[random.choice(deck_suits),random.choice(deck_values)]
    while(card in cards_dealt):
        card = [random.choice(deck_suits), random.choice(deck_values)]
    cards_dealt.append(card)
    return card

deck_suits = ["Spade","Hearts","Diamond","Clubs"]
deck_values = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
deck_values_value = {"Ace":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}

name = input("Enter the name :")
money = int(input("Amount to cash in :"))
flag_play = True
while(flag_play):
    print("The money left with you is :",money)
    bet = int(input("How much do you bet :"))
    while(money<bet):
        print("You dont have that much money")
        bet = int(input("How much do you bet :"))
    if(money==0):
        break
    money-=bet

    cards_dealt=[]
    player_cards=[]
    dealer_cards=[]

    player_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
    sum_player = 0
    sum_player +=deck_values_value[player_cards[0][1]]
    sum_player +=deck_values_value[player_cards[1][1]]
    sum_dealer = deck_values_value[dealer_cards[0][1]]

    print("The cards of the player are",player_cards)
    time.sleep(1)
    print("The cards of the dealer are",dealer_cards)

    flag = 0
    while(flag == 0):

        print("\n1.Hit \n2.Stay")
        case=int(input())
        if(case == 1):

            card_drawn=deal_card()
            print("The card drawn to you is ", card_drawn)
            sum_player += deck_values_value[card_drawn[1]]
            player_cards.append(card_drawn)
            time.sleep(1)
            print("Your cards are",player_cards)
            time.sleep(1)
            if(sum_player > 21):

                print("Busted \nYou lost the bet")
                print("Press 1 to play again else 0")
                if (int(input()) == 0):
                    flag_play = False
                break

        elif(case == 2):

            for i in player_cards:

                if(i[1]=="Ace" and sum_player<=11):

                    sum_player+=10

            while(sum_dealer<=21):

                flag_for_ace_in_dealer_hands = 0
                for i in dealer_cards:

                    if(i[1]=="Ace"):

                        flag_for_ace_in_dealer_hands=1

                card_drawn=deal_card()
                sum_dealer += deck_values_value[card_drawn[1]]
                print("Card drawn to the dealer is",card_drawn)
                time.sleep(1)
                dealer_cards.append(card_drawn)
                print("The cards of the dealer are",dealer_cards)
                time.sleep(1)
                if(sum_dealer<=21 and sum_dealer>sum_player):

                    print("The dealer won with a hand of",sum_dealer)
                    flag = 1
                    print("Press 1 to play again else 0")
                    if(int(input())==0):
                        flag_play = False
                    break

                elif(sum_dealer > 21):

                    print("You won with a hand of ",sum_player)
                    money+=bet
                    money+=bet
                    flag = 1
                    print("Press 1 to play again else 0")
                    if (int(input()) == 0):
                        flag_play = False
                    break

                elif(flag_for_ace_in_dealer_hands == 1 and sum_dealer+10>sum_player and sum_dealer+10<=21):

                    print("The dealer won with a hand of",sum_dealer+10)
                    flag = 1
                    print("Press 1 to play again else 0")
                    if (int(input()) == 0):
                        flag_play = False
                    break

                elif(sum_dealer == sum_player and sum_dealer>15):

                    print("Draw")
                    money+=bet
                    flag = 1
                    print("Press 1 to play again else 0")
                    if (int(input()) == 0):
                        flag_play = False
                    break
