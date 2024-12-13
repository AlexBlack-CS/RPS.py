"""
File:
Author: alex Black
Description: Rock, paper, scissors
"""


import random

# Main game loop

print('Each round you must select from one of the following weapons:')
print('Enter r for Rock')
print('Enter p for Paper')
print('Enter s for Scissors')
print('Enter q for Quit')

human_wins = 0
computer_wins = 0
ties = 0
num_rounds = 0

user_choice = input('Please enter your weapon of choice: ').lower()  # lowercase the input

while user_choice != 'q':
    computer = random.choice(['r', 'p', 's'])
    
    if user_choice == 'r':
        if computer == 'r':
            print('TIE. Both picked r')
            ties += 1
        elif computer == 'p':
            print('COMPUTER WINS! Human pick: r Computer pick: p')
            computer_wins += 1
        else:
            print('HUMAN WINS! Human pick: r Computer pick: s')
            human_wins += 1
        num_rounds += 1  

    elif user_choice == 'p':
        if computer == 'p':
            print('TIE. Both picked p')
            ties += 1
        elif computer == 'r':
            print('HUMAN WINS! Human pick: p Computer pick: r')
            human_wins += 1
        else:
            print('COMPUTER WINS! Human pick: p Computer pick: s')
            computer_wins += 1
        num_rounds += 1  

    elif user_choice == 's':
        if computer == 's':
            print('TIE. Both picked s')
            ties += 1
        elif computer == 'r':
            print('COMPUTER WINS! Human pick: s Computer pick: r')
            computer_wins += 1
        else:
            print('HUMAN WINS! Human pick: s Computer pick: p')
            human_wins += 1
        num_rounds += 1  

    else:
        print('ERROR. Thats not a valid choice.')

    user_choice = input('Please enter your weapon of choice: ').lower() 

print('Thanks for playing')
print(f'We played a total of {num_rounds} valid rounds')
print(f'Total ties = {ties}')
print(f'Total wins for human = {human_wins}')
print(f'Total wins for computer = {computer_wins}')



    
        
    
