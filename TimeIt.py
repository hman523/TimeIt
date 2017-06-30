#Author: Hunter Barbella (hman523)
#Date: 6/30/17
#Purpose: to time the runtime of a program and can output an average time
#for multiple runtimes
#This program comes with a licence. Please respect it

import argparse
from time import time
import subprocess

iterations = 10
command = "python primeNumberTest.py"

def getAverageTime(currentAverage, newValue, totalNumOfValues):
	temp = currentAverage * (totalNumOfValues - 1)
	temp += newValue
	return (temp / totalNumOfValues)
	
def callBashCommand(myCommand):
	commandsList = myCommand.split()
	subprocess.call(commandsList)


#TODO add args parser
def main():
	count = 1
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


if __name__ == '__main__':
	main()

