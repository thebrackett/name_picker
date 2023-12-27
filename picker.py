import random
import csv
import argparse
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show one or all at once.")

# Read arguments from command line
args = parser.parse_args()

output_style = args.Output

# define functions
def readCSV():
	# init team var
	team = []

	# read csv and load into team
	with open('names.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			team.append(row['first_name'])
	return team

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
		
	# return both source and destination
	return dest

# print to screen
def printAll(output):
	for o in output:
		print(f'- {o}')

# greeting
print(f'howdy! Today it\'s:\n{"-"*10}')

# load list of participants
team = readCSV()

# create randomized list
rand_team = randomizeList(team)

# output new list
if(output_style == "one"):
	print("next up... ")
	# TODO: pick one at a time
	# with pause and key press
	# to advance to next name
else:
	printAll(rand_team)

