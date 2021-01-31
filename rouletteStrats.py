import random

def setWinningNumber():
    winningNumber = random.randint(0,37)
    """
    if winningNumber == 37:
        winningNumber = str("Double Zero")
        print("Double Zero: " + str(winningNumber))
    else:
        winningNumber = str(winningNumber)
    """

    winningNumber = str(winningNumber)

    if winningNumber <= 9 and winningNumber >= 1:
        winningNumber = "0" + str(winningNumber)

    return winningNumber

"""def isBlack(number, BlackNumList):
    if number in BlackNumList:
        return True
    else:
        return False
"""
def getColor(number):
    #Colors
    blackNumList = ["28", "26", "11", "20", "17", "22", "15", "24", "13", "27", "25", "12", "19", "18", "21", "16", "23", "14"]
    redNumList = ["09", "30", "07", "32", "05", "34", "03", "36", "01", "10", "29", "08", "31", "06", "33", "04", "35", "02"]
    greenNumList = ["0", "00", "37"]

    if number in blackNumList:
        return "Black"
    elif number in redNumList:
        return "Red"
    elif number in greenNumList:
        return "Green"
    else:
        return "Unexpected color value"

def getOddOrEven(number):
    if int(number) % 2 == 0:
        return "Even"
    else:
        return "Odd"

def getQuadrant(number):
    #Quadrants
    quad1 = ["28", "26", "11", "20", "17", "22", "15", "24"]
    quad2 = ["09", "30", "07", "32", "05", "34", "03", "36"]
    quad3 = ["01", "10", "29", "08", "31", "06", "33", "04", "35", "02"]
    quad4 = ["13", "27", "25", "12", "19", "18", "21", "16", "23", "14"]

    if numer in quad1:
        return "Quad 1"
    elif number in quad2:
        return "Quad 2"
    elif number in quad3:
        return "Quad 3"
    elif number in quad4:
        return "Quad 4"
    else:
        return "Unexpected error for " + number

def getThirds(number):
    #thirds
    firstThird = ["28", "26", "11", "20", "17", "22", "15", "24", "09", "30", "07", "32"]
    secondThird = ["05", "34", "03", "36", "01", "10", "29", "08", "31", "06", "33", "04"]
    thirdThird = ["35", "02", "13", "27", "25", "12", "19", "18", "21", "16", "23", "14"]

    if number in firstThird:
        return "First Third"
    elif number in secondThird:
        return "Second Third"
    elif number in thirdThird:
        return "Third Third"

def getColorBetWinLose(color, colorBet):
    if color is colorBet:
        return "Win"
    elif color is not colorBet:
        return "Lose"
    else:
        return "Unexpected Error"

def get24Plus8WinLose(number):
    number = str(number)
    if number == "0" or number == "00" or number == "16" or number == "19" or number == "37":
        return "Lose"
    elif number >= "13" and number <= "24":
        return "Win"
    else:
        return "Push"

def main():
    dollars = 0
    spins = 0
    streak = 0
    highBlackStreak = 0
    highRedStreak = 0
    win = 0
    push = 0
    lose = 0
    winningNumber = 0

    playerColor = "N/A"
    colorWinLoss = "N/A"
    colorWins = 0
    colorLoses = 0

    spins = input("How many spins do you want to play: ")
    #dollars = input("How many dollars are you starting with: ")
    colorBet = raw_input("Black or Red: ")
    twentyFourPlusEightWin = 0
    twentyFourPlusEightLose = 0
    twentyFourPlusEightPush = 0
    twentyFourPlusEightLoseStreak = 0
    twentyFourPlusEightLoseHighStreak = 0

    if (colorBet == "B"):
        playerColor = "Black"

    for i in range(spins):
        winningNumber = str(setWinningNumber())
        oddOrEven = getOddOrEven(winningNumber)
        color = getColor(str(winningNumber))
        twentyFourPlusEightWinLose = get24Plus8WinLose(str(winningNumber))


        colorWinLoss = getColorBetWinLose(color, playerColor)
        if colorWinLoss is "Win":
            colorWins = colorWins + 1
        elif colorWinLoss is "Lose":
            colorLoses = colorLoses + 1
        else:
            colorWinLoss = "Unexpected Error"

        if twentyFourPlusEightWinLose is "Win":
            twentyFourPlusEightWin = twentyFourPlusEightWin + 1
            twentyFourPlusEightLoseStreak = 0
        elif twentyFourPlusEightWinLose is "Lose":
            twentyFourPlusEightLose = twentyFourPlusEightLose + 1
            twentyFourPlusEightLoseStreak = twentyFourPlusEightLoseStreak + 1
        elif twentyFourPlusEightWinLose is "Push":
            twentyFourPlusEightPush = twentyFourPlusEightPush + 1

        if twentyFourPlusEightLoseHighStreak < twentyFourPlusEightLoseStreak:
            twentyFourPlusEightLoseHighStreak = twentyFourPlusEightLoseStreak

        print("Spin " + str(i + 1))
        print("------------")
        print(winningNumber)
        print("Winning Number is: " + str(winningNumber))

        print("Color: " + color)
        print("Odd or Even: " + oddOrEven)
        print("")
        print("Color Bet: " + colorWinLoss)
        print ("Color Wins:" + str(colorWins))
        print ("Color Loses:" + str(colorLoses))
        print("24 + 8 Win/Lose/Push: " + twentyFourPlusEightWinLose)
        print ("24 + 8 Wins: " + str(twentyFourPlusEightWin))
        print ("24 + 8 Loses: " + str(twentyFourPlusEightLose))
        print ("24 + 8 Push: " + str(twentyFourPlusEightPush))
        print("24 + 8 High Streak:" + str(twentyFourPlusEightLoseHighStreak))
        print("")

if __name__ == '__main__':
    main()
