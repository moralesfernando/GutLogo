import csv
import numpy
import sys

def mean(lst):
# calculates the mean of a list
	return numpy.mean(numpy.array(lst))

def stddev(lst):
# calculates stddev of a list
	return numpy.std(numpy.array(lst))

def median(lst):
# calculates the median of a list
	return numpy.median(numpy.array(lst))
	
filename = str(sys.argv[1])
with open(filename, 'rb') as csvfile:
	#opens csv file and makes dict reader
	reader = csv.DictReader(csvfile)
	dataList = list(reader)

#list of entries to avg and format
entryList = ['count closts', 'count bifidos', 'count bacteroides', 'count desulfos','glucose','lactose',
'inulin','lactose','CS','FO','trueAbsorption']

testSet = set()
stepSet = set()
for row in dataList:
	#check number of testConstants
	testSet.add(float(row['testConst']))
	stepSet.add(float(row['[step]']))
	
testList = list()
# create the list-tree data structure
for i in range(len(testSet)):
	testList.append(list())
	for j in range(len(stepSet)):
		testList[i].append(list())
		for k in range(len(entryList)):
			testList[i][j].append(list())

# make the sets into sorted lists
testSorted = sorted(testSet)
stepSorted = sorted(stepSet)

for data in dataList:
# put the data into the dataList
	i = testSorted.index(float(data['testConst']))
	j = stepSorted.index(float(data['[step]']))
	for k in range(len(entryList)):
		testList[i][j][k].append(float(data[entryList[k]]))

with open('csvData.csv', 'w+') as file:
# get the mean, stddev, median, and write to a csv file
	rowData = list()
	datawriter = csv.writer(file, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	rowData.append('testConst')
	rowData.append('step')
	for entry in entryList:
		rowData.append('avg ' + entry)
		rowData.append('std ' + entry)
		rowData.append('median ' + entry)
	datawriter.writerow(rowData)
	rowData = list()
	for x in range(0, len(testList)):
		for y in range(0, len(testList[x])):
			rowData.append(testSorted[x])
			rowData.append(stepSorted[y])
			for z in range(len(entryList)):
				rowData.append(mean(testList[x][y][z]))
				rowData.append(stddev(testList[x][y][z]))
				rowData.append(median(testList[x][y][z]))
			datawriter.writerow(rowData)
			rowData = list()
			
