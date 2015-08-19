import argparse
import operator
import csv			    
  
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fnames", required=True, help="")
    args = vars(ap.parse_args())

    fname = args['fnames']
    sample = open(fname,'r')
    csv1 = csv.reader(sample,delimiter='\t')
    sort = sorted(csv1,key = lambda row: float(row[1]),reverse = True)	   
	         	    #print friendids[3]
    sample.close()
    f = open(fname, "wb")
    fileWriter = csv.writer(f, delimiter='\t')
    for row in sort:
    	fileWriter.writerow(row)
    f.close()
