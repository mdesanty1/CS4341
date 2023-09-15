#This is a test
#from game import Game
import numpy as np
import pygame

class GroupName:
    #def __init__(self):

    #Takes in current board and last move
    def decideMove(board, lastMove, listOfMoves):
        #File_object = open("move", "r")
        #File_object.readline([n]) to look at opponent's last move (or look at board?)
        #self.board.get(edge) is used in game.py to see if an edge is taken or not
        #^ maybe use a for loop to check all the edges?
        #^ might need to be nested to check for all edges in a box
        #(r1, c1), (r2, c2) = selected_move
        #if we can get the edges, we can store them in an array to keep track
        #when adding r and c values to the list, add them all separately and then append
        #^ append r1 and c1 together, append r2 and c2 together
        #can then search through the list to find the individual edges)
        #myList = [1,2,2,1]
        #myList.append((1,2))
        #myList.append((2,1))
        #myList.append(((1,2), (2,1)))
        updateBoard(move)

        #Minimax algo:
        #Explore all options -> store the number of boxes each route captures
        #Starting condition: choose nearest node that does not have 2 lines branching off it
            #ideal: follow your own line
        #Once one node has 2 lines branching off it:
            #Look at array of nodes not taken from left to right
            #If the next route explored captures less than the previous ones, prune
            #Tree: start node, 8!, 7!, 6!,...
            #Use iterative deepening: only check the next move after to see if there is a better move
            #"better move" = less lines connected to that node
            #When the algo comes to a node, check horizontal options first then vertical (MUST CHECK BOTH) 
                #Add and subtract 1 to the y value
                #Handle out of bounds: if <0 or >board size
                #Check horizontal and verticals at the node first to determine best move in that moment then have the computer check what the next move would be
                #Ties: pick the first option (horizontal or vertical) in queue
            #Would need to check how many lines are connected to current node and node next to it
            #If box is closed, that player gets to go again



    #Update board based on AI's last move
    def updateBoard(move):
        #File_object.write("Chosen move \n")
        #File_object.close()