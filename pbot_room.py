#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:02:14 2021

@author: hayleywalters
"""

DEFAULT_HEIGHT = 25 #number of rows (0 indexed. this is actually 4)
DEFAULT_WIDTH = 25 #number of columns (0 indexed this is actually 4)
INITIAL_STATE = 0


class Pbot_room:
    
    def __init__(self, height = DEFAULT_HEIGHT, width = DEFAULT_WIDTH, position = (0,0)):
        '''
        Initializes Pbot_room object

        Parameters
        ----------
        height : int, optional
            The height, number of rows, of the room. The default is DEFAULT_HEIGHT.
        width : int, optional
            The width, number of cols, of the room. The default is DEFAULT_WIDTH.
        position : tuple, optional
            the coordinates of the bot. The default is (0,0).
            the coordinates are zero indexed. The max will be (width-1, height-1)
        
        Returns
        -------
        an object of class Pbot_room, with the table of cells and pbot location.

        '''
        
        
        self.height = height
        self.width = width
        self.position = position
        self.state = 0
        self.cells = []
        self.state = INITIAL_STATE

        for i in range(self.height):
            self.cells.append([])
            for j in range(self.width):
                pos = (i, j)

                if pos == position:
                    self.cells[i].append("X")
                else:
                    self.cells[i].append(" ")
        
        self.full_cells = 1
        
    def valid_coord(self, row, col):
        '''
        Checks if given coordinate exists in the room. 

        Parameters
        ----------
        row : int
            0 indexed num for row.
        col : int
            0 indexed num for col.

        Returns
        -------
        bool
            True if the coord exists in the room. False if it doesn't.

        '''
        max_row = self.height-1
        max_col = self.width-1
        old_r, old_c = self.position
        if max_row < row or max_col < col or row < 0 or col < 0:
            return False
        else:
            return True
        
    def percent_full(self):
        '''
        gets the percent of cells that are filled

        Returns
        -------
        int
            integer representing the percent.

        '''
        return (str(self.cells).count("▒") + 1)/ (self.height * self.width) * 100
    
    def change_position(self, row, col):
        '''
        Changes the bot's position in the room

        Parameters
        ----------
        row : int
            DESCRIPTION.
        col : int
            DESCRIPTION.

        Raises
        ------
        IndexError
            If coordiante doesn't exist in the room, index error is raised.

        Returns
        -------
        None.

        '''
        old_r, old_c = self.position
        
        if self.valid_coord(row, col):
            
            self.position = (row, col)
            #replace the old spot with a blank space
            self.cells[old_r][old_c] = " "
            #replaces the new spot with a picobot symbol
            self.cells[row][col] = "X"
        else:
            raise IndexError
        
    def random_position(self):
        from random import randint
        rand_row = randint(0,self.height-1)
        rand_col = randint(0,self.width-1)
        
        self.change_position(rand_row,rand_col)
    
    def surroundings(self):
        '''
        
        Finds / returns the surroundings of the bot in the style NESW
        
        Returns
        -------
        surr : str
            string describing the surroundings of the bot in the style NESW.
            north east south west

        '''
        r, c = self.position
        surr = ""
        #north
        surr = surr + "x" if self.valid_coord(r-1, c) else surr + "N"
        #east
        surr = surr + "x" if self.valid_coord(r, c+1) else surr + "E"
        #south
        surr = surr + "x" if self.valid_coord(r+1, c) else surr + "S"
        #west
        surr = surr + "x" if self.valid_coord(r, c-1) else surr + "W"
        
        return surr
        
        
    def step(self, rule):
        '''
        Moves the bot forward one step according to a given rule

        Parameters
        ----------
        rule : Pbot_rule
            changes the location of the pbot in the room according to a pbot rule.

        Returns
        -------
        Boolean.
        Changes Pbot_room method and if the program breaks, it returns false

        '''

        r, c = self.position
        coord = (r, c)
        #finds the new coordinate the picobot will enter if it moves in any of the directions

        if rule.move == 'S':
            coord = (r+1, c)
        elif rule.move == 'N':
            coord = (r-1, c)
        elif rule.move == 'W':
            coord = (r, c+1)
        elif rule.move == 'E':
            coord = (r, c-1)
        
            
        
        
        #checks to see if picobot can move into the new coordinate. If it can't it won't move.
        new_r, new_c = coord
        if self.valid_coord(new_r, new_c) and rule.move != 'X':
            #set the current state to the new state described in the rule
            self.state = rule.next_state()
            #changes the position of the bot. 
            self.change_position(new_r, new_c)
            self.cells[new_r][new_c] = "X"
            self.cells[r][c] = "▒"
            return True
        else:
            return False
            

    
    def run_program(self, program, steps, printnum=0):
        '''
        takes a Pbot_program and runs it inside the Pbot_room. Does not go to completion, but rather the number of specified steps.
        returns a report detailing each step (depending on the value of printnum)

        Parameters
        ----------
        program : Pbot_program
            inputted program: assumes that for every state there is a rule for every possible surrounding
            for the empty room problem, that means 9 rules for each state.
        steps : int
            The number of times pbot will take a step.
        printnum : int, optional
            determines how many steps at the beginning and end of the program are recorded into the record string. The default is 5.

        Returns
        -------
        report : list
            a list of steps taken during the runtime of the program, including current state and surroundings. printnum number of moves at the beginning of the program and printnum number of moves at the end are recorded.
        

        '''
        l = []
        for i in range(steps):  
            surroundings = self.surroundings()
        
            state = self.state
        
            move = program.next_move(state, surroundings)
            if self.step(move):
                if i >= steps-printnum or i <= printnum:
                    l.append(f'step {i+1}:\nsurroundings: {surroundings} | state: {state} | next rule: {move}\n{self}\n')
                else:
                    pass
            else:
                break
        l.append(f'{self.percent_full()}% complete\n')
        if self.percent_full() == 100:
            l.append("success!")
        return l
    
    def __repr__(self):
        '''
        represents the object room as a string.

        Returns
        -------
        string : str
            string representing the room.

        '''
        string="++"
        string = string + "+"*self.width+"\n+"
        for i in self.cells:
            for j in i:
                string = string + j
            string = string+"+\n+"
        string = string + "+"+"+"*self.width
        return string
    

