#Author: Hunter Barbella (hman523)
#Date: 6/30/17
#Purpose: to time the runtime of a program and can output an average time
#for multiple runtimes
#This program comes with a licence. Please respect it


#Imports
import argparse
from time import time
import subprocess

#computes an average based on the current average
def getAverageTime(currentAverage, newValue, totalNumOfValues):
	temp = currentAverage * (totalNumOfValues - 1)
	temp += newValue
	return (temp / totalNumOfValues)

#calls the bash shell and enters a command
###WARNING DO NOT PUT ANYTHING DANGEROUS IN IT. YOUR SYSTEM WILL GET MESSED
###UP IF YOU ARE NOT CAREFUL
def callBashCommand(myCommand):
	commandsList = myCommand.split()
	subprocess.call(commandsList)


#Main method for connecting other methods
def main():
	count = 1
	parser = argparse.ArgumentParser(description="Times the runtime of a process")
	parser.add_argument('-c', dest='command', required=True)
	parser.add_argument('-i', dest='iterations', required=False)
	args = parser.parse_args()
	if args.command:
		command = str(args.command)
	if args.iterations:
		iterations = int(args.iterations)
	else:
		iterations = 1
	
	while(count <= iterations):
		startTime = time()
		callBashCommand(command)
		endTime = time()
		timeToRun = endTime - startTime
		if(count is 1):
			average = timeToRun
		else:
			average = getAverageTime(average, timeToRun, count)
		count +=1
	print("Average is " + str(average) + " after " + str(count-1) + " iterations")


#calls main method
if __name__ == '__main__':
	main()

