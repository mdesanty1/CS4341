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

    #Update board based on AI's last move
    def updateBoard(move):
        #File_object.write("Chosen move \n")
        #File_object.close()