import random, os, time
from typing import no_type_check_decorator
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

def field_layout(): #Function for printing the layout by diplaying a grid in each iteration
    
    global mine_value
    global n
    
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
            st = st + "|  " + str(mine_value[r][col]) + "  "
        print(st + "|")
        
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_value[r][col]) + "  "
        print(st + "|")
        
    print()

def mine_placer():
    
    global no_of_mines
    global n
    global numbers
    """
    This function will track the number of mines already set up,
    take a random number from all of the grid positions while generating a row and column
    and place a mine if it doesn't already have one. this sould repeat until we have the required
    number of mines.
    """
    count = 0
    while count < no_of_mines:
        val = random.randint(0, n*n-1)
        r = val // n
        col = val % n
        
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col]
            
def set_values():
    
    global n
    global numbers 
    """
    below we will ad a for loop that will count each cell value and the if statements that will skip
    through each mine if one is present
    """
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                continue

            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            if r < n-1 and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] +1
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] +1