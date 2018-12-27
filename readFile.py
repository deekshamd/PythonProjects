input_file = open("data.txt","r")
firstNames = list()
lastNames = list()
grades = list()
ages = list()
for i in range(0,10):
	sentence = input_file.readline()
	senList = sentence.split()
	firstNames[i] = senList[0];
	lastNames[i] = senList[1];
	grades[i] = senList[2];
	ages[i] = senList[3];
