#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:56:36 2021

@author: hayleywalters
"""
"""
Write a program that:
    Creates an instance of the Program class, with hardcoded rules for a Picobot program.
    Creates an instance of the empty room.
    Places a bot at a random location in the room.
    Runs the Picobot program until 100% of the spaces are visited, printing out an updated version of the room at each step.
"""

from pbot_program import Pbot_program
from pbot_rule import Pbot_rule
from pbot_room import Pbot_room
from Pbot_generation import Pbot_gen

G = 3 #the number of generations

#########################
##TEST 1: 3 x 3 room, starting at (0,0), moving downwards 1 unit
#########################
"""rule = Pbot_rule(0,"XXXX","W",0)
r1 = Pbot_room(3, 3)

for i in range(4):
    print(r1)
    print(r1.surroundings())
    print()
    r1.step(rule)
    
    """
########################
##TEST 2: 3 x 3 room, starting at (0,0), moving down until it hits the wall,
##then right until it hits the wall
########################
"""
r = Pbot_room(5,5)
p = Pbot_program()

p.randomize()

l = r.run_program(p,100, 3)

for i in l:
    print(i)"""
    

"""tests"""

def convert_pbot_to_prgm(str1):
    '''
    Takes the format that the Pbot_program returns as and turns it into something that the real picobot will accept.

    Parameters
    ----------
    str1 : str
        a string representation of the picobot program.

    Returns
    -------
    str1 : str
        a string that the real picobot can actually use as a program.

    '''
    for i in range(9*5):
        rule = str1[i*14: i*14+14]
        south = rule[4:5]
        west = rule[5:6]
        
        new_rule = list(rule)
        new_rule[5:6] = south
        new_rule[4:5] = west
        
        lstr1 = list(str1)
        lstr1[i*14: i*14+14] = new_rule
        
        str1 = "".join(lstr1)
        
    str1 = str1.replace("\n",",\n")
    
    return str1


##start of real test

#create an empty room
room = Pbot_room()
#put the picobot in a random position in the room
room.random_position()

#create a list of generations
gens = [None]

print("Generation 0")
gens[0] = Pbot_gen(room, True)
print(gens[0].fittest_program())
empty, top_fitness = gens[0].fittest_program()
i = 1
for i in range(1,15):
    print(f'Generation {i}')
    gens.append(None)
    gens[i] = gens[i-1].generate_new_gen()
    empty, top_fitness = gens[i].fittest_program()
    print(top_fitness)



final_program, empty = gens[14].fittest_program()
final_program = convert_pbot_to_prgm(str(final_program))
print(final_program)
print(f'fitness percent {empty}%')
    