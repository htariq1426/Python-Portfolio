import itertools
from colorama import Fore, Back, Style, init
init()

def win (current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] !=0:
            return True
        else:
            return False

    # HORIZONTAL
    for row in game:
        print(row)
        if all_same(row):     
            print(f"Player {row[0]} is the winner horizontaly!")

    # DIAGONAL
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])  
    if all_same(diags): 
            print(f"Player {diags[0]} is the winner diagonally (/)!")
            return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags): 
            print(f"Player {diags[0]} is the winner diagonally (\\)!")
            return True

    # VERTICAL
    for col in range(len(game)):
        check = [] # a list

        for row in game:
            check.append(row[col]) #append adds value to list

        if all_same(check): 
            print(f"Player {check[0]} is the winner vertically !")
            return True

    all_filled = True
    for col in range(len(game)):
        if not all_filled:
            break
        for row in range(len(game)):
            if game[row][col] == 0:
                all_filled = False
                break
            elif (row == (len(game)-1) & col == (len(game)-1)):
                print("Game Tied")
                return True
        
    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    
    try:
        if game_map[row][column] !=0:
            print("This position is occupied, Please Choose another one")
            return game_map, False

        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][column] = player
        
        for count, row in enumerate(game): 
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item ==2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)
            
        return game_map, True
    except IndexError as e:
        print("Error: Make sure you enter row/column value as 0,1 or 2?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

play = True
player_choice = itertools.cycle([1, 2])
while play:
    game_size = int(input(" Input the size of Tic Tac Toe game: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False 
    game, _ = game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_choice)
        print(f"Player {current_player}, make your move:")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Game is over, would you like to play another one? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("GoodBye")
                play = False
            else:
                print("Not a valid entry, bye")
                play = False



'''
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
#[] for lists and () for tuples
# Lists can change values, tuples can't
#game is a list of lists
'''
#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, column=1)


#win(game)


#for col, row in zip(reversed(range(len(game))), range(len(game))):
#    print (col, row)
# You can use enumerate as well
# col is indexed from 0 and row is the reversed range of game


'''
DIAGONAL WINNER
diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

#print(diags)


diags = []

for ix in range(len(game)):
    diags.append(game[ix][ix])

#print(diags)

'''

''' HARDCODE of DIAGONAL WINNERS
#if game[0][0] == game[1][1] == game[2][2]:
#   print("Winner")

#if game[2][0] == game[1][1] == game[0][2]:
#    print("Winner")

'''

''' VERTICLE WINNER
for col in range(len(game)):
    check = [] # a list

    for row in game:
        check.append(row[col]) #append adds value to list

    if check.count(check[0]) == len(check) and check[0]!=0:     
            print ("winner!!!")

'''

''' HORIZAONTAL WINNER
def win (current_game):
    for row in game:
        print(row)
        
        
    #    Hardcode of 3 x3   tic tac toe, which is not ideal for scaling
    #    col1 = row[0]
    #    col2 = row[1]
    #    col3 = row[2]
        
    #    if col1 == col2 == col3:
    #        print ("winner!!!")
        


#Taken from stackoverflow,  https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical 

        if row.count(row[0]) == len(row) and row[0]!=0:     
            print ("winner!!!")
            

win(game) 
'''