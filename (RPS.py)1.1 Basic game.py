#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:12:23 2020

@author: Nik


"""from random import choice 
evilComputer = ['Rock', 'Paper', 'Scissors']
while True:
    user = input('Rock, Paper, or Scissors?').lower()
    cpu = choice(evilComputer)
    if cpu == user:
        print('Its a tie Both you and The Evil computer said ', cpu)
    elif user == 'rock':
        if cpu == 'scissors':
            print('Evil computer says', cpu)
            print('You Win, Rock breaks Scissors')
        else:
            print('Evil computer says', cpu)
            print('You lose, Paper wraps Rock')
    elif user == 'scissors':
        if cpu == 'paper':
            print('Evil computer says', cpu)
            print('You Win, Scissors cuts Paper')
        else:
            print('Evil computer says', cpu)
            print('You lose, Rock breaks Scissors')
    elif user == 'paper':
        if cpu == 'rock':
            print('Evil computer says', cpu)
            print('You Win, Paper wraps Rock')
        else:
            print('Evil computer says', cpu)
            print('You lose, Scissors cuts Paper')
    elif user == 'q':
        break
    else:
        print('That input isnt an option')
        
        


