import random

user_turn = input('Your turn: ')

computer_choice = random.randint(1, 3)

#choices
if computer_choice == 1: 
    computer_turn = 'Rock'

if computer_choice == 2: 
    computer_turn = 'Paper'

if computer_choice == 3: 
    computer_turn = 'Sisscors'

print(computer_turn)

# user_turns
if user_turn == 'Rock' and computer_turn == 'Paper' : 
    print('Computer Wins!')

elif user_turn == 'Sisscors' and computer_turn == 'Rock' : 
    print('Computer Wins!')

elif user_turn == 'Paper'  and computer_turn == 'Sisscors' : 
    print('Computer Wins!')


elif user_turn == 'Rock' and computer_turn == 'Sisscors' : 
    print('User Wins!')
    
elif user_turn == 'Paper'  and computer_turn == 'Rock' : 
    print('User Wins!')

elif user_turn == 'Sisscors' and computer_turn == 'Paper' : 

    print('User Wins!')

elif user_turn == computer_turn : 

    print('Draw')

#bugs
elif user_turn == 'Gun' : 
    print('User hacks the game and WINS!')

else :
    print ('Computer Wins!')
    