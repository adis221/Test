from IPython.display import clear_output
clear_output()

def board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])


def choice_piece():
    #initial conditions
    player_pick_choice="string"
    
    #check piece choice acceptable
    while player_pick_choice not in ["X", "Y"]:
        player_pick_choice=input("Welcome to tic tac toe! Player 1, please pick a piece: X or O ")
        
        #if not acceptable ask for accpetable input
        if player_pick_choice not in ["X", "Y"]:
            clear_output()
            print("Please select a viable option ")
    
    #return the player's choice of piece           
    return player_pick_choice


def playerinput():
    #Initial conditions to check
    player_input="can't be a digit to ensure the loop below runs"
    in_range=False
    
    #Run the loop to validate
    while player_input.isdigit()==False or in_range==False: #include isdigit too
        player_input=input("Pick a number 1-9")
        
        #Check range
        if player_input.isdigit()==False:
            clear_output()
            
            print("Please choose a digit")
        
        #Check being in the range
        else:
            if int(player_input) in acceptable_range:
                clear_output()
                acceptable_range.pop(acceptable_range.index(int(player_input)))
                in_range=True
            else:
                
                print("Please choose a number within the range that has not been selected")
     
    return int(player_input)

def gameinplay(list1):

    global game_on
    
    if list1[0]==list1[1]==list1[2] and list1[2]!=" ":
        game_on=False
    elif list1[3]==list1[4]==list1[5] and list1[5]!=" ":
        game_on=False
    elif list1[6]==list1[7]==list1[8] and list1[8]!=" ":
        game_on=False
    elif list1[0]==list1[3]==list1[6] and list1[6]!=" ": 
        game_on=False
    elif list1[1]==list1[4]==list1[7] and list1[7]!=" ":
        game_on=False
    elif list1[2]==list1[5]==list1[8] and list1[8]!=" ":
        game_on=False
    elif list1[0]==list1[4]==list1[8] and list1[8]!=" ":
        game_on=False
    elif list1[2]==list1[4]==list1[6] and list1[6]!=" ":
        game_on=False
    else:
        if (list1[0]!=" " and list1[1]!=" " and list1[2]!=" " and list1[3]!=" " and list1[4]!=" " and list1[5]!=" " and list1[6]!=" " and list1[7]!=" " and list1[8]!=" "):
            game_on=False
        else:
            pass
    
    return game_on
    

def victory(list1):
    
    if list1[0]==list1[1]==list1[2] and list1[2]!=" ":
        print (f"{list1[0]} Wins!")
    elif list1[3]==list1[4]==list1[5] and list1[5]!=" ":
        print (f"{list1[3]} Wins!")
    elif list1[6]==list1[7]==list1[8] and list1[8]!=" ":
        print (f"{list1[6]} Wins!")
    elif list1[0]==list1[3]==list1[6] and list1[6]!=" ":
        print (f"{list1[0]} Wins!")
    elif list1[1]==list1[4]==list1[7] and list1[7]!=" ":
        print (f"{list1[1]} Wins!")
    elif list1[2]==list1[5]==list1[8] and list1[8]!=" ":
        print (f"{list1[2]} Wins!")
    elif list1[0]==list1[4]==list1[8] and list1[8]!=" ":
        print (f"{list1[0]} Wins!")
    elif list1[2]==list1[4]==list1[6] and list1[6]!=" ":
        print (f"{list1[2]} Wins!")
    else:
        if (list1[0]!=" " and list1[1]!=" " and list1[2]!=" " and list1[3]!=" " and list1[4]!=" " and list1[5]!=" " and list1[6]!=" " and list1[7]!=" " and list1[8]!=" "):
            print("Tie game.")
        else:
            print ("error")

def board_manipulationp1():
    
    guess=playerinput()
    r1[guess-1]=p1
    return board(r1)

def board_manipulationp2():
    
    move=playerinput()
    r1[move-1]=p2
    return board(r1)

def replay():
    
    replay_input="Not what I want"
    
    while replay_input not in ["Y", "N"]:
        replay_input=input("Would you like to play again? Y or N? ")
        clear_output()
        
        if replay_input not in ["Y","N"]:
            clear_output()
            print("Please select either uppercase y (Y) for yes or uppercase n (N) for no")
    
    return replay_input=="Y"

#game running
game_on=True
replay_game=True
while replay_game:
    acceptable_range=list(range(1,10))  
    r1=[" ", " "," "," "," "," "," "," "," "]
    options=['X','O']
    p1=choice_piece()
    options.pop(options.index(p1))
    p2=options[0]
    
    while game_on:
     
        board_manipulationp1()
    
        if gameinplay(r1)==False:
            continue
    
        board_manipulationp2()
    
        gameinplay(r1)

    else:
        victory(r1)
        
    if replay()==True:
        game_on=True
    else:
        print ("Thanks for playing!")
        replay_game=False
        

            