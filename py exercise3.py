print('What is your favourite number?')
favNum = int(input())

if favNum > 0 and favNum % 2 == 0:
     print('Your favourite number '+str(favNum)+' is an even number.')

else:
     print('You favourite number '+str(favNum)+' is an odd number.')
