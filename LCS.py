import sys
import copy

cache = {}

def LCS(x,y,m,n):
	try:
		return cache[tuple(sorted((tuple(x[0:m]), tuple(y[0:n]))))]
	except KeyError:
		if ((m==0)|(n==0)):
			cache[tuple(sorted((tuple(x), tuple(y))))] = []
			return []
		else:
			if (x[m-1]==y[n-1]):
				cache[tuple(sorted((tuple(x[0:m]), tuple(y[0:n]))))] = LCS(x,y,m-1,n-1)+[x[m-1]]
				return LCS(x,y,m-1,n-1)+[x[m-1]]
			else:
				if len(LCS(x,y,m,n-1))<len(LCS(x,y,m-1,n)):
					cache[tuple(sorted((tuple(x[0:m]), tuple(y[0:n]))))] = LCS(x,y,m-1,n)
					return LCS(x,y,m-1,n)
				else:
					cache[tuple(sorted((tuple(x[0:m]), tuple(y[0:n]))))] = LCS(x,y,m,n-1)
					return LCS(x,y,m,n-1)



n = raw_input()
n = map(int,n.split( ))
for i in range(0,len(n)):
    s = raw_input()
    if (type(s)!= str):
        print("invalid string:enter string")
        sys.exit()
    s = map(int, s.split( ))
    if i==0:
    	a = copy.deepcopy(s)
print ' '.join(map(str, LCS(a,s,len(a),len(s)))) 


