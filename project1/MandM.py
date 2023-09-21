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
    listOfMoves = [[((0,0), (0,0)), ((0,1), (0,1)), ((0,2), (0,2)), ((0,3), (0,3)), ((0,4), (0,4)), ((0,5), (0,5)), ((0,6), (0,6)), ((0,7), (0,7)), ((0,8), (0,8)), ((0,9), (0,9))],
                   [((1,0), (1,0)), ((1,1), (1,1)), ((1,2), (1,2)), ((1,3), (1,3)), ((1,4), (1,4)), ((1,5), (1,5)), ((1,6), (1,6)), ((1,7), (1,7)), ((1,8), (1,8)), ((1,9), (1,9))],
                   [((2,0), (2,0)), ((2,1), (2,1)), ((2,2), (2,2)), ((2,3), (2,3)), ((2,4), (2,4)), ((2,5), (2,5)), ((2,6), (2,6)), ((2,7), (2,7)), ((2,8), (2,8)), ((2,9), (2,9))],
                   [((3,0), (3,0)), ((3,1), (3,1)), ((3,2), (3,2)), ((3,3), (3,3)), ((3,4), (3,4)), ((3,5), (3,5)), ((3,6), (3,6)), ((3,7), (3,7)), ((3,8), (3,8)), ((3,9), (3,9))],
                   [((4,0), (4,0)), ((4,1), (4,1)), ((4,2), (4,2)), ((4,3), (4,3)), ((4,4), (4,4)), ((4,5), (4,5)), ((4,6), (4,6)), ((4,7), (4,7)), ((4,8), (4,8)), ((4,9), (4,9))],
                   [((5,0), (5,0)), ((5,1), (5,1)), ((5,2), (5,2)), ((5,3), (5,3)), ((5,4), (5,4)), ((5,5), (5,5)), ((5,6), (5,6)), ((5,7), (5,7)), ((5,8), (5,8)), ((5,9), (5,9))],
                   [((6,0), (6,0)), ((6,1), (6,1)), ((6,2), (6,2)), ((6,3), (6,3)), ((6,4), (6,4)), ((6,5), (6,5)), ((6,6), (6,6)), ((6,7), (6,7)), ((6,8), (6,8)), ((6,9), (6,9))],
                   [((7,0), (7,0)), ((7,1), (7,1)), ((7,2), (7,2)), ((7,3), (7,3)), ((7,4), (7,4)), ((7,5), (7,5)), ((7,6), (7,6)), ((7,7), (7,7)), ((7,8), (7,8)), ((7,9), (7,9))],
                   [((8,0), (8,0)), ((8,1), (8,1)), ((8,2), (8,2)), ((8,3), (8,3)), ((8,4), (8,4)), ((8,5), (8,5)), ((8,6), (8,6)), ((8,7), (8,7)), ((8,8), (8,8)), ((8,9), (8,9))],
                   [((9,0), (9,0)), ((9,1), (9,1)), ((9,2), (9,2)), ((9,3), (9,3)), ((9,4), (9,4)), ((9,5), (9,5)), ((9,6), (9,6)), ((9,7), (9,7)), ((9,8), (9,8)), ((9,9), (9,9))]]
    x = 0
    n = 0
    #initialize a current move variable for checking if boxes are taken
    currentMove = ((0,0), (0,0))

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
        #If player 1 or player 2 files don't exist
        if(os.path.exists('./Megan.go') == False and os.path.exists('./Michael.go') == False):
            #n is the variable that will tell us when the file exists
            n = 0
            while(n==0):
                #if a go file exists OR a pass file (because we want the player to go through the same process)
                if os.path.exists('./Megan.go') or os.path.exists('./Michael.go') or os.path.exists('./Megan.pass') or os.path.exists('./Michael.pass'):
                    #set n to 1 saying that the go file or pass file exists
                    n = n+1
                    #First check if an end game file exists
                    if os.path.exists('./end_game.py'):
                        #Display the end result of the game -> read the file because it has the end result of the game
                        File_object = open("end_game.py", "r")
                        File_object.read()
                    #If not the end of the game 
                        #check to see if there are any boxes to close
                        #if there are no boxes to close, run the decideMove function
                        #if there are boxes to close, write that move to the file and set n = 0 to re-loop
                    else:
                        #Loop to check if there are any boxes to close
                        if self.n == 0:
                            c = 0
                            while c <= 9:
                                for r in range(0,10):
                                    #set coordinates to reference when determining if we can close a box
                                    currCoordinate = [c][r]
                                    leftCoordinate = [c][r-1]
                                    rightCoordinate = [c][r+1]
                                    topCoordinate = [c-1][r]
                                    bottomCoordinate = [c+1][r]
                                    topLeftCoordinate = [c-1][r-1]
                                    topRightCoordinate = [c-1][r+1]
                                    bottomLeftCoordinate = [c+1][r-1]
                                    bottomRightCoordinate = [c+1][r+1]
                                    #start at (0,0)
                                    #if y = 0 & x = 0, check bottom right (Q4)
                                    if r == 0 and c == 0:
                                        #bottom right (1)
                                        if ((rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves):
                                            currentMove = (currCoordinate, rightCoordinate)
                                        #bottom right (2)
                                        elif ((rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, rightCoordinate) in self.listOfMoves):
                                            currentMove = (currCoordinate, bottomCoordinate)
                                    #if y = 9 & x = 9, check top left box (Q2)
                                    elif r == 9 and c == 9:
                                        #top left (1)
                                        if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, currCoordinate) in self.listOfMoves):
                                            #close rigt of box
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top left (2)
                                        elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                        and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate)):
                                            #close bottom of box
                                            currentMove = (bottomLeftCoordinate, currCoordinate)

                                    #if r = 0 & c > 0, check bottom left and bottom right
                                    elif r == 0 and c > 0 and c < 9:
                                    #checking left
                                        #bottom left (1)
                                        if((currCoordinate, leftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                        #bottom left (2)
                                        elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves):
                                            #close right line
                                            currentMove = (currCoordinate, bottomCoordinate)
                                    #checking right
                                        #bottom right (1)
                                        elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomCoordinate, bottomRightCoordinate)
                                        #bottom right (2)
                                        elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, bottomCoordinate)

                                    #if x = 0 & y > 0, check top right and bottom right
                                    elif c == 0 and r > 0 and r < 9:
                                        #top right (1)
                                        if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, rightCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top right (2)
                                        elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, topCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (currCoordinate, rightCoordinate)
                                        #bottom right (1)
                                        elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomCoordinate, bottomRightCoordinate)
                                        #bottom right (2)
                                        elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, bottomCoordinate)
                                        
                                    #if y = 9 & x > 0, check top right and top left
                                    elif r == 9 and c > 0 and c < 9:
                                        #top right (1)
                                        if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, rightCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top right (2)
                                        elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, topCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (currCoordinate, rightCoordinate)
                                        #top left (1)
                                        if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, currCoordinate) in self.listOfMoves):
                                            #close rigt of box
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top left (2)
                                        elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                        and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate)):
                                            #close bottom of box
                                            currentMove = (bottomLeftCoordinate, currCoordinate)

                                    #if x = 9 & y > 0, check top and bottom left
                                    elif c == 9 and r > 0 and r < 9:
                                        #top left (1)
                                        if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, currCoordinate) in self.listOfMoves):
                                            #close rigt of box
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top left (2)
                                        elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                        and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate)):
                                            #close bottom of box
                                            currentMove = (bottomLeftCoordinate, currCoordinate)
                                        #bottom left (1)
                                        if((currCoordinate, leftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                        #bottom left (2)
                                        elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves):
                                            #close right line
                                            currentMove = (currCoordinate, bottomCoordinate)

                                    #if x = 9 & y = 0, check bottom left
                                    elif c == 9 and r == 0:
                                        #bottom left (1)
                                        if((currCoordinate, leftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                        #bottom left (2)
                                        elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves):
                                            #close right line
                                            currentMove = (currCoordinate, bottomCoordinate)

                                    #if y = 9 & x = 0, check top right
                                    elif r == 9 and c == 0:
                                        #top right (1)
                                        if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, rightCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top right (2)
                                        elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, topCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (currCoordinate, rightCoordinate)

                                    #check all quadrants
                                    elif r > 0 and  r < 9 and c > 0 and  c < 9:
                                        #top right (1)
                                        if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, rightCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top right (2)
                                        elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                        and (currCoordinate, topCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (currCoordinate, rightCoordinate)
                                        #top left (1)
                                        if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, currCoordinate) in self.listOfMoves):
                                            #close rigt of box
                                            currentMove = (currCoordinate, topCoordinate)
                                        #top left (2)
                                        elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                        and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                        and (leftCoordinate, topLeftCoordinate)):
                                            #close bottom of box
                                            currentMove = (bottomLeftCoordinate, currCoordinate)
                                        #bottom left (1)
                                        if((currCoordinate, leftCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                        #bottom left (2)
                                        elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                        and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                        and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves):
                                            #close right line
                                            currentMove = (currCoordinate, bottomCoordinate)
                                        #bottom right (1)
                                        elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                        and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves):
                                            #close bottom line
                                            currentMove = (bottomCoordinate, bottomRightCoordinate)
                                        #bottom right (2)
                                        elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                        and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                        and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves):
                                            #close left line
                                            currentMove = (currCoordinate, bottomCoordinate)

                                    if currCoordinate[c][r] == (9,9):
                                        self.n = self.n+1
                                    #once loop runs and doesn't find a square to close, n++
                        #if the currentMove has changed, a box has been located
                        #write that move to the file using corresponding players name
                        if currentMove != ((0,0), (0,0)) and os.path.exists('./Megan.go'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +currentMove)
                                    File_object.close()
                                    n = 0
                                    time.sleep(.1)
                        elif currentMove != ((0,0), (0,0)) and os.path.exists('./Michael.go'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +currentMove)
                                    File_object.close()
                                    n = 0
                                    time.sleep(.1)
                        #case where the move hasn't changed -> go into the decide move function
                        else:
                            self.decideMove(self.board, self.cordEdges)
                time.sleep(.5)
        #else:
                #First check if an end game file exists
        #        if os.path.exists('./end_game.py'):
                    #Display the end result of the game -> read the file because it has the end result of the game
        #            File_object = open("end_game.py", "r")
        #            File_object.read()
                #Only runs on the first turn and there is nothing in the move file
        #        elif os.stat("move_file").st_size == 0:
        #            self.decideMove(self.board, self.cordEdges)
                #If not the end of the game
        #        else:
                    #Read the opponents move from move_file
                #    File_object = open("move_file", "r")
                #    File_object.read()
        #            self.decideMove(self.board, self.cordEdges)    

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
        
        while self.x <= 9:
            for y in range(0,10):
                #Check to see if a box can be closed before anything else
                #Check edges around the point (in a 3x3 grid) to see if the edges are taken
                #Check left then right then up then down
                #check number of edges at the given coordinate
                #The first time it runs

                if board[self.x][y] == (0,0) and cordEdges[0][0] == 0:
                    prevNumEdges = 4
                    numEdges = 0
                elif board[self.x][y] == (0,0) and cordEdges[0][0] == 1:
                    prevNumEdges = 4
                    numEdges = 0
                elif board[self.x][y] == (0,0) and cordEdges[0][0] >= 2:
                    prevNumEdges = cordEdges[0][0]
                    numEdges = cordEdges[1][0]
                #elif self.x == 0 and not y == 0:
                    #prevNumEdges = cordEdges[9][y-1]
                    #numEdges = cordEdges[self.x][y]
                #elif y == 0 and not self.x== 0:
                    #prevNumEdges = cordEdges[self.x-1][9]
                    #numEdges = cordEdges[self.x][y]
                else:
                    numEdges = cordEdges[self.x][y]
                    #Check if the previous move has less edges than the current one being explored
                    #Else: run through for loop again until it does
                    #This alpha beta pruning: prunes the other options
                if(prevNumEdges > numEdges):
                    #If it does, set the current move
                    currCoordinate = board[self.x][y]
                    #When the algo comes to a node, check horizontal options first then vertical (MUST CHECK BOTH)
                    
                    #Case 1: x & y = 0 (can't look left or above)
                    if self.x == 0 and y == 0:
                        leftCoordinate = board[self.x][y]
                        rightCoordinate = board[self.x][y+1] 
                        topCoordinate = board[self.x][y]
                        bottomCoordinate = board[self.x+1][y]
                    
                    elif self.x == 0 and y == 9:
                        leftCoordinate = board[self.x][y-1]
                        rightCoordinate = board[self.x][y]
                        topCoordinate = board[self.x][y] 
                        bottomCoordinate = board[self.x+1][y]

                    elif self.x == 9 and y==0:
                        leftCoordinate = board[self.x][y]
                        rightCoordinate = board[self.x][y+1] 
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x][y]
                    
                    #case 2: can't look left
                    elif y == 0:
                        leftCoordinate = board[self.x][y]
                        rightCoordinate = board[self.x][y+1] 
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x+1][y]

                    #case 3: y = 0 (can't look above)
                    elif self.x == 0:
                        leftCoordinate = board[self.x][y-1]
                        rightCoordinate = board[self.x][y+1]
                        topCoordinate = board[self.x][y] 
                        bottomCoordinate = board[self.x+1][y]

                    #Case 4: x & y = 9 (can't look right or beneath)
                    elif self.x == 9 and y == 9:
                        leftCoordinate = board[self.x][y+1]
                        rightCoordinate = board[self.x][y]
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x][y]

                    #Case 5: x = 9 (can't look right)
                    elif y == 9:
                        leftCoordinate = board[self.x][y-1]
                        rightCoordinate = board[self.x][y]
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x+1][y]

                    #Case 6: y = 9 (can't look beneath)
                    elif self.x == 9:
                        leftCoordinate = board[self.x][y-1]
                        rightCoordinate = board[self.x][y+1] 
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x][y]

                    #Case 7: normal case
                    else:      
                        leftCoordinate = board[self.x][y-1]
                        rightCoordinate = board[self.x][y+1] 
                        topCoordinate = board[self.x-1][y]
                        bottomCoordinate = board[self.x+1][y]
                    if y < 9:
                        if cordEdges[self.x][y+1] < 2:
                            # ^ originally an elif
                            chosenMove = (currCoordinate), (rightCoordinate)
                            reverse = (rightCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            #((0,0), (1,0))
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            #0, 0, 1, 0
                            #0123456789
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            #Want to check the reverse as well since we are looking at edges
                            if chosenMove in self.listOfMoves or reverse in self.listOfMoves:
                                if y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    y=0
                                continue
                            else:
                                #Current chosen move
                                #Also append the reverse of the move because we are checking edges
                                self.listOfMoves.append(chosenMove)
                                self.listOfMoves.append(reverse)
                                #Opens file with all players moves
                                #Checks if a box was closed, if so then the player passes
                                if os.path.exists('./Megan.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Checks if a box was closed, if so then the player passes
                                elif os.path.exists('./Michael.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Megan.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Closes file until next turn
                                #Add 1 to number of edges at those nodes
                                cordEdges[self.x][y] = cordEdges[self.x][y] + 1
                                cordEdges[self.x][y+1] = cordEdges[self.x][y+1] + 1
                                prevNumEdges = numEdges
                                self.n = 0
                                if y==9:
                                    self.x=self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    y=0
                                test = MandM()
                                break

                    #Want to check if there are less than two edges at the node next to the choice
                    #Break ties: pick from left to right then up to down
                    if y > 0:
                        if cordEdges[self.x][y-1] < 2:
                            #Current chosen move
                            chosenMove = (currCoordinate), (leftCoordinate)
                            reverse = (leftCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            #((0,0), (1,0))
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            #0, 0, 1, 0
                            #0123456789
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            if chosenMove in self.listOfMoves:
                                if y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    y=0
                                continue
                            else:
                                #Current chosen move
                                self.listOfMoves.append(chosenMove)
                                self.listOfMoves.append(reverse)
                                #Opens file with all players moves
                                #Checks if a box was closed, if so then the player passes
                                if os.path.exists('./Megan.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Checks if a box was closed, if so then the player passes
                                elif os.path.exists('./Michael.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Megan.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Closes file until next turn
                            #Add 1 to number of edges at those nodes
                            cordEdges[self.x][y] = cordEdges[self.x][y] + 1
                            cordEdges[self.x][y-1] = cordEdges[self.x][y-1] + 1
                            prevNumEdges = numEdges
                            self.n = 0
                            if y==9:
                                self.x=self.x+1
                                previousNumEdges = 4
                                y=0
                            test = MandM()
                            break
                    
                    if self.x > 0:
                        if cordEdges[self.x-1][y] < 2:
                            #Current chosen move
                            chosenMove = (currCoordinate), (topCoordinate)
                            reverse = (topCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            #((0,0), (1,0))
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            #0, 0, 1, 0
                            #0123456789
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            if chosenMove in self.listOfMoves or reverse in self.listOfMoves:
                                if y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    y=0
                                continue
                            else:
                                #Current chosen move
                                self.listOfMoves.append(chosenMove)
                                self.listOfMoves.append(tuple(reverse))
                                #Opens file with all players moves
                                #Checks if a box was closed, if so then the player passes
                                if os.path.exists('./Megan.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Checks if a box was closed, if so then the player passes
                                elif os.path.exists('./Michael.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Megan.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Closes file until next turn
                            #Add 1 to number of edges at those nodes
                            cordEdges[self.x][y] = cordEdges[self.x][y] + 1
                            cordEdges[self.x-1][y] = cordEdges[self.x-1][y] + 1
                            prevNumEdges = numEdges
                            self.n = 0
                            if y==9:
                                self.x=self.x+1
                                previousNumEdges = 4
                                temp = self.x
                                y=0
                            test = MandM()
                            break

                    if self.x < 9:    
                        if cordEdges[self.x][y] < 2:
                            #Current chosen move
                            chosenMove = (currCoordinate), (bottomCoordinate)
                            reverse = (bottomCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            #((0,0), (1,0))
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            #0, 0, 1, 0
                            #0123456789
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            if chosenMove in self.listOfMoves or reverse in self.listOfMoves:
                                if y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    y=0
                                continue
                            else:
                                #Current chosen move
                                self.listOfMoves.append(chosenMove)
                                self.listOfMoves.append(tuple(reverse))
                                #Opens file with all players moves
                                #Checks if a box was closed, if so then the player passes
                                if os.path.exists('./Megan.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Checks if a box was closed, if so then the player passes
                                elif os.path.exists('./Michael.pass'):
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Megan.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                #Closes file until next turn
                            #Add 1 to number of edges at those nodes
                            cordEdges[self.x][y] = cordEdges[self.x][y] + 1
                            cordEdges[self.x+1][y] = cordEdges[self.x+1][y] + 1
                            prevNumEdges = numEdges
                            self.n = 0
                            if y==9:
                                self.x=self.x+1
                                previousNumEdges = 4
                                temp = self.x
                                y=0
                            test = MandM()
                            break
                    
                    #case where we don't want to go here: go back to start of nested for loop
                    else:
                        prevNumEdges = numEdges
                        if y == 9:
                            self.x = self.x+1
                            previousNumEdges = 4
                            temp = self.x
                            y=0
                #Case where box already exists here
                else:
                    if y == 9:
                        self.x = self.x+1
                        previousNumEdges = 4
                        temp = self.x
                        y=0
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