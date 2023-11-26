import random

card_values={'K':10,'Q':10,'J':10,'A':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
suites=['D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C','D','S','H','C']
values=['A','K','Q','J','T','9','8','7','6','5','4','3','2','A','K','Q','J','T','9','8','7','6','5','4','3','2','A','K','Q','J','T','9','8','7','6','5','4','3','2','A','K','Q','J','T','9','8','7','6','5','4','3','2']
your_card=''
your_card_value=0
dealer_card_value=0
dealer_card=''
your_card+=random.choice(values)+random.choice(suites)+' '
values.remove(your_card[0])
suites.remove(your_card[1])
your_card_value+=card_values.get(your_card[0])
dealer_card+=random.choice(values)+random.choice(suites)+' '
values.remove(dealer_card[0])
suites.remove(dealer_card[1])
dealer_card_value+=card_values.get(dealer_card[0])
your_card+=random.choice(values)+random.choice(suites)+' '
values.remove(your_card[3])
suites.remove(your_card[4])
your_card_value+=card_values.get(your_card[3])
dealer_card+=random.choice(values)+random.choice(suites)+' '
values.remove(dealer_card[3])
suites.remove(dealer_card[4])
dealer_card_value+=card_values.get(dealer_card[3])
print(f'Your cards={your_card}')
print(f'Dealer cards={dealer_card[0]}{dealer_card[1]} *')

    
    
if your_card_value==21:
    print('Black jack!')
else:
            
 while your_card_value<22:
    if your_card_value==21:
        print('21!')
        print('You won!')
        break
    else:
     print('1.Hit')
     print('2.Stand')
     choose=input('Hit or Stand:')
     if choose=='1':
        temp=random.choice(values)+random.choice(suites)
        values.remove(temp[0])
        suites.remove(temp[1])
        
        your_card_value+=card_values.get(temp[0])
        your_card+=temp+' '
     elif choose=='2':
        print(f'Your cards={your_card}')
        print('Dealer turn')
        print(f'Dealer cards={dealer_card}')
        if dealer_card_value==21:
            print('Black jack!')
        else:    
            
        
               
        
         while dealer_card_value<22:
                if dealer_card_value==21 or dealer_card_value>your_card_value:
                    print('Dealer stands!')
                    print('Dealer won!')
                    break
                else:

                 if dealer_card_value in range(2,16):
                    print('Dealer hits')
                    temp=random.choice(values)+random.choice(suites)
                    values.remove(temp[0])
                    suites.remove(temp[1])
                    dealer_card_value+=card_values.get(temp[0])
                    dealer_card+=temp+' '
                 elif dealer_card_value in range(16,18):
                    choices=['1','2']
                    choose=random.choice(choices)
                    if choose=='1':
                     print('Dealer hits')
                     temp=random.choice(values)+random.choice(suites)
                     values.remove(temp[0])
                     suites.remove(temp[1])
                     dealer_card_value+=card_values.get(temp[0])
                     dealer_card+=temp+' '                        
                    else:
                     if dealer_card_value<your_card_value:
                        print('You won!')
                        break                        

                     elif dealer_card_value==your_card_value:
                        print('Tie!')
                        break
                 elif dealer_card_value in range(18,21):
                     if dealer_card_value<your_card_value:
                        print('You won!')
                        break                        

                     elif dealer_card_value==your_card_value:
                        print('Tie!')
                        break                        
                    
                 print(f'Dealer cards={dealer_card}')        
                        
         else:
                print(f'Dealer={dealer_card_value}')
                print('Dealer bust!')
                print('You won!')    
         break        
                  
     else:   
        print('Wrong command!')
     print(f'Your cards={your_card}')    
 else:
    print(f'You={your_card_value}')
    print('You bust!')    
