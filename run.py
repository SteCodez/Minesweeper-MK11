import random
import os

def print_mines_layout():
 
    global mine_values
    global n
 
    print()
    
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
 
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
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
            
            if r > 0:
                zero_value_check(r-1, col)
            if r < n-1:
                zero_value_check(r+1, col)
            if col > 0:
                zero_value_check(r, col-1)
            if col < n-1:
                zero_value_check(r, col+1)  
            if r > 0 and col > 0:
                zero_value_check(r-1, col-1)  
            if r > 0 and col < n-1:
                zero_value_check(r-1, col+1)
            if r < n-1 and col > 0:
                zero_value_check(r+1, col-1)
            if r < n-1 and col < n-1:
                zero_value_check(r+1, col+1)  
        if numbers[r][col] != 0:
            mine_value[r][col] = numbers[r][col]

def clear():
    os.system("clear")
    """
    this function will check the progress of the game, count all of the numbered value and and for loop
    to check each cell in the grid.
    """
def check_game_progress():
    global mine_value
    global n
    global no_of_mines
    
    count = 0
    
    for r in range(n):
        for col in range(n):
            
            if mine_value[r][col] != ' ' and  mine_value[r][col]!= 'F':
                count = count + 1
    
    if count == n * n - no_of_mines:
        return True
    else:
        return False
    """
    this funtion will display all of the mine locations, mines have been given the
    value M for Mine.
    """
def mine_displayer():
    global mine_value
    global numbers
    global n
    
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_value[r][col] = 'M'
                
if __name__ == "__main__":
    n = 8
    no_of_mines = 8
    
    numbers = [[0 for y in range(n)] for x in range(n)] 
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    flags = []
    mine_placer()
    set_values()
    over = False
    
    while not over:
        print_mines_layout()
        inp = input("Enter row number followed by space and column number = ").split()
        """
        Above: The input that enters your selections into the grid.
        Below: The try block that calls a ValueError if the input is invalid.
        """
        if len(inp) ==2:
            try:
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Invalid input, try again!")
                continue
        
        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                clear()
                print("Invalid input, try again!")
                continue
            
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Invalid input, try again!")   
                continue
            
            r = val[0]-1
            col = val