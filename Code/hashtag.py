import re
import csv
excl = {}
with open ("timoreilly_tweets.csv", "r") as myfile:
    data=myfile.read().replace('\n', '')
    #print re.findall(r"#(\w+)", data)
f = open('tp.csv', "wb")
exclude = open('exclusion.csv','r')
csvex = csv.reader(exclude,delimiter='\t')

for i in data.split():
	if i.startswith("#"):
		if not excl.has_key(i):			
				f.write('%s\n' % i)
				excl[i] = 1
		
