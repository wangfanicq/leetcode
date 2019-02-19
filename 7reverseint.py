def reverseint(x):
	
	'''
	type x : int
	type return : int
	'''
	
	if x==0:
		return 0
	strx=str(x)
	newx=''
	if strx[0]=='-':
		newx+='-'
	newx+=strx[::-1].lstrip('0').rstrip('-')
	lastx=int(newx)
	if lastx>2**31-1 or lastx<(-2)**31:
		return 0
	else:
		return lastx
