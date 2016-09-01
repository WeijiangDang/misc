input_file = open('1/input.txt')
try:
	def main():
		#Input
		task = input_file.readline()
		print ("Task #%s"%(task))
		player = input_file.readline()
		print ("Player %s"%(player))
		depth = input_file.readline()
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
		r = [[0,0,0,0,0] for i in range(5)]
		v = [[0,0,0,0,0] for i in range(5)]
		#print r
		
		#Search for the move with greatest value
		print "\n\nSearching for the available moves..."
		for i in range(5):
			for j in range(5):
				#The square should be unoccupied so that we can make a move there
				#print "Square %d %d is %s"%(i,j,t[i][j])
				
				 
				#For sneak(no square around is on our side)
					
				#For raid(our square is around), we mark the potential raid square
				if t[i][j] == 'X':
					#r[i][j] = t[i][j]
					#We need to check the square above it, except for the first row
					if i != 0:
						#Mark the unoccupied square as potential raid square
						if t[i-1][j] == '*':
							#print "Checking t %d %d %s"%(i-1, j, t[i-1][j])
							r[i-1][j] += 1 
					#We need to check the square left to it, except for the first collum
					if j != 0:
						#Mark the unoccupied square as potential raid square
						if t[i][j-1] == '*':
							#print "Checking t %d %d %s"%(i, j-1, t[i][j-1])
							r[i][j-1] += 1
					#We need to check the square below it, except for the last row
					if i != 4:
						#Mark the unoccupied square as potential raid square
						if t[i+1][j] == '*':
							#print "Checking t %d %d %s"%(i+1, j, t[i+1][j])
							r[i+1][j] += 1
					#We need to check the square right to it, except for the last collum
					if j != 4:
						#Mark the unoccupied square as potential raid square
						if t[i][j+1] == '*':
							#print "Checking t %d %d %s"%(i, j+1, t[i][j+1])
							r[i][j+1] += 1
						
		print "\nPotential raid square:"		
		for i in range(5):
			for j in range(5):
				print r[i][j],
			print
			
		#Check the value we get from the move
		print "\nNow check the value we get from the move"
		for i in range(5):
			for j in range(5):
				#Sneak
				if t[i][j] == '*' and r[i][j] == 0 :
					v[i][j] += s[i][j]
				#Raid
				if t[i][j] == '*' and r[i][j] != 0 :
					v[i][j] += s[i][j]
					#We need to check the square above it, except for the first row
					if i != 0:
						if t[i-1][j] == 'O':
							#print "Checking t %d %d %s"%(i-1, j, t[i-1][j])
							v[i][j] += s[i-1][j]
					#We need to check the square left to it, except for the first collum
					if j != 0:
						if t[i][j-1] == 'O':
							#print "Checking t %d %d %s"%(i, j-1, t[i][j-1])
							v[i][j] += s[i][j-1]
					#We need to check the square below it, except for the last row
					if i != 4:
						if t[i+1][j] == 'O':
							#print "Checking t %d %d %s"%(i+1, j, t[i+1][j])
							v[i][j] += s[i+1][j]
					#We need to check the square right to it, except for the last collum
					if j != 4:
						if t[i][j+1] == 'O':
							#print "Checking t %d %d %s"%(i, j+1, t[i][j+1])
							v[i][j] += s[i][j+1]
					
		print "\nPotential value on square taken:"		
		for i in range(5):
			for j in range(5):
				print v[i][j],
			print
		#Find the max value we can get
		max = 0
		maxi = 0
		maxj = 0
		for i in range(5):
			for j in range(5):
				if v[i][j] > max:
					max = v[i][j]
					maxi = i
					maxj = j
				#if v[i][j] == max:
		print "Max value we get is %d with move %d %d"%(max, maxi, maxj)
		move = 0
		if r[maxi][maxj] != 0:
			print "It is a raid move"
			move = 1
		else:
			print "It is a sneak move"
			
		#Tie breaking when multi-move of same value 
	
	
		#Take the move
		n = [[] for i in range(5)]
		
		for i in range(5):
			for j in range(5):
				#Sneak move
				if move == 0:
				#print i,j
					if i != maxi or j!= maxj:
						#print "n %d %d = t %d %d"%(i, j, i, j)
						n[i].append(t[i][j])
						#print n[i][j]
					if i == maxi and j == maxj:
						n[i].append('X')
				#Raid move
				if move == 1:
					#Check if there is opponet's square involved in the raid
					x = [[0,0,0,0,0]for k in range(5)]
					#We need to check the square above it, except for the first row
					if maxi != 0:
						if t[maxi-1][maxj] == 'O':
							#print "Checking t %d %d %s"%(maxi-1, maxj, t[maxi-1][maxj])
							x[maxi - 1][maxj] += 1
					#We need to check the square left to it, except for the first collum
					if maxj != 0:
						if t[maxi][maxj-1] == 'O':
							#print "Checking t %d %d %s"%(maxi, maxj-1, t[maxi][maxj-1])
							x[maxi][maxj-1] += 1
					#We need to check the square below it, except for the last row
					if maxi != 4:
						if t[maxi+1][maxj] == 'O':
							#print "Checking t %d %d %s"%(maxi+1, maxj, t[maxi+1][maxj])
							x[maxi+1][maxj] += 1
					#We need to check the square right to it, except for the last collum
					if maxj != 4:
						if t[maxi][maxj+1] == 'O':
							#print "Checking t %d %d %s"%(maxi, maxj+1, t[maxi][maxj+1])
							x[maxi][maxj+1] += 1
					
					if (i != maxi or j!= maxj) and x[i][j] == 0:
						#print "n %d %d = t %d %d"%(i, j, i, j)
						n[i].append(t[i][j])
						#print n[i][j]
					if (i == maxi and j == maxj) or x[i][j] != 0:
						n[i].append('X')
		
		#Raid taking square
		if move == 1:	
			print "\nRaid taking square"
			for i in range(5):
				for j in range(5):
					print x[i][j],
				print	
		#Show next state and write it to next_state.txt
		if move == 0:
			print "\nNext state"
			for i in range(5):
				for j in range(5):
					print n[i][j],
				print
			
		next_state = open('next_state.txt', 'w')
		for i in range(5):	
			next_state.writelines(n[i])
			next_state.write('\n')
		next_state.close()
		
	if __name__=='__main__':
		main()
finally:
	input_file.close() 