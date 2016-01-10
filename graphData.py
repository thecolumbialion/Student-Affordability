# The Lion Data Analytics 
# Student Affordability Project

from bokeh.plotting import *
import numpy
from os import mkdir
from os.path import exists, expanduser, isdir, join
import csv

# loads and cleans data 
def get_data(filename): 
	with open('./data/'+filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(row[1])

get_data("researchData.csv")

# creates new plot
def visualize(): 
	print("buffer")


def aid_per_stud(totalAid, undPop):
	perStud = totalAid / undPop
	

# shows results 
def show_results(p):
	show(p)
