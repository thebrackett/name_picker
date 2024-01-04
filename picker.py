import random
import csv
import argparse
import time
import sys
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show one or all at once.")

# read arguments from command line
args = parser.parse_args()

# assign to var for readability
output_style = args.Output

# read csv and return as list
def readCSV():
	# init team var
	team = []

	# read csv and load into team
	with open('names.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			team.append(row['first_name'])
	return team

# randomize list and return it
def randomizeList(source):
	# init destination list
	dest = []

	# store count participants
	team_count = len(source)

	# iterate through and build randomized list
	for t in range(team_count):
		# pick one at random
		r = random.randrange(0, len(source))
	
		# add to destination randomized list
		dest.append(source[r])
	
		# remove from source list
		source.remove(source[r])
		
	# return randomize list
	return dest

# print one letter at a time
def typePrint(text):
	for t in text:
		sys.stdout.write(t)
		sys.stdout.flush()
		time.sleep(.07*random.randrange(0,5))


# print each name to screen
def printAll(output):
	for o in output:
		print(f'- {o}')

# print one at a time
def printOne(output):
	for o in output:
		typePrint(o)
		input(' ')	
	print("That's everyone!\n")

# greeting
print(f'howdy! Today it\'s:\n{"-"*10}')

# load list of participants
team = readCSV()

# create randomized list
rand_team = randomizeList(team)

# output new list
if(output_style == "one"):
	printOne(rand_team)
else:
	printAll(rand_team)



