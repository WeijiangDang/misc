import sys
import collections

def main():
	#Read the input file
	input_file = sys.argv[2]
	file = open(input_file)
	#First line is the query we want to know
	query = file.readline()
	print("Query: %s" %(query))
	#Second line is the number of clauses in KB
	KBlen = int(file.readline())
	KB = [[]for i in range(KBlen)]
	KBA = []
	KBI = []
	for i in range(KBlen):
		KB[i] = file.readline()
		print KB[i]
		#Split KB into atomic and implication
		if( KB[i].find(' => ') < 0):
		#Atomic
			KBA.append( KB[i] )
		else:
		#Implecation
			KBI.append( KB[i] )
			
	for i in KBA:
		print("Atomic sentence: %s"%i)
	print len(KBA)
	for i in KBI:
		print("Implecation sentence: %s"%i)
	print len(KBI)
	
	#Open write file
	output_file = open("output.txt","w")
	
	#Check the query 
	querys = query.split(' && ')
	for q in querys:
		print("Ask: %s"%(q))
		output_file.write("Ask: %s"%(q))
		
		#Search for the predicate in KB
		posL = q.index('(')
		posR = q.index(')')
		query_pre = q[0:posL]
		query_args = q[posL + 1: posR]
		query_args = query_args.split(', ')
		query_args_count = len(query_args)
		print query_pre
		print query_args
		print query_args_count
		#Check in KBA
		#If matches then true
		for i in KBA:
			posL = i.index('(')
			posR = i.index(')')
			i_pre = i[0:posL]
			i_args = i[posL + 1:posR]
			i_args = i_args.split(', ')
			i_args_count = len(i_args)
			if( i_pre == query_pre and i_args == query_args):
				print "True: %s"%q
					
		#Check in KBI
		#If on the right side of ' => ' then backward chain
		for i in KBI:
			i_left = i.split(' => ')[0]
			i_right = i.split(' => ')[1]
			print i_right
			posL = i_right.index('(')
			posR = i_right.index(')')
			i_right_pre = i_right[0:posL]
			i_right_args = i_right[posL + 1:posR]
			i_right_args = i_right_args.split(', ')
			i_right_args_count = len(i_args)
			print i_right_pre
			print query_pre
			theta = collections.OrderedDict()
			if(query_pre == i_right_pre):
				#Unify query with i
				for j in range( len(i_right_args) ):
					#Same constant then no unify
					if(i_right_args[j][0].isupper() and ( i_right_args[j] == query_args[j] ) ):
						continue
					#Both variable then unify i to q
					if(i_right_args[j][0].islower() and ( i_right_args[j] == query_args[j]) ):
						continue
					#Constant and variable unify variable to constant
					if(i_right_args[j][0].isupper() and query_args[j][0].islower()):
						print("Binding query_arg to i_right_arg")
						theta[query_args[j]] =  i_right_args[j]
					if(i_right_args[j][0].islower() and query_args[j][0].isupper()):
						print("Binding i_right_arg to query_arg")
						theta[i_right_args[j]] =  query_args[j]
					#Different constant cannot unify
					if(i_right_args[j][0].isupper() and query_args[j][0].isupper() and ( i_right_args[j] != query_args[j])):
						break
			#Get the theta after unification			
			print("Printing theta key value pairs")
			for k,v in theta.items():
				print k,v
			
			#Check the left conjuctions
			#The checking process is just like above
			
#def FOL_BC_ASK(KBA, KBI, query):	


if __name__=='__main__':
	main()
