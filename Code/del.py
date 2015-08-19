import csv

table = {}
lat = open('record.csv','r')
csvlat = csv.reader(lat,delimiter='\t')

for row in csvlat:
	if not table.has_key(row[0]):
		table[row[0]] = row[3]
		#print row[0]


