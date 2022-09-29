import random, os, time
#Introduction

def field_layout(): #Function for printing the layout by diplaying a grid in each iteration
    
    global mine_value
    global n
    
    print()
    print('A Game that starts with chance')
    print('And ends with wits!')
    print('Good luck!')
    print()

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
    
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)
    
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
            
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
        
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|")
        
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|")
        
    print()
        