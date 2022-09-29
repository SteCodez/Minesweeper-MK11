import random, os
#Introduction
print()
print('A Game that starts with chance')
print('And ends with wits!')
print('Good luck!')
print()

def reset():
    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P'
''')
    
    choice = input('Type here: ').upper
    
    if choice == 'I':
        os.system('clear')
        
        print(open('instructions.txt', 'r').read())
        
        input('Press [enter] when ready to play. ')
        
    elif choice != 'p':
        os.system('clear')
        reset()