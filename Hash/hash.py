def pb(b):
	for i in range(3):
		print(b[i])

def cond(t):
	return True if r(t) or c(t) or acr(t) else False
	
def r(t):
	for i in range(3):
		if t[i][0] == t[i][1] == t[i][2] and t[i][0] != ".":
			return True
	return False

def c(t):
	for i in range(3):
		if t[0][i] == t[1][i] == t[2][i] and t[0][i] != ".":
			return True
	return False

	
def acr(t):
	if t[0][0] == t[1][1] == t[2][2] or t[0][2] == t[1][1] == t[2][0]:
		if t[1][1] == ".":
			return False
		return True
	return False

fim = False
turn = "o"
print("Numbers must be between 1 and 3, format \"n1 n2\" \n")
board = [["." for i in range(3)] for j in range(3)]
pb(board)

def inbet(a):
    if a < 3 and a > 0:
        return True
    return False
        
while fim == False:
    turn = "x" if turn == "o" else "o"
    while True:
        print("Enter position of " + turn + ":")
        a = str(input())
        x = int(a[0])-1
        y = int(a[2])-1
        if not inbet(x) and not inbet(y):
            print("invalid number")
        if board[x][y] == ".":
            break
        else:
            print("invalid position")
    board[x][y] = turn
    pb(board)
    fim = cond(board)

