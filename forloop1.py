# save file as forloop1.py
#encapsulation
print("DEX\tHEX\tBIN\tCHAR")
for d in range(32,128):
	h = hex(d)
	h = h.replace("Ox","$ ")
	b = bin(d)
	b = b.replace("Ob","- ")
	c = chr(d)
	# ~ print(str(d)+" "+h,end="")
	print(str(d)+"\t"+h+"\t"+b+"\t"+c)
# str(d)+"" is call concatination
# python3 "%f"
