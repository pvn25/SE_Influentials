import heapq
import csv
import operator

h = []


arr = ['following/Eleni_Stroulia.csv','following/victorguana.csv','following/Felienne.csv','following/avandeursen.csv','following/icse2015.csv']
f = open('following/top19.csv', "wb")
for i in range (len(arr)):
	fname = arr[i]
	sample = open(fname,'r')
	csv1 = csv.reader(sample,delimiter='\t')
	for row in csv1:
		heapq.heappush(h,(-(int(row[3])),row[1]))
	sample.close()

for x in range(0,145):
	heapq.heappop(h)

for x in range(0,55):
	p = heapq.heappop(h)
	params = (p[1],-p[0])
	f.write('%s\t%s\n' % params)



f.close()


