#Users/denzelbalbosa/Documents/Python_Projects/final_project.py
#Denzel Balbosa

import random
import sys
import time

#Prints the board table when called
def get_board(lst):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|", end="")
        for j in range(3):
            print("  ", lst[i][j], end="   |")
        print("\n|       |       |       |")
        print("+-------+-------+-------+")

#Checks if there's a winner
        #Returns 1 if player wins, 2 if AI wins and 3 if it's a tie
def get_winner(lst):
    #Checks horizontal and vertical
    for i in range(3):
        if lst[i][0] == lst[i][1] == lst[i][2]:
            if lst[i][0] == 'O':
                return 1
            elif lst[i][0] == 'X':
                return 2
        elif lst[0][i] == lst[1][i] == lst[2][i]:
            if lst[0][i] == 'O':
                return 1
            elif lst[0][i] == 'X':
                return 2
    #Checks other posibilities to win
    if lst[0][0] == lst[1][1] == lst[2][2]:
        if lst[0][0] == 'O':
            return 1
        elif lst[0][0] == 'X':
            return 2
    elif lst[0][2] == lst[1][1] == lst[2][0]:
        if lst[0][2] == 'O':
            return 1
        elif lst[0][2] == 'X':
            return 2
    #Runs through the list and check if there's any spot available by type int
    for row in lst:
        empty_spot = [(i, j) for i in range(3) for j in range(3) if isinstance(lst[i][j], int)]
        if not empty_spot:
            return 0
    return -1

#User's turn - requires a list perameter
    #Returns the new list
def user_turn(lst):
    while True:
        #Ask the user for input
        user_input = int(input("Enter a spot (1-9): "))
        if 0 < user_input < 10:
            #Converts the input into a number within the range of the dimensions
            i = (user_input - 1) // 3
            j = (user_input - 1) % 3
            #Makes sure that the user's input is a valid option by checking if it's an int
            if isinstance(lst[i][j], int):
                lst[i][j] = 'O'
                break
            else:
                print("That option is already occupied.")
        else:
            print("You entered an invalid key.")
    return lst

#AI's turn by random
    #Returns a new list
def ai_turn(lst):
    #Iterates to all the values in the list and mark it as empty
    empty_spots = [(i, j) for i in range(3) for j in range(3) if isinstance(lst[i][j], int)]
    #Ramdomizes the list created that is available
    i, j = random.choice(empty_spots)
    lst[i][j] = 'X'
    return lst

#AI in hard mode turn
def ai_hard(lst):
    # Check rows and columns for possible winning moves
    for i in range(3):
        # Check rows
        if lst[i][0] == lst[i][1] and isinstance(lst[i][2], int):
            lst[i][2] = 'X'
            return lst
        elif lst[i][0] == lst[i][2] and isinstance(lst[i][1], int):
            lst[i][1] = 'X'
            return lst
        elif lst[i][1] == lst[i][2] and isinstance(lst[i][0], int):
            lst[i][0] = 'X'
            return lst
        # Check columns
        elif lst[0][i] == lst[1][i] and isinstance(lst[2][i], int):
            lst[2][i] = 'X'
            return lst
        elif lst[0][i] == lst[2][i] and isinstance(lst[1][i], int):
            lst[1][i] = 'X'
            return lst
        elif lst[1][i] == lst[2][i] and isinstance(lst[0][i], int):
            lst[0][i] = 'X'
            return lst

    # Check diagonals for possible winning moves
    if lst[0][0] == lst[1][1] and isinstance(lst[2][2], int):
        lst[2][2] = 'X'
        return lst
    elif lst[0][0] == lst[2][2] and isinstance(lst[1][1], int):
        lst[1][1] = 'X'
        return lst
    elif lst[2][2] == lst[1][1] and isinstance(lst[0][0], int):
        lst[0][0] = 'X'
        return lst
    elif lst[0][2] == lst[1][1] and isinstance(lst[2][0], int):
        lst[2][0] = 'X'
        return lst
    elif lst[0][2] == lst[2][0] and isinstance(lst[1][1], int):
        lst[1][1] = 'X'
        return lst
    elif lst[1][1] == lst[2][0] and isinstance(lst[0][2], int):
        lst[0][2] = 'X'
        return lst

    # If no winning move is found, make a random move
    empty_spots = [(i, j) for i in range(3) for j in range(3) if isinstance(lst[i][j], int)]
    i, j = random.choice(empty_spots)
    lst[i][j] = 'X'
    
    return lst

