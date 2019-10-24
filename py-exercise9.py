#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Do you want to play the Rock-Paper-Scissors game?')


while True:
    player1 = input('What do player no 1 choose: ')
    player2 = input('What do player no 2 choose: ')
    if player1 == 'rock'and player2 == 'scissors':
        print('Player1 - won!')
    elif player1 == 'scissors' and player2 == 'paper':
        print('Player1 - won!')
    else:
        #player1 == 'paper' and player2 == 'rock':
            print('Player2 - won!')


# In[ ]:




