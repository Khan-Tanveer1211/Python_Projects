
def printBoard(xState,zState):
    zero = 'X' if xState[0] else('O' if zState[0] else 0)
    one = 'X' if xState[1]  else('O' if zState[1]  else 1)
    two = 'X' if xState[2]  else('O' if zState[2]  else 2)
    three = 'X' if xState[3] else('O' if zState[3] else 3)
    four = 'X' if xState[4]  else('O' if zState[4]  else 4)
    five = 'X' if xState[5]  else('O' if zState[5]  else 5)
    six = 'X' if xState[6] else('O' if zState[6] else 6)
    seven = 'X' if xState[7]  else('O' if zState[7]  else 7)
    eight = 'X' if xState[8]  else('O' if zState[8]  else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    
def wincheck(xState,zState):
    win_condition =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in win_condition:
        print("the  X cursor is here ", xState[win[0]],xState[win[1]],xState[win[2]])
        if (xState[win[0]] + xState[win[1]] + xState[win[2]] == 3):
            print("X Wons the Match")
            return 1
        print("the 0 cursor is here ", zState[win[0]],zState[win[1]],zState[win[2]])
        if (zState[win[0]] + zState[win[1]] + zState[win[2]] == 3):
            print("0 Wons the Match")
            return 0
    
    return -1   

        #print(xState[win[0]] +xState[win[1]]+ xState[win[2]])

    
if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    
    print( "Welcome to Tic Tac Toa Game !!!!")
    turn = 1 # 1 for X and 0 for O
    print("X's Chance")
    while True:
        printBoard(xState,zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a Value: "))
            xState[value] = 1
        else:
            print("0's Chance")
            value = int(input("Please enter a Value: "))
            zState[value] = 1
        #print("here the cursor")
        check = wincheck(xState,zState)
        print("Check : ", check)
        if check == 1 or check == 0:
            print("Match Win")
            break
        turn = 1 - turn   
        