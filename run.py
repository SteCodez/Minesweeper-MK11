import random
import os

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
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] +1
            if r >0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] +1
            if r > 0 and col < n -1 and numbers[r-1][col-1] == -1:
                numbers[r][col] == numbers[r][col] +1
            if r < n-1 and col > 0 and numbers[r+1][col+1]== -1:
                numbers[r][col] = numbers[r][col] +1
            if r < n-1 and col < n-1 and numbers[r+1][col+1]== -1:
                numbers[r][col] = numbers[r][col] +1
        """
        The above statements go either + or - or both in the row and column to check in a full circle
        around each grid which should in return add 1 to every cell that is touching a mine.
        """
def zero_value_check(r, col):
    
    global mine_value
    global number
    global vis
    """
    This function will check for zeros surrounding the chosen cell using a recursive function.
    """
    
    if [r, col] not in vis:
        vis.append([r, col])
        
        if numbers[r][col] == 0:
            mine_value[r][col] = numbers[r][col]
            
            
