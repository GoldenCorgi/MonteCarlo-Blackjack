import random
StartMoney = 1000
PlayerNumber = 6
PlayerDict = {}
Rounds = 1000
bet = 1

for i in range(PlayerNumber):
    PlayerDict[i]=StartMoney

PlayerDict['banker'] = StartMoney

Deck = []
for i in range(1,11):
    for j in range(4):
        Deck.append(i)
for i in range(12):
    Deck.append(10)

#print(Deck)

def wincondition(DealerCards,PlayerCards):
    Dealer = 0
    Player = 0
    if len(DealerCards) >= 5:
        Dealer = 1
    if len(PlayerCards) >= 5:
        Player = 1
    if DealerCards[0] == 1 and DealerCards[1] == 1:
        Dealer = 3
    if PlayerCards[0] == 1 and PlayerCards[1] == 1:
        Player = 3
    if sum(DealerCards) == 11:
        Dealer = 2
    if sum(PlayerCards) == 11:
        Player = 2
    if sum(DealerCards) > 21:
        Dealer = -1
    if sum(PlayerCards) > 21:
        Player = -1
    if Dealer > Player:
        if Dealer == 3:
            return -3
        if Dealer == 2:
            return -2
        if Dealer == 1:
            return -2
        if Dealer == 0:
            return -1
    elif Player > Dealer:
        if Player == 3:
            return 3
        if Player == 2:
            return 2
        if Player == 1:
            return 2 
        if Player == 0:
            return 1
    elif Player == -1 and Dealer == -1:
        return -1
    else:
        if sum(PlayerCards) == sum(DealerCards):
            return 0
        if sum(PlayerCards) > sum(DealerCards):
            return 1
        else:
            return -1
    
def draw(cardslist,deck):
    if cardslist[0] == 1:
        if cardslist[1] == 10:
            return cardslist
        elif cardslist[1] == 1:
            return cardslist
    if cardslist[1] == 1:
        if cardslist[0] == 10:
            return cardslist

    if sum(cardslist) < 16:
        cardslist.append(deck.pop())
    if sum(cardslist) >= 16:
        return cardslist
    if len(cardslist) >= 5:
        return cardslist
    cardslist = draw(cardslist,deck)
    return cardslist

for i in range(Rounds):
    
    CardDict = {}
    CurrentDeck = Deck.copy()
    random.shuffle(CurrentDeck)
    for players in PlayerDict.keys():
        CardDict[players] = [CurrentDeck.pop(),CurrentDeck.pop()]
    #print(CardDict)
    for player, card in CardDict.items():
        card = draw(card,CurrentDeck)
        CardDict[player] = card
    Profit=0
    for player, card in CardDict.items():
        if player == "banker":
            continue
        moneytime = wincondition(CardDict['banker'],card)
        PlayerDict[player] = PlayerDict[player] + moneytime*bet
        PlayerDict['banker'] = PlayerDict['banker'] - moneytime*bet
        Profit = Profit-moneytime*bet
        if moneytime > 0:
            CardDict[player]=f'W{abs(moneytime)}'
        if moneytime < 0:
            CardDict[player]=f'L{abs(moneytime)}'
        if moneytime == 0:
            CardDict[player]=f'D{abs(moneytime)}'
    CardDict['banker'] = Profit
    #print(CardDict)
print(PlayerDict)
print(min(PlayerDict.values()),max(PlayerDict.values()))
