import sys
#---------------Define functions---------------#
def getP(x, xpn, givenpn, table):
	for i in table:
		if i[0] == x:
			if i[1] == '':
				if isinstance(i[2], float):
					if xpn == '+':
						return i[2]
					else:
						return 1 - i[2]
				else:
					return 1.0
				
			else:
				px = Parents(x, table)
				if xpn == '+':
					return i[2][givenpn]
				else:
					return 1 - i[2][givenpn]
				
def Parents(x, bn):
	for i in bn:
		if i[0] == x:
			return i[1]
			
def getVars(table):
	VARS = []
	for i in table:
		if (not i[0] in VARS) and (not i[0] == '') and (not i[0] == 'utility'):
			VARS.append(i[0])
		for j in i[1].split(' '):
			if (not j in VARS) and ( not j == ''):
				VARS.append(j)
	return VARS
	
def ENUMERATION_ASK(X, e, bn):
	Q = {}
	NQ = {}
	k = X.keys()
	for x in X:
		exi = e
		VARS = getVars(bn)
		#print VARS
		for i in k:
			exi[x] = X[x]
	f = ENUMERATE_ALL(bn, VARS, exi)
	#print f
	VARS = getVars(bn)
	enom = {}

	if X == e: 
		return f
	else:
	
		l = len(X)
		enom = {}
		if l == 1:
			for i in e :
				enom[i] = e[i]
			for x in X:
				enom[x] = '+'
	
			t1 = ENUMERATE_ALL(bn, VARS, enom)
			VARS = getVars(bn)
			for i in e :
				enom[i] = e[i]
			for x in X:
				enom[x] = '-'
	
			t2 = ENUMERATE_ALL(bn, VARS, enom)
			a = 1/(t1 + t2)
	
		if l == 2:
			for i in e :
				enom[i] = e[i]
			keys = X.keys()
			lk = len(keys)
			enom[keys[0]] = '+'
			enom[keys[1]] = '+'

			t1 = ENUMERATE_ALL(bn, VARS, enom)
			VARS = getVars(bn)
			for i in e :
				enom[i] = e[i]
			enom[keys[0]] = '+'
			enom[keys[1]] = '-'
	
			t2 = ENUMERATE_ALL(bn, VARS, enom)
			for i in e :
				enom[i] = e[i]
			keys = X.keys()
			lk = len(keys)
			enom[keys[0]] = '-'
			enom[keys[1]] = '+'

			t3 = ENUMERATE_ALL(bn, VARS, enom)
			VARS = getVars(bn)
			for i in e :
				enom[i] = e[i]
			enom[keys[0]] = '-'
			enom[keys[1]] = '-'
		
			t4 = ENUMERATE_ALL(bn, VARS, enom)
			a = 1/(t1 + t2 + t3 + t4)
	
		return f * a

def ENUMERATE_ALL(bn, VARS, e):
	if len(VARS) == 0:
		return 1.0
	else:
		y = VARS.pop(0)
		#print "yyyyyyyyyyyyyyyyyy"
		#print y
		ypa = Parents(y, bn)
		##print "ypaaaaaaaaaaaaaaaaa"
		##print ypa
		givenpn = []
		if not len(ypa) == 0:
			pa = ypa.split(' ')
			##print "*********"
			##print pa 
			for j in pa:
				##print "---------"
				##print j,e[j]
				
				givenpn.append(e[j] + ' ')
	
		g = ''.join(givenpn)
	
		g = g.strip()
	
		for i in e:
			if i == y:
				#print getP(y, e[y], g, bn)
				#print '* in e'
				return getP(y, e[y], g, bn) * ENUMERATE_ALL(bn, VARS, e)
		eyp = {}
		eyn = {}
		for i in e :
			eyp[i] = e[i]
			eyn[i] = e[i]
	
		eyp[y] = '+'

		eyn[y] = '-'
	
		VARSn = []
		for v in VARS:
			VARSn.append(v)
		#print getP(y, '+', g, bn)
		#print '* sum'
		#print getP(y, '-', g, bn)
		#print '* sum'
		return  getP(y, '+', g, bn) * ENUMERATE_ALL(bn, VARS, eyp) + getP(y, '-', g, bn) * ENUMERATE_ALL(bn, VARSn, eyn)
		
