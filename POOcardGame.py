import random

cardNumbers = "2 3 4 5 6 7 8 9 10 J Q K A".split()
cardSuite = "H D S C".split()
cardSuites = (int(len(cardNumbers)/4))*cardSuite
cardSuites.sort()


class Deck():

    def __init__(self, cardNumbers, cardSuite):
        self.cardNumbers = cardNumbers
        self.cardSuite = cardSuite

    def shuffle(self):
        deck = []
        for suite in cardSuite:
            for num in cardNumbers:
                deck.append(num+suite)
        random.shuffle(deck)
        return deck

    def assignCards(self, deck):
        deckLength = int(len(deck)/2)
        player1 = deck[0:deckLength]
        player2 = deck[deckLength:len(deck)+1]
        return player1, player2


class Hand():

    def __init__(self, hand):
        self.hand = hand

    def cardsLeft(self):
        if len(self.hand) == 0:
            print(len(self.hand))
            return True
        else:
            print(len(self.hand))
            return False

    def isNum(self, currentCard):
        if (currentCard =="A") or (currentCard == "K") or (currentCard == "Q") or (currentCard == "J"):
            currentCard = currentCard
            return currentCard
        else:
            currentCard = int(currentCard)
            return currentCard

    def addCard(self, addCard):
        currentHand = self.hand
        for a in addCard:
            currentHand.append(a)

    def removeCard(self, removeCard):
        currentHand = self.hand
        currentHand.remove(removeCard)

    def getCard(self):
        card = self.hand[0]
        return card

    def getCardNum(self):
        card = self.hand[0]
        if type(card)!= "int":
            if len(card) == 2:
                currentCard = self.hand[0][0]
                currentCard = self.isNum(currentCard)
            else:
                currentCard = self.hand[0][0:2]
                currentCard = self.isNum(currentCard)
        else:
            currentCard = card

        return currentCard

#playerOneName = input("Tell me P1 name: ")
#print(f"Welcome, {playerOneName}")
#playerTwoName = input("Tell me P2 name: ")
#print(f"Welcome, {playerTwoName}")

newDeck = Deck(cardNumbers, cardSuite)
shuffledDeck = newDeck.shuffle()
assignedCards = newDeck.assignCards(shuffledDeck)

playerOneCards = Hand(assignedCards[0])  #shuffled cards assigned to P1
playerTwoCards = Hand(assignedCards[1])  #shuffled cards assigned to P2
cardsInGame = []


def gameOver(playerOneCards, playerTwoCards):
    pOneOver = playerOneCards.cardsLeft()
    pTwoOver = playerTwoCards.cardsLeft()

    if (pOneOver == True):
        print("Player 2 has won the game!")
        return True
    elif (pTwoOver == True):
        print("Player 1 has won the game!")
        return True
    else:
        return False

def cardsAcumulator(playerOneWar, playerTwoWar):
    acumCards = []
    acumCards.append(playerOneWar)
    acumCards.append(playerTwoWar)
    return acumCards

def cardsWar(pOneAvCards, pTwoAvCards,InGameCards):

    for i in range(0,3):
        cardsPOne = pOneAvCards.getCard()
        cardsPTwo = pTwoAvCards.getCard()
        InGameCards.append(cardsPOne)
        InGameCards.append(cardsPTwo)
        pOneAvCards.removeCard(cardsPOne)
        pTwoAvCards.removeCard(cardsPTwo)

    compareCards(pOneAvCards,pTwoAvCards,InGameCards)


def getCardType(playerCardType):
    cType = type(playerCardType)
    return cType

def compareCards (playerOneCards, playerTwoCards,cardsInGame):

    playerOneCard = playerOneCards.getCard()
    playerTwoCard = playerTwoCards.getCard()
    playerOne = playerOneCards.getCardNum()
    playerTwo = playerTwoCards.getCardNum()
    pOneType = getCardType(playerOne)
    pTwoType = getCardType(playerTwo)
    playerOneCards.removeCard(playerOneCard)
    playerTwoCards.removeCard(playerTwoCard)

    print(playerOne)
    print(playerTwo)
    print(playerOneCards.cardsLeft())
    print(playerOneCards.cardsLeft())

    if len(cardsInGame) == 0:
        InGameCards = cardsAcumulator(playerOneCard, playerTwoCard)
    else:
        InGameCards = cardsAcumulator(playerOneCard,playerTwoCard)
        cardsInGame.append(InGameCards[0])
        cardsInGame.append(InGameCards[1])
        InGameCards = cardsInGame

    print(InGameCards)

    if ((pOneType == pTwoType) and (pOneType == type("a"))):
        if(playerOne == playerTwo):
            cardsWar(playerOneCards,playerTwoCards,InGameCards)
        else:
            if (playerOne == 'A'):
                playerOneCards.addCard(InGameCards)
            elif (playerTwo == 'A'):
                playerTwoCards.addCard(InGameCards)
            elif (playerOne == 'K'):
                playerOneCards.addCard(InGameCards)
            elif (playerTwo == 'K'):
                playerTwoCards.addCard(InGameCards)
            elif (playerOne == 'Q'):
                playerOneCards.addCard(InGameCards)
            elif (playerTwo == 'Q'):
                playerTwoCards.addCard(InGameCards)

    elif (pOneType != pTwoType):
        if pOneType == type("a"):
            playerOneCards.addCard(InGameCards)
        else:
            playerTwoCards.addCard(InGameCards)

    else:
        if (playerOne > playerTwo):
            playerOneCards.addCard(InGameCards)
        elif (playerTwo > playerOne):
            playerTwoCards.addCard(InGameCards)
        else:
            cardsWar(playerOneCards,playerTwoCards,InGameCards)

while True:
    endGame = gameOver(playerOneCards,playerTwoCards)
    if endGame == False:
        keepGoing = input("Do you want to continue? Y/N")
        if (keepGoing == "Y"):
            compareCards(playerOneCards, playerTwoCards, cardsInGame)
        else:
            break
    else:
        break
