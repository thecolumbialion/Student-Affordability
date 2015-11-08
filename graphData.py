# The Lion Data Analytics 
# Student Affordability Project

from bokeh.plotting import *
import numpy
from os import mkdir
from os.path import exists, expanduser, isdir, join

# loads and cleans data 
def get_data(filename): 
	with open('/data/'+filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

# creates new plot
def visualize(): 
	
# shows results 
def show_results(p):
	show(p)
