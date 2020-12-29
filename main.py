
# Constant:

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Main Function

def solve(board):

	find = find_zero(board)

	if not find:
		return True
	else:
		row, col = find

	for i in range(1,10):
		if is_valid(board, i, (row, col)):
			board[row][col] = i
			
			if solve(board):
				return True
			
			board[row][col] = 0

	return False



# Find empty slot, goes right and down
# find_zero: Board -> (anyof (Int, Int) None)

def find_zero(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j) # row, col
	return None



# Checks if num at position pos(row,col) on the board is valid
#   according to constraints of Sudoku
# is_valid: Board Int (Int, Int) -> Bool

def is_valid(board, num, pos):
	
	# Row Check
	for j in range(9):
		if board[pos[0]][j] == num and pos[1] != j:
			return False

	# Column Check
	for i in range(9):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# Box Check
	x = pos[1] // 3
	y = pos[0] // 3
	for i in range(y*3, y*3 + 3):
		for j in range(x * 3, x*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False
	return True



# Custom board printing function
def prettify_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -")

		for j in range(len(board[i])):
			if j % 3 == 0 and j != 0:
				print("| ", end="")

			if j == 8:
				print(board[i][j])
			else:
				if j == 0:
					print(" " + str(board[i][j]) + " ", end="")
				else:
					print(str(board[i][j]) + " ", end="")



# ---------------------------------------------------------------
print("Given Board: ")
print("_______________________")
prettify_board(board)
print("_______________________")
print("")

solve(board)

print("Solved Board:")
print("_______________________")
prettify_board(board)
print("_______________________")
# ---------------------------------------------------------------


