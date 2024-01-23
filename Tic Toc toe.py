def gameBoard ():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end="  ")
        print()  

game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]  
gameBoard()       


while True:
    print("*--Player 1--*")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    game[row][col]="X"
    gameBoard()

    print("*--Player 2--*")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    game[row][col]="O"
    gameBoard()

