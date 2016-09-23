# Edmond Lam and Henry Zhang
# SoftDev1 pd8
# HW#01 -- Divine Your Destiny
# 2016-09-15

import random
import io
import csv

def calc():
    f=open('occupations.csv', 'r')
    file=f.read();
    lines=file.splitlines()
    del lines[0]
    #deletes first line
    prob={}
    for n in  csv.reader(lines, quotechar='"', delimiter=',',
        quoting=csv.QUOTE_ALL, skipinitialspace=True):
        a=n[0]
        b=float(n[1])
        prob[a]=b
        #ignores comma in quotations and creates the dictionary
    sorted(prob.keys())
    #sorts dict by value in ascending order
    return prob


def randOcc(prob):
	rand=random.randrange(0,998)
	counter=0
	for key, value in prob.iteritems():
		counter+=value*10
		#add by ascending numbers for ranges of probability
		if (rand<counter):
			return key
	return "None"

print randOcc(calc())
