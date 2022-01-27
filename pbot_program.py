#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:22:31 2021

@author: hayleywalters
"""
from pbot_rule import Pbot_rule
from random import randint

DEFAULT_NUM_STATES = 5


class Pbot_program(object):
    
    def __init__(self, rules=[]):
        '''
        Initializes a Pbot_program object

        Parameters
        ----------
        rules : list
            A list of Pbot_rules

        Returns
        -------
        an instance of the class Pbot_program

        '''

        self.rules = rules
        
    
    def next_move(self, current_state, surroundings):
        '''
        
        finds / returns the next_move in the program given a current state / surroundings

        Parameters
        ----------
        current_state : int
            DESCRIPTION.
        surroundings : string
            a string in the style North East South West (NESW) to describe the pBot's surroundings (whether it's touching a block or not).

        Returns
        -------
        str
            string character representing the direction the picobot will move next.
        int
            integer representing the next state the picobot will enter.
        

        '''
        possible_rules = self.rules[current_state*9: current_state*9 + 10]
        for rule in possible_rules:
            rule_state, rule_surroundings = rule.initial_state()
            if (rule_state == current_state) and (surroundings == rule_surroundings):
                return (rule)
                
    
    
    def randomize(self,n=DEFAULT_NUM_STATES):
        '''
        Generates a random Pbot program for the empty room problem.
        Assumes that the Pbot is in an empty room, with only nine possible surrounding states and five
        possible moves: north, south, east, west, and rest.
        
        changes the rules to match the new randomly generated ones.
        
        Parameters
        ----------
        n : int
            the number of desired states for the program. (default value 5)
    
        '''
        rules = []
        possible_surroundings = ["Nxxx","xExx","xxSx", "xxxW","NExx","NxxW","xESx", "xxSW", "xxxx"]
        possible_moves = ["N", "E", "S", "W", "X"]
        possible_states = list(range(n))
        
        for i in possible_states:
            for j in possible_surroundings:
                #randomly selects a move and a state
                rand_move = possible_moves[randint(0,len(possible_moves)-1)]
                rand_state = randint(0,n-1)
                #creates a picobot rule based off the rule and state
                rules.append(Pbot_rule(i, j, rand_move, rand_state))
        self.rules = rules
    
    def default_rules(self,n=DEFAULT_NUM_STATES):
        '''
        Sets every rule inside of the object to the default rule. Accounts for ever possible state and surroundings.

        Parameters
        ----------
        n : TYPE, optional
            DESCRIPTION. The default is DEFAULT_NUM_STATES.

        Returns
        -------
        None.

        '''
        rules=[]
        possible_surroundings = ["Nxxx","xExx","xxSx", "xxxW","NExx","NxxW","xESx", "xxSW", "xxxx"]
        possible_states = list(range(n))
        
        for i in possible_states:
            for j in possible_surroundings:
                rules.append(Pbot_rule(i,j))
        self.rules = rules
    
    def __str__(self):
        '''
        Returns
        -------
        str1 : string
            string representation of pBot_program.
        '''
        
        str1 = ""
        for rule in self.rules:
            str1 = str1 + "\n" + str(rule)
        #starts at index 1 to remove the extra empty line at the start
        return str1[1:]
    
    def __repr__(self):
        '''
        returns the string representation of the program. 

        Returns
        -------
        str
            string containing every rule in program.

        '''
        return str(self)
    
    def mutate(self,num_states=DEFAULT_NUM_STATES):
        '''
        Selects one random rule in the program and randomly changes it to a new rule, maintaining the initial state

        Parameters
        ----------
        num_states : int, optional
            The default is DEFAULT_NUM_STATES. A way to represent the number of states in the program.

        Returns
        -------
        None.
        Modifies the object.

        '''
        length = 45
        randnum = randint(0, length-1)
        
        rand_move = ["N", "E", "S", "W", "X"][randint(0,4)]
        rand_state = randint(0,num_states-1)
        
        rand_rule = self.rules[randnum]
        
        initial_state = rand_rule.state1
        initial_surr = rand_rule.surroundings
        

        self.rules[randnum] = Pbot_rule(initial_state, initial_surr, rand_move, rand_state)
        
    def crossover(self,program,num_states=DEFAULT_NUM_STATES):
        '''
        Returns a new program that is the child of both the current object and a given Pbot_program object
        Assumes that the length of the given program and the length of the current object are the same.
        
        Parameters
        ----------
        program : Pbot_program
            A Pbot_program of identical length to the current object.
        num_states : int, optional
            The number of states in the program. The default is DEFAULT_NUM_STATES.

        Returns
        -------
        A Pbot_program object.

        '''
        possible_states = list(range(DEFAULT_NUM_STATES))
        rand_state=possible_states[randint(0,DEFAULT_NUM_STATES-1)]
        
        rules = []
        for i in range(0, rand_state*9):
            rules.append(self.rules[i])
        for i in range(rand_state*9, DEFAULT_NUM_STATES*9):
            rules.append(program.rules[i])
     
        return Pbot_program(rules)
      









