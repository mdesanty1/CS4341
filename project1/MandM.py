#This is a test
#from game import Game
import numpy as np
import pygame

class GroupName:
    #def __init__(self):

    #Takes in current board and last move
    #board = 9x9 of board coordinates in (x,y)
    #lastMove = (x1,y1) (x2, y2) of move made
    #listOfMoves = list of lastMove 's made
    #cordEdges = 9x9 array that tells you how many edges are attached to that specific coordinate
        #Helps AI in determining where to go (Iterative deepening heuristic that looks for coordinates with 0 or 1 edges connected)
    def decideMove(board, lastMove, listOfMoves, cordEdges):
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
        for x in range(0,8):
            for y in range(0,8):
                #check number of edges at the given coordinate
                #The first time it runs 
                if board[x][y] == (0,0):
                    prevNumEdges = cordEdges[x][y]
                    numEdges = prevNumEdges
                else:
                    numEdges = cordEdges[x][y]
                    #Check if the previous move has less edges than the current one being explored
                    #Else: run through for loop again until it does
                    #This alpha beta pruning: prunes the other options
                if(prevNumEdges < numEdges):
                    #If it does, set the current move
                    currCoordinate = board[x][y]
                    #When the algo comes to a node, check horizontal options first then vertical (MUST CHECK BOTH)
                    #case 1: can't look left
                    if x == 0:
                        leftCoordinate = board[x][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y-1]
                        bottomCoordinate = board[x][y+1]

                    #case 2: y = 0 (can't look above)
                    if y == 0:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y]
                        topCoordinate = board[x][y] 
                        bottomCoordinate = board[x][y+1]

                    #Case 3: x & y = 0 (can't look left or above)
                    if x == 0 & y == 0:
                        leftCoordinate = board[x][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y]
                        bottomCoordinate = board[x][y+1]

                    #Case 4: x = 8 (can't look right)
                    if x == 8:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y]
                        topCoordinate = board[x][y-1]
                        bottomCoordinate = board[x][y+1]

                    #Case 5: y = 8 (can't look beneath)
                    if y == 8:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y-1]
                        bottomCoordinate = board[x][y]

                    #Case 6: x & y = 8 (can't look right or beneath)
                    if x == 8 & y == 8:
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x][y]
                        topCoordinate = board[x][y-1]
                        bottomCoordinate = board[x][y]

                    #Case 7: normal case
                    else:      
                        leftCoordinate = board[x-1][y]
                        rightCoordinate = board[x+1][y] 
                        topCoordinate = board[x][y-1]
                        bottomCoordinate = board[x][y+1]

                    #Want to check if there are less than two edges at the node next to the choice
                    #Break ties: pick from left to right then up to down
                    if cordEdges.get(leftCoordinate) < 2 & x != 0:
                        #Current chosen move
                        chosenMove = (currCoordinate), (leftCoordinate)
                        #Add 1 to number of edges at those nodes
                        cordEdges.get(currCoordinate).set(cordEdges.get(currCoordinate) + 1)
                        cordEdges.get(leftCoordinate).set(cordEdges.get(leftCoordinate) + 1)
                        prevNumEdges = numEdges

                    elif cordEdges.get(rightCoordinate) < 2 & x != 8:
                        #Current chosen move
                        chosenMove = (currCoordinate), (rightCoordinate)
                        #Add 1 to number of edges at those nodes
                        cordEdges.get(currCoordinate).set(cordEdges.get(currCoordinate) + 1)
                        cordEdges.get(rightCoordinate).set(cordEdges.get(rightCoordinate) + 1)
                        prevNumEdges = numEdges

                    elif cordEdges.get(topCoordinate) < 2 & y != 0:
                        #Current chosen move
                        chosenMove = (currCoordinate), (topCoordinate)
                        #Add 1 to number of edges at those nodes
                        cordEdges.get(currCoordinate).set(cordEdges.get(currCoordinate) + 1)
                        cordEdges.get(topCoordinate).set(cordEdges.get(topCoordinate) + 1)
                        prevNumEdges = numEdges
                        
                    elif cordEdges.get(bottomCoordinate) < 2 & y != 8:
                        #Current chosen move
                        chosenMove = (currCoordinate), (bottomCoordinate)
                        #Add 1 to number of edges at those nodes
                        cordEdges.get(currCoordinate).set(cordEdges.get(currCoordinate) + 1)
                        cordEdges.get(bottomCoordinate).set(cordEdges.get(bottomCoordinate) + 1)
                        prevNumEdges = numEdges
                    
                    #case where we don't want to go here: go back to start of nested for loop
                    else:
                        prevNumEdges = numEdges
                        continue
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

        updateBoard(move)

    #Helper function used: iterative deepening
    #Want to check next move which allows us to deepen & prune at a level of 2
    #Given the first chosen move, we want to check what the next player would play
    #If the next players move 
    #def decideMove2(move):

    
    #Update board based on AI's last move
    def updateBoard(move):
        #Opens file with all players moves
        File_object = open("move_file", "w")
        #Writes in selected move from decideMove()
        File_object.write(move)
        #Closes file unti next turn
        File_object.close()