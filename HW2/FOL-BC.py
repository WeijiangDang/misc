import sys

def FOL_BC_ASK(KB, query):
	print("Ask: %s"%query)
	output_file = open("output.txt","w")
	output_file.write("Ask: %s"%query)
	return FOL_BC_OR(KB, query, {})

def FOL_BC_OR(KB, goal, theta):
	for rule in FETCH_RULES_FOR_GOAL(KB, goal):
		lhs = rule.split(' => ')[0]
		rhs = rule.split(' => ')[1]
		STANDARDIZE_VARIABLES(lhs, rhs, theta)
		for theta_ in FOL_BC_AND(KB, lhs, UNIFY(rhs, goal, theta)):
			yield theta
			print theta

def	FOL_BC_AND(KB, goals, theta):
	if theta == 'failure':
		return
	elif len(goals) == 0:
		yield theta
		print theta
	else:
		first, rest = FIRST(goals), REST(goals)
		print ("First and rest as %s, %s"%(first, rest) )
		for theta_ in FOL_BC_OR(KB, SUBST(theta, first), theta):
			for theta__ in FOL_BC_AND(KB, rest, theta_):
				yield theta__
				print theta__

def SUBST(theta, first):
	print("Making substitution for %s"%first)
	posL = first.index('(')
	posR = first.index(')')
	first_args = first[posL + 1: posR].split(', ')
	print first_args
	#print theta.next()
	for arg in first_args:
		for k in theta:
			if(k == arg):
				first.replace(arg, theta[k])
	print first
	return first
		
				
def FIRST(goals):
	return goals.split(' && ')[0]

def REST(goals):
	return goals.split(' && ')[1:]
				
def UNIFY(rhs, goal, theta):
	print("Unifying for %s and %s"%(rhs, goal))
	#Check if new pair should be added
	rhs_pre = rhs.split('(')[0]
	goal_pre = goal.split('(')[0]
	posL = rhs.index('(')
	posR = rhs.index(')')
	rhs_args = rhs[posL + 1: posR].split(', ')
	posL = goal.index('(')
	posR = goal.index(')')
	goal_args = goal[posL + 1: posR].split(', ')
	if(rhs_pre == goal_pre):
		for j in range( len(rhs_args) ):
			if(rhs_args[j][0].isupper() and goal_args[j][0].islower() and not(theta.has_key(goal_args[j] ) ) ):
				print("Binding goal_arg: %s to rhs_arg: %s"%(goal_args[j], rhs_args[j]))
				theta[goal_args[j]] =  rhs_args[j]
			if(rhs_args[j][0].islower() and goal_args[j][0].isupper() and not(theta.has_key(rhs_args[j] ) ) ):
				print("Binding rhs_arg: %s to goal_arg: %s"%(rhs_args[j], goal_args[j]))
				theta[rhs_args[j]] =  goal_args[j]
			#Both variable then unify i to q
			if(rhs_args[j][0].islower() and ( rhs_args[j] == goal_args[j]) and not(theta.has_key(goal_args[j] ) )):
				print("Binding goal_arg: %s to rhs_arg: %s"%(goal_args[j], rhs_args[j]))
				theta[goal_args[j]] =  rhs_args[j]
			#Different constant cannot unify
			#if(i_right_args[j][0].isupper() and query_args[j][0].isupper() and ( i_right_args[j] != query_args[j])):
				#return 'failure'
	yield theta
	
				
def STANDARDIZE_VARIABLES(lhs, rhs, theta):
	print("Standardizing variables...") 
	#Standardize lhs
	for r in lhs.split(' && '):
		posL = r.index('(')
		posR = r.index(')')
		r_args = r[posL + 1: posR].split(', ')
		for arg in r_args:
			for k in theta:
				if(k == arg):
					rhs.replace(arg, arg + '1')
					print("New variable for lhs as"%(arg+'1'))
	#Standardize rhs
	posL = rhs.index('(')
	posR = rhs.index(')')
	rhs_args = rhs[posL + 1: posR].split(', ')
	for arg in rhs_args:
		for k in theta:
			if(k == arg):
				rhs.replace(arg, arg + '1')
				print("New variable for rhs as"%(arg+'1'))
	
def FETCH_RULES_FOR_GOAL(KB, goal):
	rules = []
	for sentence in KB:
		if(sentence.find(' => ') >= 0 ):
			right = sentence.split(' => ')[1]
			if (right.split('(')[0] == goal.split('(')[0] ):
				rules.append(sentence)
	return rules
				
def main():
	#Read the input file
	input_file = sys.argv[2]
	file = open(input_file)
	#First line is the query we want to know
	query = file.readline()
	print("Showing input file")
	print("Query: %s" %(query))
	#Second line is the number of clauses in KB
	KBlen = int(file.readline())
	KB = [[]for i in range(KBlen)]
	#Read KB
	for i in range(KBlen):
		KB[i] = file.readline()
		print KB[i]
			
	#Open write file
	output_file = open("output.txt","w")
	
	#Check the query 
	querys = query.split(' && ')
	for q in querys:
			theta = FOL_BC_ASK(KB, q)
	for t in theta:
		print t

if __name__=='__main__':
	main()
