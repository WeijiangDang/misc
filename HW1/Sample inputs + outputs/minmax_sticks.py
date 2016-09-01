from sys import maxsize

#********************************************************************************************************************************************************
#Builder
class Move:
	def __init__(self, i_movei, i_movej):
		self.i_movei = i_movei
		self.i_movej = i_movej
		#moveType: 0 means sneak move; 1 means raid move
		#self.i_moveType = i_moveType
		
class Node(object):
	def __init__(self, i_depth, i_playerNum, boardState, gridValue, move, i_value):
		self.i_depth = i_depth
		#i_playerNum: 1 for 'X' max, 0 for 'O' min
		self.i_playerNum = i_playerNum
		self.boardState = boardState
		self.gridValue = gridValue
		self.move = MakeMoveList().pop()
		self.i_value = maxsize * -i_playerNum
		self.children = []
		self.CreateChildren()
	
	def CreateChildren(self):
		if self.i_depth >= 0:
			#Mark raid move out
			r = self.MakeMoveList()
			
			#Generate available move list 
			moveList = self.MakeMoveList()
			i_squareRemaining = len(moveList)
			while i_squareRemaining != 0:
				move = moveList.pop()
				nextState = self.boardState
				nextState[move.i_movei][move.i_movej] = 'X'
				self.children.append( Node( self.i_depth - 1, -self.i_playerNum, nextState, self.gridValue, move, self.CalVal(nextState, self.gridValue)))
	
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
		
	#Mark raid move out
	def MarkRaid():
		r = [[0,0,0,0,0] for i in range(5)]
		for i in range(5):
			for j in range(5):
				#For raid(our square is around), we mark the potential raid square
				if self.boardState[i][j] == 'X':
						#r[i][j] = t[i][j]
						#We need to check the square above it, except for the first row
					if i != 0:
							#Mark the unoccupied square as potential raid square
						if self.boardState[i-1][j] == '*':
								#print "Checking t %d %d %s"%(i-1, j, t[i-1][j])
							r[i-1][j] += 1 
						#We need to check the square left to it, except for the first collum
					if j != 0:
							#Mark the unoccupied square as potential raid square
						if self.boardState[i][j-1] == '*':
								#print "Checking t %d %d %s"%(i, j-1, t[i][j-1])
							r[i][j-1] += 1
						#We need to check the square below it, except for the last row
					if i != 4:
							#Mark the unoccupied square as potential raid square
						if self.boardState[i+1][j] == '*':
								#print "Checking t %d %d %s"%(i+1, j, t[i+1][j])
							r[i+1][j] += 1
						#We need to check the square right to it, except for the last collum
					if j != 4:
							#Mark the unoccupied square as potential raid square
						if self.boardState[i][j+1] == '*':
								#print "Checking t %d %d %s"%(i, j+1, t[i][j+1])
							r[i][j+1] += 1
		return r
		
	#Make a list for available move 	
	def MakeMoveList():
		moveList = []
			for i in range(5):
				for j in range(5):
					if self.boardState[i][j] == '*':
						moveList.append( Move( i, j) )
		return moveList
#********************************************************************************************************************************************************		

#********************************************************************************************************************************************************
#Algorithm
def MinMax(node, i_depth, i_playerNum):
	if(i_depth == 0) or (len(node.MakeMoveList()) == 0):
		return node.i_value
	
	i_bestValue = maxsize * -i_playerNum
	
	for child in node.children:
		i_val = MinMax(child, i_depth - 1, -i_playerNum)
		if (abs(maxsize * i_playerNum - i_val) < (abs(maxsize * i_playerNum - i_bestValue))):
			i_bestValue = i_val
	
	return i_bestValue 
#********************************************************************************************************************************************************

#********************************************************************************************************************************************************
#Implementation
input_file = open('2/input.txt')
try:
	def main():
		#Input
		task = input_file.readline()
		print ("Task #%s"%(task))
		player = input_file.readline()
		print ("Player %s"%(player))
		depth = input_file.readline()
		print ("Depth %s"%(depth))
		if depth%2 == 0:
			i_curPlayer = 1
		else:
			i_curPlayer = -1
		print "Board grid value:"
		s = [[]for i in range(5)]
		sum = 0
		for i in range(5):
			strValue = input_file.readline()
			s[i] = strValue.split( )
			for j in range(5):
				s[i][j] = int (s[i][j])
				sum += s[i][j]
				print s[i][j],
			print
		print "\nTotal value: %d\n"%sum
		print "Current board state:"
		t = [[]for i in range(5)]
		for i in range(5):
			t[i] = input_file.readline()
			print t[i],
		r = [[0,0,0,0,0] for i in range(5)]
		v = [[0,0,0,0,0] for i in range(5)]
		
		#Make move list
		moveList = []
			for i in range(5):
				for j in range(5):
					if self.t[i][j] == '*':
						moveList.append( Move( i, j) )
		
		while (len(moveList) > 0):
			move = moveList.pop()
			node = Node(depth, i_curPlayer, t, s)
			
			
	if __name__=='__main__':
		main()
finally:
	input_file.close() 
#********************************************************************************************************************************************************