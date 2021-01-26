from random import randrange
import sys
import copy

# --------- Global Variables -----------

# When you refer to a variable in multiple functions
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Test grid: [[4, 8, 4, 8], [8, 4, 8, 4], [4, 8, 4, 8], [12, 0, 0, 0]]
# Test grid: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# ------------- Functions ---------------

def print_grid():
  lar_num_length = 0
  for list in grid:
    if len(str(max(list))) > lar_num_length: # String to use len()
      lar_num_length = len(str(max(list)))
  for row in grid:
    current_row = '|'
    for x in row:
      current_row += ' ' + (' ' * (lar_num_length - len(str(x)))) + str(x) + ' |'
    print(current_row)


def generate_a_new_number():
  # 87.5% chance of '2' and 12.5% change of '4'
  if randrange(8) != 7:
    return 2
  else:
    return 4


def place_number():
  not_empty = True # Assumption it's not empty as while it is not empty we keep the loop going
  while not_empty == True: # Finds random space
      location_x = randrange(4)
      location_y = randrange(4)
      no_zero = True
      if grid[location_x][location_y] == 0:
        grid[location_x][location_y] = generate_a_new_number()
        not_empty = False # Exit loop and function. this would loop forever even if no spaces - so we have done the for loop below.
      for row in grid: # Double check whether there is a 0 at all - safety net
        if 0 in row:
          no_zero = False
          break
      if no_zero == True: # We didn't find a 0, so exit the function
        return


def movement(direction):
  if direction == "right":
    for row in range(0, 4, 1):
      for x in range(3, 0, -1): # Inner loop executed for each iteration of the outer loop
        for column in range(x, 4, 1): # Inner loop executed for each iteration of the outer loop
          if grid[row][column] == 0:
            grid[row][column] = grid[row][column - 1]
            grid[row][column - 1] -= grid[row][column - 1]
          elif grid[row][column] == grid[row][column - 1]:
            grid[row][column] += grid[row][column - 1]
            grid[row][column - 1] -= grid[row][column - 1]
  elif direction == "up":
    for column in range(0, 4, 1):
      for x in range(0, 3, 1):
        for row in range(x, -1, -1):
          if grid[row][column] == 0:
            grid[row][column] = grid[row + 1][column]
            grid[row + 1][column] -= grid[row + 1][column]
          elif grid[row][column] == grid[row + 1][column]:
            grid[row][column] += grid[row + 1][column]
            grid[row + 1][column] -= grid[row + 1][column]
  elif direction == "left":
    for row in range(0, 4, 1):
      for x in range(0, 3, 1):
        for column in range(x, -1, -1):
          if grid[row][column] == 0:
            grid[row][column] = grid[row][column + 1]
            grid[row][column + 1] -= grid[row][column + 1]
          elif grid[row][column] == grid[row][column + 1]:
            grid[row][column] += grid[row][column + 1]
            grid[row][column + 1] -= grid[row][column + 1]
  elif direction == "down":
    for column in range(0, 4, 1):
      for x in range(3, 0, -1):
        for row in range(x, 4, 1):
          if grid[row][column] == 0:
            grid[row][column] = grid[row - 1][column]
            grid[row - 1][column] -= grid[row - 1][column]
          elif grid[row][column] == grid[row - 1][column]:
            grid[row][column] += grid[row - 1][column]
            grid[row - 1][column] -= grid[row - 1][column]


def game_over(status):
  while True: # Always True - infinite loop until we exit function
    end_keyboard_input = input("You {}. Type 'restart' to play again. Type 'exit' to exit >".format(status)).lower()
    if end_keyboard_input == 'exit':
      print("Thanks for playing 2048 - by India & Matt")
      sys.exit() 
    elif end_keyboard_input == 'restart':
      return
    else:
      print("Incorrect input please try again.")


def test_endgame(): # Testing moves on our copy grid against our main grid
  global grid
  grid_test = copy.deepcopy(grid) # Using deepcopy function to ensure both parts of the list are copied
  movement("up")
  if grid_test == grid:
    movement("down")
    if grid_test == grid:
      movement("left")
      if grid_test == grid:
        movement("right")
        if grid_test == grid:
          print("Game Over")
          return True
  grid = copy.deepcopy(grid_test)
  return False


# ------------- Main Game ---------------

def start_2048():
  print("Welcome to 2048!")
  print("Move up, left, right, down using WASD keys")
  place_number()
  place_number()
  print_grid()
  print("Press W, A, S or D to start/move; or type 'exit' to quit the program")

  while True:
    for row in grid:
      if 2048 in row: # Then do this function - which we are relying on for an output
        if game_over("win") == None:
          return # Jump to line 168
    
    place_number_test = copy.deepcopy(grid)

    keyboard_input = input('Accepting input: ').lower()
    if keyboard_input == 'exit':
      sys.exit()  
    elif keyboard_input == "w":
      movement("up")
    elif keyboard_input == "d":
      movement("right")
    elif keyboard_input == "a":
      movement("left")
    elif keyboard_input == "s":
      movement("down")
    else: 
      print("Unrecognised input, please try again (W, A, S, D or 'exit'):")  

    if grid != place_number_test: # Checks if the move was valid - e.g. if I moved down and no numbers shifted, then do not place a new number
      place_number()
    print_grid()

    if test_endgame() == True:
      if game_over("lose") == None:
        return

  
# ------------- Start the Game & Loop ---------------

while True:
  start_2048()
  grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  print("-------------------------------- \n \n")

