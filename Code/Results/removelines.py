import pandas as pd

mat = pd.read_csv("createdat.csv", header=None, delim_whitespace=True)

for i in range(0,200):	
	print mat[0][i]
