#This will take a lists of lists and convert them to one list
def flatten(listIn):
	flat = list()
	for i in listIn:
		if isinstance(i, list):
			for e in i:
				if isinstance(e,list):
					for a in e:
						flat.append(a)
				else:
					flat.append(e)
		else:
			flat.append(i)
	return flat
		
#Making power sets of a list
def powerset(powerList):	
    x = len(s)
    pw = list()
    for i in range(1 << x):
        pw.append([s[j] for j in range(x) if (i & (1 << j))])
    return pw
	   
	   
#getting all premutations of a list
def all_perms(List):
	if len(List) <= 1:
		return List
	l = [] 
    for i in range(len(List)):
       m = List[i]
       remLst = List[:i] + List[i+1:]
       for p in all_perms(remLst):
           l.append([m] + [p])
    return l
		
		
#makes a spiral array ending in the designated cornor
def spiral(n, c):
	N = (0, -1)
	E = (1,0)
	W = (-1,0)
	S = (0,1)
    turn_right = {N: E, E: S, S: W, W: N}
	if n<1:
        return []
	if n %2 == 0:
		if c == 4:
			x = (n//2) -1
			y = (n//2) 
			dx,dy = W
		if c == 3:
			x = (n//2) -1
			y = (n//2) -1
			dx,dy= N
		if c == 2:
			x = (n//2) 
			y = (n//2) 
			dx,dy = S
		if c == 1:
			x = (n//2) 
			y = (n//2) -1
			dx,dy = E
	else:
		x = n // 2 
		y = n // 2
		if c == 4:
			dx,dy = E 
		if c == 3:
			dx,dy = S
		if c == 2:
			dx,dy = N
		if c == 1:
			dx,dy = W
	matrix = [[None] * n for _ in range(n)]
    count = 0
    while True:
        matrix[y][x] = count
        count+=1
        new_dx, new_dy = turn_right[dx,dy]
		new_x = x + new_dx 
		new_y = y + new_dy
		if (0 <= new_x < n and 0 <= new_y < n and
			matrix[new_y][new_x] is None):
			x = new_x 
			y = new_y
			dx  = new_dx
			dy = new_dy
		else:
			x = x + dx 
			y = y + dy
			if not (0 <= x < n and 0 <= y < n):
				return matrix