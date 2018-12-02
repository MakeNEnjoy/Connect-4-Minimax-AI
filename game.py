import numpy as np
import random

height = 6
width = 7

gameState = np.zeros((height, width))

def grav(gameState, move, team):
	counter = 0
	for row in range(height):
		counter += abs(gameState[row, move])
	gameState[height - int(counter) - 1, move] = team
	return gameState

def get_legal_moves(gameState):
	row = gameState[0]
	moves = list()
	for i in range(len(row)):
		if(row[i] == 0):
			moves.append(i)
	return moves

def count_row(gameState, length, team):
	n = 0
	for y in gameState:
		for x in range(len(y)):
			test = y[x:x + length]
			if(sum(test * team) == length):
				n += 1
	return n
			
def count_col(gameState, length, team):
	n = 0
	for x in gameState.T:
		for y in range(len(x)):
			test = x[y:y + length]
			if(sum(test * team) == length):
				n += 1
	return n

def count_dig_left(gameState, length, team):
	n = 0
	for dig in range(-height+1,width-1):
		diag = gameState.diagonal(dig)
		for x in range(len(diag)):
			test = diag[x:x + length]
			if(sum(test * team) == length):
				n+=1
	return n

def count_dig_right(state, length, team):
	gameState = np.fliplr(state)
	n = 0
	for dig in range(-height+1,width-1):
		diag = gameState.diagonal(dig)
		for x in range(len(diag)):
			test = diag[x:x + length]
			if(sum(test * team) == length):
				n+=1
	return n

def count_all(gameState, length, team):
	count = 0
	count += count_row(gameState, length, team)
	count += count_col(gameState, length, team)
	count += count_dig_left(gameState, length, team)
	count += count_dig_right(gameState, length, team)
	return count


def who_solo_win(gameState):
	if(count_all(gameState, 4, 1) > 0):
		return 1
	elif(count_all(gameState, 4, -1) > 0):
		return -1
	else:
		return 0

def who_win(gameState):
	if(count_all(gameState, 4, 1) > 0):
		return 100
	elif(count_all(gameState, 4, -1) > 0):
		return -100
	else:
		return count_all(gameState, 3, 1) - count_all(gameState, 3, -1) # Implement VIKTOR in here

class node:
	def __init__(self, gameState, depth):
		self.gameState = gameState
		self.depth = depth
		self.moves = []  # {'index':2, 'move':3}

def make_move(gameState):
	max_depth = 6
	possible_teams = [-1,1]

	start = node(gameState, 1)
	queue = [start]
	network = [start]
	while queue:
		curr = queue[0]
		moves = get_legal_moves(curr.gameState)
		for move in moves:
			state = grav(curr.gameState.copy(), move, possible_teams[curr.depth%2])
			new_node = node(state, curr.depth+1)
			network.append(new_node)
			curr.moves.append({'index':len(network)-1, 'move':move})
			if(new_node.depth < max_depth and who_solo_win(state) == 0):
				queue.append(new_node)




		del queue[0]
	
	for move in reversed(network):
		move.eval = who_win(move.gameState)
		if(move.eval != 100 and move.eval != -100 and move.depth < max_depth):
			if(move.depth == 1):
				print('test')
			best_move = None
			best_eval = None
			for connection in move.moves:
				#if(network[connection['index']].depth == 2):
				#	print('lol')
				if(best_move is not None):

					if(network[connection['index']].eval * 
					possible_teams[move.depth % 2] / move.depth
                    > best_eval * possible_teams[move.depth % 2]):

						best_move = connection['move']
						best_eval = network[connection['index']].eval
				else:
					best_move = connection['move']
					best_eval = network[connection['index']].eval / move.depth
			move.eval = best_eval
	move = random.choice(get_legal_moves(gameState))
	if(network[move + 1].eval == best_eval):
		return move
	else:
		return best_move

def is_problem(potential_problem, team):
	if(team*-1 in potential_problem)

def get_problems(gameState, team): # Problems are potential threats from opponent. So if team = 1 then it will find potential threats for team = -1
	








for turn in range(42):
	move = input("Please enter your move: ")
	grav(gameState, int(move), 1)

	if(who_solo_win(gameState) != 0):
		break


	move = make_move(gameState*-1)
	print("move:", move)
	grav(gameState, move, -1)
	print(gameState)
	print("   0   1   2   3   4   5   6")
	if(who_solo_win(gameState) != 0):
		break
'''
for turn in range(42):
	move = make_move(gameState*-1)
	grav(gameState, int(move), -1)
	print("move:", move)
	print(gameState)
	print("   0   1   2   3   4   5   6")
	if(who_solo_win(gameState) != 0):
		break

	move = input("Please enter your move: ")
	grav(gameState, int(move), 1)
	print("   0   1   2   3   4   5   6")
	print(gameState)
	if(who_solo_win(gameState) != 0):
		break

gameState = np.array([[0,  0,  0,  1,  0,  0,  0,],
                      [0,  0,  0,  1,  0,  0, -1,],
                      [0,  0,  1, -1,  0,  1, -1,],
                      [0,  0, -1, -1,  0,  1,  1,],
                      [0,  0,  1,  1, -1, -1,  1,],
                      [0,  0, -1,  1, -1, -1, -1]])
print(make_move(gameState*-1)) # Check why it makes losing play.
'''
