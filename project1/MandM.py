#This is a test
#from game import Game
import numpy as np
import pygame
import os.path
import time
from os.path import exists

class MandM:
    #Initialize 9x9 that tells you how many edges are at the corresponding coordinate
    #Initialized to all zeros to start the game
    cordEdges = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    def __init__(self):
        #Define board coordinates
        self.board = [[(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9)], 
                      [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)],
                      [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9)],
                      [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9)],
                      [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9)],
                      [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9)],
                      [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9)],
                      [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9)],
                      [(8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9)],
                      [(9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)]]

        #self.decideMove(self.board, self.cordEdges)
        #If player 1 or player 2 files exist, begin running function
        print("hello")
        while(not(os.path.exists('./Megan.go')) and not(os.path.exists('./Michael.go'))):
            if os.path.exists('./Megan.go') or os.path.exists('./Michael.go'):
                #First check if an end game file exists
                if os.path.exists('./end_game.py'):
                    #Display the end result of the game -> read the file because it has the end result of the game
                    File_object = open("end_game.py", "r")
                    File_object.read()
                #Only runs on the first turn and there is nothing in the move file
                elif os.stat("move_file").st_size == 0:
                    self.decideMove(self.board, self.cordEdges)
                #If not the end of the game
                else:
                    #Read the opponents move from move_file
                #    File_object = open("move_file", "r")
                #    File_object.read()
                    self.decideMove(self.board, self.cordEdges)
            print("looping")
            time.sleep(.5)
            

    #Takes in current board and last move
    #board = 9x9 of board coordinates in (x,y)
    #lastMove = (x1,y1) (x2, y2) of move made
    #listOfMoves = list of lastMove 's made
    #cordEdges = 9x9 array that tells you how many edges are attached to that specific coordinate
        #Helps AI in determining where to go (Iterative deepening heuristic that looks for coordinates with 0 or 1 edges connected)
    def decideMove(self, board, cordEdges):
        #lastMove, listOfMoves ^ add back if we need
        #Opens file with all players moves
        #File_object = open("move_file", "r")
        #File_object.close()
        #self.board.get(edge) is used in game.py to see if an edge is taken or not
        #to determine if there is an edge connecting two coordinates, traverse through listOfMoves
        #if we can get the edges, we can store them in an array to keep track
        #when adding r and c values to the list, add them all separately and then append
        #^ append r1 and c1 together, append r2 and c2 together
        #can then search through the list to find the individual edges)
        #myList = [1,2,2,1]
        #myList.append((1,2))
        #myList.append((2,1))
        #myList.append(((1,2), (2,1)))

        #Minimax algo:
        #Explore all options -> store the number of boxes each route captures
        #Start checking the board from left to right, starting at row 0, then row 1, etc
        x = 0
        listOfMoves = []
        while x < 9:
            for y in range(0,10):
                #check number of edges at the given coordinate
                #The first time it runs
                if board[x][y] == (0,0) and cordEdges[0][0] == 0:
                    prevNumEdges = 4
                    numEdges = 0
                elif board[x][y] == (0,0) and cordEdges[0][0] == 1:
                    prevNumEdges = 4
                    numEdges = 0
                elif board[x][y] == (0,0) and cordEdges[0][0] >= 2:
                    prevNumEdges = cordEdges[0][0]
                    numEdges = cordEdges[1][0]
                else:
                    numEdges = cordEdges[x][y]
                    #Check if the previous move has less edges than the current one being explored
                    #Else: run through for loop again until it does
                    #This alpha beta pruning: prunes the other options
                if(prevNumEdges > numEdges):
                    #If it does, set the current move
                    currCoordinate = board[x][y]
                    #When the algo comes to a node, check horizontal options first then vertical (MUST CHECK BOTH)
                    #Case 1: x & y = 0 (can't look left or above)
                    if x == 0 & y == 0:
                        leftCoordinate = board[x][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y]
                        bottomCoordinate = board[x][y-1]
                    
                    #case 2: can't look left
                    elif x == 0:
                        leftCoordinate = board[x][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y+1]
                        bottomCoordinate = board[x][y-1]

                    #case 3: y = 0 (can't look above)
                    elif y == 0:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y]
                        topCoordinate = board[x][y] 
                        bottomCoordinate = board[x][y-1]

                    #Case 4: x & y = 9 (can't look right or beneath)
                    elif x == 9 & y == 9:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x][y]
                        topCoordinate = board[x][y+1]
                        bottomCoordinate = board[x][y]

                    #Case 5: x = 9 (can't look right)
                    elif x == 9:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y]
                        topCoordinate = board[x][y+1]
                        bottomCoordinate = board[x][y-1]

                    #Case 6: y = 9 (can't look beneath)
                    elif y == 9:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y+1]
                        bottomCoordinate = board[x][y]

                    #Case 7: normal case
                    else:      
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y+1]
                        bottomCoordinate = board[x][y-1]

                    #Want to check if there are less than two edges at the node next to the choice
                    #Break ties: pick from left to right then up to down
                    if cordEdges[x-1][y] < 2 and x != 0:
                        #Current chosen move
                        chosenMove = (currCoordinate), (leftCoordinate)
                        if chosenMove in listOfMoves:
                            continue
                        else:
                            #Current chosen move
                            listOfMoves.append(chosenMove)
                            #Opens file with all players moves
                            #Checks if a box was closed, if so then the player passes
                            if os.path.exists('./Megan.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Checks if a box was closed, if so then the player passes
                            elif os.path.exists('./Michael.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Megan.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Michael.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Closes file until next turn
                            File_object.close()
                        #Add 1 to number of edges at those nodes
                        cordEdges[x][y] = cordEdges[x][y] + 1
                        cordEdges[x-1][y] = cordEdges[x-1][y] + 1
                        prevNumEdges = numEdges
                        break

                    elif cordEdges[x+1][y] < 2 and x != 8:
                        chosenMove = (currCoordinate), (rightCoordinate)
                        if chosenMove in listOfMoves:
                            continue
                        else:
                            #Current chosen move
                            listOfMoves.append(chosenMove)
                            #Opens file with all players moves
                            #Checks if a box was closed, if so then the player passes
                            if os.path.exists('./Megan.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Checks if a box was closed, if so then the player passes
                            elif os.path.exists('./Michael.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Megan.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan " +str(chosenMove))
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Michael.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael " +str(chosenMove))
                                File_object.close()
                                test = MandM()

                            #Closes file until next turn
                            #Add 1 to number of edges at those nodes
                            cordEdges[x][y] = cordEdges[x][y] + 1
                            cordEdges[x+1][y] = cordEdges[x+1][y] + 1
                            prevNumEdges = numEdges
                            break

                    elif cordEdges[x][y-1] < 2 and y != 0:
                        #Current chosen move
                        chosenMove = (currCoordinate), (topCoordinate)
                        if chosenMove in listOfMoves:
                            continue
                        else:
                            #Current chosen move
                            listOfMoves.append(chosenMove)
                            #Opens file with all players moves
                            #Checks if a box was closed, if so then the player passes
                            if os.path.exists('./Megan.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Checks if a box was closed, if so then the player passes
                            elif os.path.exists('./Michael.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Megan.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Michael.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Closes file until next turn
                        #Add 1 to number of edges at those nodes
                        cordEdges[x][y] = cordEdges[x][y] + 1
                        cordEdges[x][y-1] = cordEdges[x][y-1] + 1
                        prevNumEdges = numEdges
                        break
                        
                    elif cordEdges[x][y+1] < 2 and y != 8:
                        #Current chosen move
                        chosenMove = (currCoordinate), (bottomCoordinate)
                        if chosenMove in listOfMoves:
                            continue
                        else:
                            #Current chosen move
                            listOfMoves.append(chosenMove)
                            #Opens file with all players moves
                            #Checks if a box was closed, if so then the player passes
                            if os.path.exists('./Megan.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Checks if a box was closed, if so then the player passes
                            elif os.path.exists('./Michael.pass'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael 0,0 0,0")
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Megan.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Megan " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Writes in selected move from decideMove() if it is player's turn
                            elif os.path.exists('./Michael.go'):
                                File_object = open("move_file", "w")
                                File_object.write("Michael " +chosenMove)
                                File_object.close()
                                test = MandM()
                            #Closes file until next turn
                        #Add 1 to number of edges at those nodes
                        cordEdges[x][y] = cordEdges[x][y] + 1
                        cordEdges[x][y+1] = cordEdges[x][y+1] + 1
                        prevNumEdges = numEdges
                        break
                    
                    #case where we don't want to go here: go back to start of nested for loop
                    else:
                        prevNumEdges = numEdges
                        if y == 8:
                            x = x+1
                #Case where box already exists here
                else:
                    continue

        #Once one node has 2 lines branching off it:
            #Look at array of nodes not taken from left to right
            #If the next route explored captures less than the previous ones, prune
            #Tree: start node, 8!, 7!, 6!,...
            #Use iterative deepening: only check the next move after to see if there is a better move
            #"better move" = less lines connected to that node
            #Would need to check how many lines are connected to current node and node next to it
            #If box is closed, that player gets to go again


    #Helper function used: iterative deepening
    #Want to check next move which allows us to deepen & prune at a level of 2
    #Given the first chosen move, we want to check what the next player would play
    #If the next players move 
    #def decideMove2(move):

    
    #Update board based on AI's last move
    def updateBoard(self, move):
        #Opens file with all players moves
        File_object = open("move_file", "w")
        #Checks if a box was closed, if so then the player passes
        if os.path.exists('./Megan.pass'):
            File_object.write("Megan 0,0 0,0")
        #Checks if a box was closed, if so then the player passes
        elif os.path.exists('./Michael.pass'):
            File_object.write("Michael 0,0 0,0")
        #Writes in selected move from decideMove() if it is player's turn
        elif os.path.exists('./Megan.go'):
            File_object.write("Megan " +move)
        #Writes in selected move from decideMove() if it is player's turn
        elif os.path.exists('./Michael.go'):
            File_object.write("Michael " +move)
        #Closes file until next turn
        File_object.close()

if __name__ == "__main__":
    print("detected")
    test = MandM()
    print("ended")