#Introduction and instruction
def introduction():
    #AI fun variables
    rand_ai_sec = [1, 2, 3, 4, 5]
    rand_ai_words = ["hmmm..", "maybe...", "Aha!", "Actaully..", "Nah", "HmMm", "Ehh"]
    hard_mode = False

    print("Welcome to a Tic-Tac-Toe game")
    print("Beat the AI by getting 3 marks in a row")
    time.sleep(1)

    #Ask for the user's name
    user_name = str(input("Please enter your name: "))
    file_name = user_name + ".txt"
    while True:
        ai_dificulty = int(input("Enter \"1\" for Normal difficulty and \"2\" for Very hard: "))
        if ai_dificulty == 1:
            print("You've chosen the right path.")
            break
        elif ai_dificulty == 2:
            print("You have chosen the wrong path. Good luck!")
            hard_mode = True
            break
        else:
            print("You entered a wrong key")
    time.sleep(2)
    print()
    print()

    #Tries to find a file by the name
    #If data is found, it will continue the existing record
    #If it does not exist, it will catch it and creates a new one
    try:
        with open(file_name, "r") as file:
            print("You have an existing data", user_name, end="!")
            while True:
                user_key = str(input("\nDid you want to continue?(Yes or No): ")).lower()
                if user_key == 'yes' or user_key == 'y':
                    wins = int(file.readline())
                    lost = int(file.readline())
                    break
                elif user_key == 'no' or user_key == 'n':
                    wins = 0
                    lost = 0
                    break
                else:
                    print("You entered an invalid key")
        print("Your current score is:", wins, "wins and", lost, "loses.")
        time.sleep(1)
        print()
    except FileNotFoundError:
        print("You don't have an existing data")
        wins = 0
        lost = 0
        print("Your current score is:", wins, "wins and", lost, "loses.")
        time.sleep(1)
        print()

    #A loop used for the player and AI's turn
    #Loop stops when game ends by winning, losing or a tie
    while True:
        board_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = None
        print("Starting game...")
        print("Computer's turn first")
        board_lst[1][1] = 'X'
        get_board(board_lst)
        time.sleep(2)
        print()
        print()

        while True:
            #Calls the user_turn function to get input
            get_board(board_lst)
            print("Player's turn:")
            board_lst = user_turn(board_lst)
            #Checks if there's a winner after User's turn
            winner = get_winner(board_lst)
            print()
            print()
            if winner == 1:
                result = 1
                break
            elif winner == 2:
                result = 2
                break
            elif winner == 0:
                result = 0
                break
            
            print()
            time.sleep(1)

            #Calls the ai_turn function to get random input
            get_board(board_lst)
            print("AI's turn:")
            print("AI is thinking....(Yes the AI is thinking)")
            for sec in range(random.choice(rand_ai_sec)):
                print("AI:", random.choice(rand_ai_words))
                time.sleep(1)
            if hard_mode:
                board_lst = ai_hard(board_lst)
            else:
                board_lst = ai_turn(board_lst)
            #Checks if there's a winner after AI's turn
            winner = get_winner(board_lst)
            print()
            print()
            if winner == 1:
                result = 1
                break
            elif winner == 2:
                result = 2
                break
            elif winner == 0:
                result = 0
                break
            print()
            time.sleep(1)

        #Shows the final board and result
        if result == 1:
            get_board(board_lst)
            print("You won!")
            wins += 1
        elif result == 2:
            get_board(board_lst)
            print("You lost")
            lost += 1
        else:
            get_board(board_lst)
            print("It's a tie!")

        #Shows the current record and asks the user to play again
        #If player answers yes, the loop will run again if not it will create and record the file data
        print("Your current record is now:", wins, "wins and", lost, "loses.")
        time.sleep(1)
        user_choice = input("\nPlay again? (Yes or No): ").lower()
        if user_choice != 'yes' and user_choice != 'y':
            with open(file_name, "w") as file:
                file.write(str(wins) + "\n")
                file.write(str(lost) + "\n")
            print("Thanks for playing", user_name, end="!")
            sys.exit()

#Starts the program
introduction()