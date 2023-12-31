import random

player = random.randint(0,1)
if player == 0:
    playerTurn = " X "
else:
    playerTurn = " O "


def printBoard(Board):
    print("")
    print("---|---|---")
    print(Board[0][0]+"|"+Board[0][1]+"|"+Board[0][2])
    print("---|---|---")
    print(Board[1][0]+"|"+Board[1][1]+"|"+Board[1][2])
    print("---|---|---")
    print(Board[2][0]+"|"+Board[2][1]+"|"+Board[2][2])
    print("---|---|---")


def TerminalGame(playerTurn):
    endgame = True

    instructionsBoard = [
        [" 1 ", " 2 ", " 3 "],
        [" 4 ", " 5 ", " 6 "],
        [" 7 ", " 8 ", " 9 "]
    ]

    gameBoard = [
        ["   ", "   ", "   "],
        ["   ", "   ", "   "],
        ["   ", "   ", "   "]
    ]
    
    print("Terminal TIC-TAC-TOE: ")
    printBoard(instructionsBoard)
    print("\nGet three in a row.")
    print("\n-------------------------------------------")
    print("-------------------------------------------")
    print("\nPlayer Turn: ", playerTurn)
    move = input("Where is your move? (use nums above): ")

    while endgame:
        if move == "1":
            if gameBoard[0][0] == "   ":
                gameBoard[0][0] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "2":
            if gameBoard[0][1] == "   ":
                gameBoard[0][1] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "3":
            if gameBoard[0][2] == "   ":
                gameBoard[0][2] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "4":
            if gameBoard[1][0] == "   ":
                gameBoard[1][0] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "5":
            if gameBoard[1][1] == "   ":
                gameBoard[1][1] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "6":
            if gameBoard[1][2] == "   ":
                gameBoard[1][2] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")
                
        elif move == "7":
            if gameBoard[2][0] == "   ":
                gameBoard[2][0] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "8":
            if gameBoard[2][1] == "   ":
                gameBoard[2][1] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")

        elif move == "9":
            if gameBoard[2][2] == "   ":
                gameBoard[2][2] = playerTurn
                printBoard(gameBoard)

                if playerTurn == " X ":
                    playerTurn = " O "
                else:
                    playerTurn = " X "
                if checkwin(gameBoard):
                    print("Player Turn: ", playerTurn)
                    move = input("Where is your move? (use nums above): ")
                else:
                    endgame = False
            else:
                printBoard(gameBoard)
                print("Bad move. Try again.")
                move = input("Where is your move? (use nums above): ")


def checkwin(gameBoard):
    if gameBoard[0][0] == " O " and gameBoard[0][1] == " O " and gameBoard[0][2] == " O ":
        gameBoard[0][0] = " - "
        gameBoard[0][1] = " - "
        gameBoard[0][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[1][0] == " O " and gameBoard[1][1] == " O " and gameBoard[1][2] == " O ":
        gameBoard[1][0] = " - "
        gameBoard[1][1] = " - "
        gameBoard[1][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")            
    elif gameBoard[2][0] == " O " and gameBoard[2][1] == " O " and gameBoard[2][2] == " O ":
        gameBoard[2][0] = " - "
        gameBoard[2][1] = " - "
        gameBoard[2][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n") 
    elif gameBoard[0][0] == " O " and gameBoard[1][0] == " O " and gameBoard[2][0] == " O ":
        gameBoard[0][0] = " | "
        gameBoard[1][0] = " | "
        gameBoard[2][0] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][1] == " O " and gameBoard[1][1] == " O " and gameBoard[2][1] == " O ":
        gameBoard[0][1] = " | "
        gameBoard[1][1] = " | "
        gameBoard[2][1] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][2] == " O " and gameBoard[1][2] == " O " and gameBoard[2][2] == " O ":
        gameBoard[0][2] = " | "
        gameBoard[1][2] = " | "
        gameBoard[2][2] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][0] == " O " and gameBoard[1][1] == " O " and gameBoard[2][2] == " O ":
        gameBoard[0][0] = " \\ "
        gameBoard[1][1] = " \\ "
        gameBoard[2][2] = " \\ "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[2][0] == " O " and gameBoard[1][1] == " O " and gameBoard[0][2] == " O ":
        gameBoard[2][0] = " / "
        gameBoard[1][1] = " / "
        gameBoard[0][2] = " / "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][0] == " X " and gameBoard[0][1] == " X " and gameBoard[0][2] == " X ":
        gameBoard[0][0] = " - "
        gameBoard[0][1] = " - "
        gameBoard[0][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[1][0] == " X " and gameBoard[1][1] == " X " and gameBoard[1][2] == " X ":
        gameBoard[1][0] = " - "
        gameBoard[1][1] = " - "
        gameBoard[1][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[2][0] == " X " and gameBoard[2][1] == " X " and gameBoard[2][2] == " X ":
        gameBoard[2][0] = " - "
        gameBoard[2][1] = " - "
        gameBoard[2][2] = " - "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][0] == " X " and gameBoard[1][0] == " X " and gameBoard[2][0] == " X ":
        gameBoard[0][0] = " | "
        gameBoard[1][0] = " | "
        gameBoard[2][0] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][1] == " X " and gameBoard[1][1] == " X " and gameBoard[2][1] == " X ":
        gameBoard[0][1] = " | "
        gameBoard[1][1] = " | "
        gameBoard[2][1] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][2] == " X " and gameBoard[1][2] == " X " and gameBoard[2][2] == " X ":
        gameBoard[0][2] = " | "
        gameBoard[1][2] = " | "
        gameBoard[2][2] = " | "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[0][0] == " X " and gameBoard[1][1] == " X " and gameBoard[2][2] == " X ":
        gameBoard[0][0] = " \\ "
        gameBoard[1][1] = " \\ "
        gameBoard[2][2] = " \\ "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    elif gameBoard[2][0] == " X " and gameBoard[1][1] == " X " and gameBoard[0][2] == " X ":
        gameBoard[2][0] = " / "
        gameBoard[1][1] = " / "
        gameBoard[0][2] = " / "
        printBoard(gameBoard)
        if playerTurn == " X ":
            print("Player O WINS!!!!!!\n")
        else:
            print("Player X WINS!!!!!!\n")
    else:
        return True


def main():
    TerminalGame(playerTurn)

if __name__ == "__main__":
    main()
