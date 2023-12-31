#This is a test
#from game import Game
import numpy as np
import pygame
import os.path
import time
from os.path import exists
import sys

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
    listOfMoves = []
        #[((0,0), (0,0)), ((0,1), (0,1)), ((0,2), (0,2)), ((0,3), (0,3)), ((0,4), (0,4)), ((0,5), (0,5)), ((0,6), (0,6)), ((0,7), (0,7)), ((0,8), (0,8)), ((0,9), (0,9))],
         #          [((1,0), (1,0)), ((1,1), (1,1)), ((1,2), (1,2)), ((1,3), (1,3)), ((1,4), (1,4)), ((1,5), (1,5)), ((1,6), (1,6)), ((1,7), (1,7)), ((1,8), (1,8)), ((1,9), (1,9))],
          #         [((2,0), (2,0)), ((2,1), (2,1)), ((2,2), (2,2)), ((2,3), (2,3)), ((2,4), (2,4)), ((2,5), (2,5)), ((2,6), (2,6)), ((2,7), (2,7)), ((2,8), (2,8)), ((2,9), (2,9))],
           #        [((3,0), (3,0)), ((3,1), (3,1)), ((3,2), (3,2)), ((3,3), (3,3)), ((3,4), (3,4)), ((3,5), (3,5)), ((3,6), (3,6)), ((3,7), (3,7)), ((3,8), (3,8)), ((3,9), (3,9))],
            #       [((4,0), (4,0)), ((4,1), (4,1)), ((4,2), (4,2)), ((4,3), (4,3)), ((4,4), (4,4)), ((4,5), (4,5)), ((4,6), (4,6)), ((4,7), (4,7)), ((4,8), (4,8)), ((4,9), (4,9))],
             #      [((5,0), (5,0)), ((5,1), (5,1)), ((5,2), (5,2)), ((5,3), (5,3)), ((5,4), (5,4)), ((5,5), (5,5)), ((5,6), (5,6)), ((5,7), (5,7)), ((5,8), (5,8)), ((5,9), (5,9))],
              #     [((6,0), (6,0)), ((6,1), (6,1)), ((6,2), (6,2)), ((6,3), (6,3)), ((6,4), (6,4)), ((6,5), (6,5)), ((6,6), (6,6)), ((6,7), (6,7)), ((6,8), (6,8)), ((6,9), (6,9))],
               #    [((7,0), (7,0)), ((7,1), (7,1)), ((7,2), (7,2)), ((7,3), (7,3)), ((7,4), (7,4)), ((7,5), (7,5)), ((7,6), (7,6)), ((7,7), (7,7)), ((7,8), (7,8)), ((7,9), (7,9))],
                #   [((8,0), (8,0)), ((8,1), (8,1)), ((8,2), (8,2)), ((8,3), (8,3)), ((8,4), (8,4)), ((8,5), (8,5)), ((8,6), (8,6)), ((8,7), (8,7)), ((8,8), (8,8)), ((8,9), (8,9))],
                 #  [((9,0), (9,0)), ((9,1), (9,1)), ((9,2), (9,2)), ((9,3), (9,3)), ((9,4), (9,4)), ((9,5), (9,5)), ((9,6), (9,6)), ((9,7), (9,7)), ((9,8), (9,8)), ((9,9), (9,9))]]
    x = 0
    c = 0
    r = 0
    y = 0
    #initialize a current move variable for checking if boxes are taken
    currentMove = ((0,0), (0,0))

    def __init__(self):
        sys.setrecursionlimit(10000)
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

        #If not the end of the game, wait for go files
        while(os.path.exists('./end_game.py' == False)):
            #if a go file exists OR a pass file (because we want the player to go through the same process)
            if os.path.exists('./Megan.go') or os.path.exists('./Michael.go'):
                #set n to 1 saying that the go file or pass file exists
                #First check if an end game file exists
                if os.path.exists('./end_game.py'):
                    #Display the end result of the game -> read the file because it has the end result of the game
                    #setting n = 1 should break out of while loop
                    File_object = open("end_game.py", "r")
                    File_object.read()
                    self.r = 10
                    self.c = 10
                #If not the end of the game 
                    #check to see if there are any boxes to close
                    #if there are no boxes to close, run the decideMove function
                    #if there are boxes to close, write that move to the file and set n = 0 to re-loop
                else:
                    #Loop to check if there are any boxes to close
                    while self.r <= 9:
                        for self.c in range(0,10):
                            #set coordinates to reference when determining if we can close a box
                            currCoordinate = self.board[self.c][self.r]
                            if self.c > 0 and self.r > 0:
                                topLeftCoordinate = self.board[self.c-1][self.r-1]
                            if self.c < 9 and self.r > 0:
                                topRightCoordinate = self.board[self.c+1][self.r-1]
                            if self.c > 0 and self.r < 9:
                                bottomLeftCoordinate = self.board[self.c-1][self.r+1]
                            if self.c < 9 and self.r < 9:
                                bottomRightCoordinate = self.board[self.c+1][self.r+1]
                            if self.c > 0:
                                leftCoordinate = self.board[self.c-1][self.r]
                            if self.c < 9:
                                rightCoordinate = self.board[self.c+1][self.r]
                            if self.r > 0:
                                topCoordinate = self.board[self.c][self.r-1]
                            if self.r < 9:
                                bottomCoordinate = self.board[self.c][self.r+1]
                            #start at (0,0)
                            #if r = 0 & c = 0, check bottom right (Q4)
                            if self.r == 0 and self.c == 0:
                                #bottom right (1)
                                if ((rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) not in self.listOfMoves):
                                    self.currentMove = (currCoordinate, rightCoordinate)
                                    reverse = (rightCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom right (2)
                                elif ((rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                            #if r = 9 & c = 9, check top left box (Q2)
                            elif self.r == 9 and self.c == 9:
                                #top left (1)
                                if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (leftCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close rigt of box
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #top left (2)
                                elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, leftCoordinate) not in self.listOfMoves):
                                    #close bottom of box
                                    self.currentMove = (leftCoordinate, currCoordinate)
                                    reverse = (currCoordinate, leftCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1

                            #if r = 0 & c > 0, check bottom left and bottom right
                            elif self.r == 0 and self.c > 0 and self.c < 9:
                            #checking left
                                #bottom left (1)
                                if((currCoordinate, leftCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (bottomLeftCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, bottomLeftCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #bottom left (2)
                                elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close right line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                            #checking right
                                #bottom right (1)
                                elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomRightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomCoordinate, bottomRightCoordinate)
                                    reverse = (bottomRightCoordinate, bottomCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #bottom right (2)
                                elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    

                            #if c = 0 & r > 0, check top right and bottom right
                            elif self.c == 0 and self.r > 0 and self.r < 9:
                                #top right (1)
                                if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #top right (2)
                                elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (currCoordinate, rightCoordinate)
                                    reverse = (rightCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #bottom right (1)
                                elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomRightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomCoordinate, bottomRightCoordinate)
                                    reverse = (bottomRightCoordinate, bottomCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #bottom right (2)
                                elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                
                            #if r = 9 & c > 0, check top right and top left
                            elif self.r == 9 and self.c > 0 and self.c < 9:
                                #top right (1)
                                if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #top right (2)
                                elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (currCoordinate, rightCoordinate)
                                    reverse = (rightCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #top left (1)
                                if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (leftCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close right of box
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #top left (2)
                                elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, leftCoordinate) not in self.listOfMoves):
                                    #close bottom of box
                                    self.currentMove = (leftCoordinate, currCoordinate)
                                    reverse = (currCoordinate, leftCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    

                            #if c = 9 & r > 0, check top and bottom left
                            elif self.c == 9 and self.r > 0 and self.r < 9:
                                #top left (1)
                                if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (leftCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close rigt of box
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #top left (2)
                                elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, leftCoordinate) not in self.listOfMoves):
                                    #close bottom of box
                                    self.currentMove = (leftCoordinate, currCoordinate)
                                    reverse = (currCoordinate, leftCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom left (1)
                                if((currCoordinate, leftCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (bottomLeftCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, bottomLeftCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom left (2)
                                elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close right line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1

                            #if c = 9 & r = 0, check bottom left
                            elif self.c == 9 and self.r == 0:
                                #bottom left (1)
                                if((currCoordinate, leftCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (bottomLeftCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, bottomLeftCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom left (2)
                                elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close right line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    # if self.c == 9:
                                    #     self.r = self.r+1

                            #if r = 9 & c = 0, check top right
                            elif self.r == 9 and self.c == 0:
                                #top right (1)
                                if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                #top right (2)
                                elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (currCoordinate, rightCoordinate)
                                    reverse = (rightCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                    
                                

                            #check all quadrants
                            elif self.r > 0 and  self.r < 9 and self.c > 0 and  self.c < 9:
                                #top right (1)
                                if ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #top right (2)
                                elif ((rightCoordinate, topRightCoordinate) in self.listOfMoves
                                and (topCoordinate, topRightCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) in self.listOfMoves
                                and (currCoordinate, rightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (currCoordinate, rightCoordinate)
                                    reverse = (rightCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #top left (1)
                                if ((topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (leftCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, topCoordinate) not in self.listOfMoves):
                                    #close rigt of box
                                    self.currentMove = (currCoordinate, topCoordinate)
                                    reverse = (topCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #top left (2)
                                elif ((currCoordinate, topCoordinate) in self.listOfMoves
                                and (topLeftCoordinate, topCoordinate) in self.listOfMoves
                                and (leftCoordinate, topLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, leftCoordinate) not in self.listOfMoves):
                                    #close bottom of box
                                    self.currentMove = (leftCoordinate, currCoordinate)
                                    reverse = (currCoordinate, leftCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom left (1)
                                if((currCoordinate, leftCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (bottomLeftCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomLeftCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, bottomLeftCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom left (2)
                                elif((leftCoordinate, currCoordinate) in self.listOfMoves
                                and (leftCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomLeftCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close right line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom right (1)
                                elif((rightCoordinate, currCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomCoordinate, bottomRightCoordinate) not in self.listOfMoves):
                                    #close bottom line
                                    self.currentMove = (bottomCoordinate, bottomRightCoordinate)
                                    reverse = (bottomRightCoordinate, bottomCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1
                                #bottom right (2)
                                elif((currCoordinate, rightCoordinate) in self.listOfMoves
                                and (rightCoordinate, bottomRightCoordinate) in self.listOfMoves
                                and (bottomRightCoordinate, bottomCoordinate) in self.listOfMoves
                                and (currCoordinate, bottomCoordinate) not in self.listOfMoves):
                                    #close left line
                                    self.currentMove = (currCoordinate, bottomCoordinate)
                                    reverse = (bottomCoordinate, currCoordinate)
                                    #TEST
                                    # if self.c == 9:
                                    #     self.r = self.r+1

                            if self.c == 9 and self.r != 9:
                                self.r = self.r+1
                            #end of board (doesn't necessarily mean end of game)
                            #if at end of board, want to re-run program
                            if currCoordinate == (9,9):
                                self.r = self.r+1                                                                    
                    #if the currentMove has changed, a box has been located
                    #write that move to the file using corresponding players name
                    if self.currentMove != ((0,0), (0,0)) and os.path.exists('./Megan.go'):
                                #If the current move or reverse is in list of moves, then reset rows and columns back to zero and run decide move fxn
                                if self.currentMove in self.listOfMoves or reverse in self.listOfMoves:
                                    print("box is already closed")
                                    self.r = 0
                                    self.c = 0
                                    self.decideMove(self.board, self.cordEdges)
                                else:
                                    chosenMoveStr = str(self.currentMove)
                                    chosenMoveNoP = chosenMoveStr.replace("(","")
                                    chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                                    chosenMoveFirst = chosenMoveNoP2[0:3]
                                    chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                                    chosenMoveSpace = chosenMoveNoP2[3:5]
                                    chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                                    chosenMoveSecond = chosenMoveNoP2[5:10]
                                    chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                                    chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                                    #append current move
                                    time.sleep(.1)
                                    print(chosenMoveReal)
                                    self.listOfMoves.append(self.currentMove)
                                    self.listOfMoves.append(reverse)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    self.r = 0
                                    self.c = 0
                                    time.sleep(.1)
                    #If the current move isn't the top left corner and the go file exists
                    elif self.currentMove != ((0,0), (0,0)) and os.path.exists('./Michael.go'):
                                if self.currentMove in self.listOfMoves or reverse in self.listOfMoves:
                                    print("box is already closed")
                                    self.r = 0
                                    self.c = 0
                                    self.decideMove(self.board, self.cordEdges)
                                else:
                                    chosenMoveStr = str(self.currentMove)
                                    chosenMoveNoP = chosenMoveStr.replace("(","")
                                    chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                                    chosenMoveFirst = chosenMoveNoP2[0:3]
                                    chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                                    chosenMoveSpace = chosenMoveNoP2[3:5]
                                    chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                                    chosenMoveSecond = chosenMoveNoP2[5:10]
                                    chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                                    chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                                    time.sleep(.1)
                                    print(chosenMoveReal)
                                    self.listOfMoves.append(self.currentMove)
                                    self.listOfMoves.append(reverse)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    self.r = 0
                                    self.c = 0
                                    time.sleep(.1)
                    #case where the move hasn't changed -> go into the decide move function
                    else:
                        print("there are no boxes to close")
                        self.r = 0
                        self.c = 0
                        self.decideMove(self.board, self.cordEdges)
            elif os.path.exists('./Michael.pass'):
                time.sleep(.1)
                File_object = open("move_file", "w")
                File_object.write("Michael 0,0 0,0")
                File_object.close()
                time.sleep(.1)
            elif os.path.exists('./Megan.pass'):
                time.sleep(.1)
                File_object = open("move_file", "w")
                File_object.write("Megan 0,0 0,0")
                File_object.close()
                time.sleep(.1)
            else:
                continue
            time.sleep(.1)
        #else:
                #print("you are in else statement")
                #First check if an end game file exists
                #if os.path.exists('./end_game.py'):
                    #Display the end result of the game -> read the file because it has the end result of the game
                    #File_object = open("end_game.py", "r")
                    #File_object.read()
                    #self.r = 10
                    #self.c = 10
                #Only runs on the first turn and there is nothing in the move file
                #elif os.stat("move_file").st_size == 0:
                    #self.decideMove(self.board, self.cordEdges)
                #If not the end of the game
                #else:
                    #Read the opponents move from move_file
                    #File_object = open("move_file", "r")
                    #File_object.read()
                    #self.decideMove(self.board, self.cordEdges)    

    #Takes in current board and last move
    #listOfMoves = list of lastMove 's made
    #Helps AI in determining where to go (Iterative deepening heuristic that looks for coordinates with 0 or 1 edges connected)
    def decideMove(self, board, cordEdges):

        #Minimax algo:
        #Explore all options -> store the number of boxes each route captures
        #Start checking the board from left to right, starting at row 0, then row 1, etc
        
        #while column is on the board
        while self.x <= 9:
            #while row is on the board
            for self.y in range(0,10):
                if os.path.exists('./end_game.py'):
                    #Display the end result of the game -> read the file because it has the end result of the game
                    #setting n = 1 should break out of while loop
                    File_object = open("end_game.py", "r")
                    File_object.read()
                #Check to see if a box can be closed before anything else
                #Check edges around the point (in a 3x3 grid) to see if the edges are taken
                #Check left then right then up then down
                #check number of edges at the given coordinate
                #The first time it runs

                #Starting case when at top left corner
                #If it's the first time running through, there shouldn't be any cord edges
                if board[self.x][self.y] == (0,0) and cordEdges[0][0] == 0:
                    #set to max previous number of edges
                    prevNumEdges = 4
                    numEdges = 0
                #if at top left corner and there is one edge connecting 
                #this means there is only one way the edges can connect
                elif board[self.x][self.y] == (0,0) and cordEdges[0][0] == 1:
                    prevNumEdges = 4
                    numEdges = 0
                #if at top left corner and there's at least two edges connecting to that point
                elif board[self.x][self.y] == (0,0) and cordEdges[0][0] >= 2:
                    prevNumEdges = cordEdges[0][0]
                    numEdges = cordEdges[1][0]
                #elif self.x == 0 and not y == 0:
                    #prevNumEdges = cordEdges[9][y-1]
                    #numEdges = cordEdges[self.x][y]
                #elif y == 0 and not self.x== 0:
                    #prevNumEdges = cordEdges[self.x-1][9]
                    #numEdges = cordEdges[self.x][y]
                #If not at start coordinate
                else:
                    numEdges = cordEdges[self.x][self.y]
                #Check if current number of edges is less than the previous
                #Else: run through for loop again until it does
                #This alpha beta pruning: prunes the other options
                if(prevNumEdges > numEdges):
                    #If it does, set the current move
                    currCoordinate = board[self.x][self.y]                    
                    #Case 1: x & y = 0 (can't look left or above)
                    if self.x == 0 and self.y == 0:
                        leftCoordinate = board[self.x][self.y]
                        rightCoordinate = board[self.x][self.y+1] 
                        topCoordinate = board[self.x][self.y]
                        bottomCoordinate = board[self.x+1][self.y]
                    
                    elif self.x == 0 and self.y == 9:
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y]
                        topCoordinate = board[self.x][self.y] 
                        bottomCoordinate = board[self.x+1][self.y]

                    elif self.x == 9 and self.y==0:
                        leftCoordinate = board[self.x][self.y]
                        rightCoordinate = board[self.x][self.y+1] 
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x][self.y]
                    
                    #case 2: can't look left
                    elif self.y == 0:
                        leftCoordinate = board[self.x][self.y]
                        rightCoordinate = board[self.x][self.y+1] 
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x+1][self.y]

                    #case 3: y = 0 (can't look above)
                    elif self.x == 0:
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y+1]
                        topCoordinate = board[self.x][self.y] 
                        bottomCoordinate = board[self.x+1][self.y]

                    #Case 4: x & y = 9 (can't look right or beneath)
                    elif self.x == 9 and self.y == 9:
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y]
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x][self.y]

                    #Case 5: x = 9 (can't look right)
                    elif self.y == 9:
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y]
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x+1][self.y]

                    #Case 6: y = 9 (can't look beneath)
                    elif self.x == 9:
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y+1] 
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x][self.y]

                    #Case 7: normal case
                    else:      
                        leftCoordinate = board[self.x][self.y-1]
                        rightCoordinate = board[self.x][self.y+1] 
                        topCoordinate = board[self.x-1][self.y]
                        bottomCoordinate = board[self.x+1][self.y]
                    #if columns less than 9, make a horizontal right move
                    if self.y < 9:
                        #see if number of edges is less than 2
                        if cordEdges[self.x][self.y+1] < 4 and ((currCoordinate), (rightCoordinate)) not in self.listOfMoves:
                            #if less than 2, good to go here
                            chosenMove = (currCoordinate), (rightCoordinate)
                            reverse = (rightCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            #Want to check the reverse as well since we are looking at edges
                            if chosenMove in self.listOfMoves or reverse in self.listOfMoves:
                                if self.y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                continue
                            #case where the chosen move or the reverse are not in the list of moves
                            else:                                
                                #If pass file exists, send message to signal the player is passing
                                if os.path.exists('./Megan.pass'):
                                    time.sleep(.1)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #If a pass file exists, send message to signal the player is passing
                                elif os.path.exists('./Michael.pass'):
                                    time.sleep(.1)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael 0,0 0,0")
                                    File_object.close()
                                    time.sleep(.1)
                                #If go file exists, write to move file
                                elif os.path.exists('./Megan.go'):
                                    time.sleep(.1)
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x][self.y+1] = cordEdges[self.x][self.y+1] + 1
                                    prevNumEdges = numEdges
                                    #If go file exists, write to move file
                                elif os.path.exists('./Michael.go'):
                                    time.sleep(.1)
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x][self.y+1] = cordEdges[self.x][self.y+1] + 1
                                    prevNumEdges = numEdges
                                if self.y==9:
                                    self.x=self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                self.n = 0
                                #If at last column, increment row by 1
                                
                                test = MandM()
                                break

                    #Want to check if there are less than two edges at the node next to the choice
                    #Break ties: pick from left to right then up to down
                    #If columns are greater than zero
                    if self.y > 0:
                        #If there are less than two edges at that coordinate, make horizontal left move
                        if cordEdges[self.x][self.y-1] < 4 and ((currCoordinate), (leftCoordinate)) not in self.listOfMoves:
                            #Current chosen move
                            chosenMove = (currCoordinate), (leftCoordinate)
                            reverse = (leftCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            #If the chosen move is in the list of moves
                            if chosenMove in self.listOfMoves:
                                #If at last column, increment rows by 1 and reset columns to zero
                                if self.y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                #If the last vertical is in the list of moves, reset everything
                                if (((8,9), (9,9)) in self.listOfMoves
                                    or ((9,8), (9,9)) in self.listOfMoves):
                                    self.y = 0
                                    self.x = 0
                                continue
                            else:
                                #Current chosen move
                                
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
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x][self.y-1] = cordEdges[self.x][self.y-1] + 1
                                    prevNumEdges = numEdges
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    print(chosenMoveReal)
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x][self.y-1] = cordEdges[self.x][self.y-1] + 1
                                    prevNumEdges = numEdges
                                if self.y==9:
                                    self.x=self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                #Closes file until next turn
                            
                            
                            test = MandM()
                            break
                    
                    if self.x > 0:
                        if cordEdges[self.x-1][self.y] < 4 and ((currCoordinate), (topCoordinate)) not in self.listOfMoves:
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
                                if self.y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                continue
                            else:
                                #Current chosen move
                                
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
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x-1][self.y] = cordEdges[self.x-1][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    prevNumEdges = numEdges
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x-1][self.y] = cordEdges[self.x-1][self.y] + 1
                                    prevNumEdges = numEdges
                                if self.y==9:
                                    self.x=self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                #Closes file until next turn
                            
                            self.n = 0
                            
                            test = MandM()
                            break

                    if self.x < 9:    
                        if cordEdges[self.x+1][self.y] < 4 and ((currCoordinate), (bottomCoordinate)) not in self.listOfMoves:
                            #Current chosen move
                            chosenMove = (currCoordinate), (bottomCoordinate)
                            reverse = (bottomCoordinate), (currCoordinate)
                            chosenMoveStr = str(chosenMove)
                            chosenMoveNoP = chosenMoveStr.replace("(","")
                            chosenMoveNoP2 = chosenMoveNoP.replace(")","")
                            chosenMoveFirst = chosenMoveNoP2[0:3]
                            chosenMoveFirstFixed = chosenMoveFirst.replace(" ","")
                            chosenMoveSpace = chosenMoveNoP2[3:5]
                            chosenMoveSpaceFixed = chosenMoveSpace.replace(","," ")
                            chosenMoveSecond = chosenMoveNoP2[5:10]
                            chosenMoveSecondFixed = chosenMoveSecond.replace(" ","")
                            chosenMoveReal = chosenMoveFirstFixed + chosenMoveSpaceFixed + chosenMoveSecondFixed
                            if chosenMove in self.listOfMoves or reverse in self.listOfMoves:
                                if self.y == 9:
                                    self.x = self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                continue
                            else:
                                #Current chosen move
                 
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
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Megan " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x+1][self.y] = cordEdges[self.x+1][self.y] + 1
                                    prevNumEdges = numEdges
                                #Writes in selected move from decideMove() if it is player's turn
                                elif os.path.exists('./Michael.go'):
                                    self.listOfMoves.append(chosenMove)
                                    self.listOfMoves.append(reverse)
                                    print(chosenMoveReal)
                                    File_object = open("move_file", "w")
                                    File_object.write("Michael " +chosenMoveReal)
                                    File_object.close()
                                    time.sleep(.1)
                                    #Add 1 to number of edges at those nodes
                                    cordEdges[self.x][self.y] = cordEdges[self.x][self.y] + 1
                                    #add an edge to the neighboring coordinate
                                    cordEdges[self.x+1][self.y] = cordEdges[self.x+1][self.y] + 1
                                    prevNumEdges = numEdges
                                if self.y==9:
                                    self.x=self.x+1
                                    previousNumEdges = 4
                                    temp = self.x
                                    self.y=0
                                #Closes file until next turn
                            #Add 1 to number of edges at those nodes
                            
                            self.n = 0
                            
                            test = MandM()
                            break
                    
                    #case where we don't want to go here: go back to start of nested for loop
                    else:
                        prevNumEdges = numEdges
                        if self.y == 9:
                            self.x = self.x+1
                            previousNumEdges = 4
                            temp = self.x
                            self.y=0
                #Case where box already exists here
                else:
                    if self.y == 9:
                        self.x = self.x+1
                        previousNumEdges = 4
                        temp = self.x
                        self.y=0
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