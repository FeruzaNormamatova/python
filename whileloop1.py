#save file as whileloop1.py

d = 0 # d is the counter
while d < 101:
	squared = d*d
	print(d,squared," ", end="")
	d=d+1
	if(d % 5 == 0):
		print()