#---------------Main function------------------#
def main():
#---------------Read file input----------------#
	input_file = sys.argv[2]
	output = open("output.txt", 'w')
	res = []
	file = open(input_file)
	#---------------Ask line part--------------#
	line = file.readline()[:-1]
	ask_line = []
	while not line.startswith('*'):
		ask_line.append(line)
	
		line = file.readline()[:-1]

	#---------------Table part-----------------#

	table = []
	while 1:
		line = file.readline()[:-1]
		
		if line.startswith('*'):
			continue
		if not len(line):
			break
	
		left = line.split(' | ')[0]
	
		if len(line.split(' | ')) > 1:
		#--------------With given---------------#
			right = line.split(' | ')[1]
		
			#-----Num of variables given--------#
			num_given = len(right.split(' '))
		
			#--------Read next line-------------#
			next_line = file.readline()[:-1]
		
			pair = {}
			
			while (not next_line.startswith('*') ) and len(next_line):
				
				t = next_line.split(' ', 1)
				
				pair[t[1]] = float(t[0])
				next_line = file.readline().strip('\n')
				
				
			table.append( (left, right, pair) )
		else:
		#--------------Without given-----------#
			next_line = file.readline()[:-1]
			if next_line.islower():
				table.append( (left, '', next_line ) )
				
			else:
				table.append( (left, '', float(next_line) ) )
	#print table
	
	#------------Table part end----------------#	
	VARS = getVars(table)
	#print ask_line
	for i in ask_line:
		X = {}
		e = {}
		pre = i.split('(')[0]
		#print "11111111111111111111"
		#print pre
		rear = i.split('(')[1][:-1]
		query = rear.split(' | ')[0]
		if pre == 'P':
			if len(rear.split(' | ')) > 1:
				given = rear.split(' | ')[1]
			else:
				given = ''
		
			q = query.split(', ')
		
			if given:
				g = given.split(', ')
				for k in g:
					key = k.split(' = ')[0]
					value = k.split(' = ')[1]
					e[key] = value

			for j in q:
				key = j.split(' = ')[0]
			
				value = j.split(' = ')[1]
				X[key] = value
				e[key] = value
			#print e
			dis = ENUMERATION_ASK( X, e, table)

			str = '%.2f' %dis
			res.append(str + '\n')
			#print res
		if pre == 'EU':
			X = {}
			e = {}
			if len(rear.split(' | ')) > 1:
				given = rear.split(' | ')[1]
			else:
				given = []
			##print given
			#given = list(given)
			t = query.split(', ')
			#print "ttttttttttttt"
			#print t
			for x in t:
				key = x.split(' = ')[0]
				value = x.split(' = ')[1]
				e[key] = value
			if len(given) > 0:
				g = given.split(', ')
				for k in g:
					key = k.split(' = ')[0]
					value = k.split(' = ')[1]
					e[key] = value
			#print e
			utilist = Parents('utility', table)
			u = utilist.split(' ')
			num = len(u)
			for x in u:
				if num == 1:
					X[x] = '+'
					#print X,e
					p1 = ENUMERATION_ASK(X, e, table)
					#print p1
					for tmp in table:
						if tmp[0] == 'utility':
							u1 = tmp[2]['+']
							#print u1
					X[x] = '-'
					p2 = ENUMERATION_ASK(X, e, table)
					#print p2
					for tmp in table:
						if tmp[0] == 'utility':
							u2 = tmp[2]['-']
							#print u2
					eu = p1 * u1 + p2 * u2
					#print eu
					str = '%d' %round(eu)
					res.append(str + '\n')
					#print res
				if num == 2:
					X[u[0]] = '+'
					X[u[1]] = '+'
					p1 = ENUMERATION_ASK(X, e, table)
					for tmp in table:
						if tmp[0] == 'utility':
							u1 = tmp[2]['+ +']
							#print u1
					X[u[0]] = '+'
					X[u[1]] = '-'
					p2 = ENUMERATION_ASK(X, e, table)
					for tmp in table:
						if tmp[0] == 'utility':
							u2 = tmp[2]['+ -']
							#print u2
					X[u[0]] = '-'
					X[u[1]] = '+'
					p3 = ENUMERATION_ASK(X, e, table)
					for tmp in table:
						if tmp[0] == 'utility':
							u3 = tmp[2]['- +']
							#print u3
					X[u[0]] = '-'
					X[u[1]] = '-'
					p4 = ENUMERATION_ASK(X, e, table)
					for tmp in table:
						if tmp[0] == 'utility':
							u4 = tmp[2]['- -']
							#print u4
					eu = p1 * u1 + p2 * u2 + p3 * u3 + p4 * u4
					#print eu
					str = '%d' %round(eu)
					res.append(str + '\n')
					#print res
			#ENUMERATION_ASK(X, e, table)
		#if pre == 'MEU':
			
	t= res.pop()
	res.append(t.strip())
	output.writelines(res)
	#print table
	#print getP('LeakIdea', '+', '', table)
	
if __name__=='__main__':
	main()