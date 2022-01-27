#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:17:47 2021

@author: hayleywalters
"""
from pbot_program import Pbot_program
from pbot_room import Pbot_room
from random import randint

DEFAULT_GENERATION_SIZE = 200
TRIALS = 25
P = 0.3 #the probability that the algorithm uses mutation to generate a program
M = 20 #possible parent candidate pool
class Pbot_gen():
    
    def __init__(self, room, first_gen = False, programs=[]):
        self.room = room
        self.room_copy = room
        self.programs = programs
        
        #the minimum number of steps is 50% more than the total number of cells
        # in the room. It is 150% of the total cells.
        # When the room is 25 x 
        min_num_steps = round(room.height * room.width * (1.5))
        
        self.fitness_percents = {}
        
        if first_gen:
            self.randomize(DEFAULT_GENERATION_SIZE)
        self.__run_programs__(min_num_steps)
        print("Generation Completed")
        
        
        
    def get_candidate(self,index):
        return self.programs[index]
    
    def randomize(self, num_programs):
        for i in range(num_programs):
            x = Pbot_program([])
            x.randomize()
            self.programs.append(x)
    
    def __run_programs__(self, steps):
        '''
        Runs all the programs inside the generation, default trial number times, then takes their average percent filled cells and adds it to a list, which is returned

        Parameters
        ----------
        steps : int
            the number of steps each program will be run.

        Returns
        -------
        nothing. modifies the fitness_percents dictionary.

        '''
        #run the pbot candidates in the room
        for program in self.programs:
            fitness_sum = 0
            for i in range(TRIALS):
                r = Pbot_room(self.room.height, self.room.width)
                r.random_position()
                try:
                    r.run_program(program, steps)
                except AttributeError:
                    
                    print(program)
                    pass
                fitness_sum+=r.percent_full()
            #print(r)
            fitness = fitness_sum / TRIALS
            self.fitness_percents[program] = fitness
            self.sorted_fitness = dict(sorted(self.fitness_percents.items(), key=lambda item: item[1]))
            
    def generate_new_gen(self):
        topM = self.sorted_fitness 
        topM = list(topM.items())[DEFAULT_GENERATION_SIZE-M:]

        new_prgms = []
        for i in range(DEFAULT_GENERATION_SIZE):
            randnum = randint(0, 10)
            #if the random number is less than P*10, (which is default 3). 30% chance
            if randnum <= P*10:
                randnum2 = randint(0,M-1)
                
                prgm, empty = topM[randnum2]
                mutant_program = Pbot_program(prgm.rules)
                
                mutant_program.mutate()
                new_prgms.append(mutant_program)
            else:
                randnum2 = randint(0,M-1)
                randnum3 = randint(0,M-1)
                
                prgm1, empty = topM[randnum2]
                prgm2, empty = topM[randnum3]
                
                parent_program1 = prgm1
                parent_program2 = prgm2
                
                child_program = parent_program1.crossover(parent_program2)
                
                new_prgms.append(child_program)
                
        
        return Pbot_gen(self.room, False, new_prgms)
    
    def fittest_program(self):
        top = self.sorted_fitness 
        top = list(top.items())[-1:]
        top = top[0]
        
        
        return top
    
    def avg_fitness(self):
        dict_values = list(self.fitness_percents.values())
        return sum(dict_values)/DEFAULT_GENERATION_SIZE
    
    def __str__(self):
        dict_values = list(self.fitness_percents.values())
        l = []
        for i in range(len(dict_values)):
            l.append(f'program {i}: {dict_values[i]}%')
        l.append(f'average fitness: {sum(dict_values)/DEFAULT_GENERATION_SIZE}%')
        return str(l)
    
    
    
            

