#***********************************************************************
#Builder
class Node(object):
	def __init__(self, i_depth, i_x, i_y, i_value):
		self.i_depth = i_depth
		self.i_x = i_x
		self.i_y = i_y
		self.i_value = i_value
		
		
#***********************************************************************
#Algorithm
def MinMax (boardState, gridValue, depth):
	root = Node(0, -1, -1, -1000)
	traverse_log.write("Node,Depth,Value\n")
	traverse_log.write("root,0,-Infinity\n")
	print "\nroot 0 -Infinity"
	bestVal = MaxMove(root, boardState, gridValue, depth)
	print "root %d %d"%(root.i_depth, root.i_value)
	traverse_log.close()
	return bestVal
	
def MaxMove(node, boardState, gridValue, depth):
	#Get children[]
	print "\nRun max move..."
	#print "Current node: %d %d depth %d value %d"%(node.i_x, node.i_y, node.i_depth, node.i_value)
	children = []
	childrenPos = CreateChildrenPos(boardState)
	#print childrenPos
	for childPos in childrenPos:
		children.append( Node(node.i_depth + 1, childPos[0], childPos[1], 1000) )
	#print children
	curValue = node.i_value
	for child in children:
		print "child depth = %d value= %d x = %d y = %d"%(child.i_depth, child.i_value, child.i_x, child.i_y)
		boardState = BuildBoard(boardState, child.i_x, child.i_y, 'X')
		#Search for the max val in children
		if child.i_depth == depth:
			child.i_value = CalVal(boardState, gridValue)
			index = GetIndex(child)
			print "%s%d child depth: %d value: %d"%(index[0], index[1], child.i_depth, child.i_value)
			traverse_log.write("%s%d,%d,%d\n"%(index[0], index[1], child.i_depth, child.i_value))
			boardState = BuildBoard(boardState, child.i_x, child.i_y, '*')
		if child.i_depth < depth:
			child.i_value = MinMove(child, boardState, gridValue, depth)
			index = GetIndex(child)
			print "%s%d child depth: %d value: %d"%(index[0], index[1], child.i_depth, child.i_value)
			#node.i_value = curValue
		if curValue < child.i_value:
			curValue = child.i_value
			node.i_value = curValue
			#Record the move
			move = [child.i_x, child.i_y]
			index = GetIndex(node)
			if len(index) == 4:
				print "%s depth: %d value: %d"%(index, node.i_depth, node.i_value)
				traverse_log.write("%s,%d,%d\n"%(index, child.i_depth, child.i_value))
			if len(index) == 2:
				print "%s%d child depth: %d value: %d"%(index[0], index[1], node.i_depth, node.i_value)
				traverse_log.write("%s%d,%d,%d\n"%(index[0], index[1], node.i_depth, node.i_value))
		else:
			index = GetIndex(node)
			if len(index) == 4:
				print "%s depth: %d value: %d"%(index, node.i_depth, node.i_value)
				traverse_log.write("%s,%d,%d\n"%(index, node.i_depth, node.i_value))
			if len(index) == 2:
				print "%s%d child depth: %d value: %d"%(index[0], index[1], node.i_depth, node.i_value)
				traverse_log.write("%s%d,%d,%d\n"%(index[0], index[1], node.i_depth, node.i_value))
		
	return curValue
	
def MinMove(node, boardState, gridValue, depth):
	#Get children[]
	print "\nRun min move..."
	#print node.i_x, node.i_y, node.i_depth, node.i_value
	children = []
	childrenPos = CreateChildrenPos(boardState)
	for childPos in childrenPos:
		children.append( Node(node.i_depth + 1, childPos[0], childPos[1], -1000) )
	curValue = node.i_value
	for child in children:
		print "child depth = %d value= %d x = %d y = %d"%(child.i_depth, child.i_value, child.i_x, child.i_y)
		boardState = BuildBoard(boardState, child.i_x, child.i_y, 'O')
		#Search for the max val in children
		if child.i_depth == depth:
			child.i_value = CalVal(boardState, gridValue)
			index = GetIndex(child)
			print "%s%d child depth: %d value: %d"%(index[0], index[1], child.i_depth, child.i_value)
			boardState = BuildBoard(boardState, child.i_x, child.i_y, '*')
		if child.i_depth < depth:
			child.i_value = MaxMove(child, boardState, gridValue, depth)
			index = GetIndex(child)
			print "%s%d child depth: %d value: %d"%(index[0], index[1], child.i_depth, child.i_value)
			#node.i_value = curValue
		if curValue > child.i_value:
			print "current value %d"%curValue
			curValue = child.i_value
			node.i_value = curValue
			#Record the move
			move = [child.i_x, child.i_y]
			index = GetIndex(node)
			print "%s depth: %d value: %d"%(index, node.i_depth, node.i_value)
		else:
			index = GetIndex(node)
			print "%s depth: %d value: %d"%(index, node.i_depth, node.i_value)
	return curValue

def GetIndex(node):
	index = [ 0, 0]
	if node.i_x == -1 and node.i_y == -1:
		return 'root'
	if node.i_y == 0:
		index[0] = 'A'
	if node.i_y == 1:
		index[0] = 'B'
	if node.i_y == 2:
		index[0] = 'C'
	if node.i_y == 3:
		index[0] = 'D'
	if node.i_y == 4:
		index[0] = 'E'
	index[1] = node.i_x + 1
	return index
	
def CreateChildrenPos(boardState):
	childrenPos = []
	for i in range(5):
		for j in range(5):
			if boardState[i][j] == '*':
				childrenPos.append([i, j])
	return childrenPos
	
#Build Board
def BuildBoard(boardState, x, y, t):
	newState = [[0 for i in range(5)]for i in range(5)]
	# newState[0][0] = 1
	#print newState
	#print "x = %d y = %d"%(x, y)
	for i in range(5):
		#print i
		for j in range(5):
			#print j
			if i == x and j == y:
				#print "new state at %d %d from %s to %s"%(x, y, boardState[i][j], t)
				newState[i][j] = t
			else:
				newState[i][j] = boardState[i][j]
	return newState
	
#Calculate the value
def CalVal(boardState, gridValue):
	value = 0
	for i in range(5):
		for j in range(5):
			if boardState[i][j] == 'X':
				value += gridValue[i][j]
			if boardState[i][j] == 'O':
				value -= gridValue[i][j]
	return value
	
#***********************************************************************
#main()	
input_file = open('2/input.txt')
traverse_log = open('traverse_log.txt', 'w')
# next_state = open('next_state.txt', 'w')
 
try:
	if __name__ == '__main__':
		#****************************************
		#Input
		task = input_file.readline()
		print ("Task #%s"%(task))
		player = input_file.readline()
		print ("Player %s"%(player))
		depth = int(input_file.readline())
		print ("Depth %s"%(depth))
		print "Board grid value:"
		s = [[]for i in range(5)]
		for i in range(5):
			strValue = input_file.readline()
			s[i] = strValue.split( )
			for j in range(5):
				s[i][j] = int (s[i][j])
				print s[i][j],
			print
		print
		print "Current board state:"
		t = [[]for i in range(5)]
		for i in range(5):
			t[i] = input_file.readline()
			print t[i],
		#r = [[0,0,0,0,0] for i in range(5)]
		#v = [[0,0,0,0,0] for i in range(5)]
		
		#****************************************
		#Process
		MinMax(t, s, depth)
		
finally:
	input_file.close() 
	