def panlindrome(x):
	'''
	type x : int
	type return : boolean
	'''
	strx=str(x)
	newx=strx[::-1]
	if strx==newx:
		return true
	else:
		return false
