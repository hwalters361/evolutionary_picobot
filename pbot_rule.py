#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:20:25 2021

@author: hayleywalters
"""

class Pbot_rule():
    
    def __init__(self, state1=0, surroundings= "xxxx", move="N", state2=1):
        '''
        
        Initializes a Pbot_rule() object
        
        Parameters
        ----------
        state1 : str, optional
            the initial state for the rule. The default is "0".
        surroundings : str, optional
            the surroundings. The default is "XXXX".
        move : int, optional
            the move the pbot will take. The default is "#".
        state2 : int, optional
            the next state the pbot will enter. The default is "0".

        Returns
        -------
        An instance of the class pbot_rule

        '''
        self.state1 = state1
        self.surroundings = surroundings
        self.move = move #the direction the rule tells the bot to move given the conditions of surroundings and state are met
        self.state2 = state2
        
    def __str__(self):
        return f'{self.state1} {str(self.surroundings)} -> {self.move} {self.state2}'
    def __repr__(self):
        return str(self)
    
    def initial_state(self):
        return (self.state1, self.surroundings)
    def next_state(self):
        return self.state2
    
    
    





            