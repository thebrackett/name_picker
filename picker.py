import random
import csv
import argparse
import time
import sys
from math import floor

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Enter 'one' to set output to one at a time, or 'all' to print all names at once.")

# Adding optional team argument
parser.add_argument("-t", "--TeamSize", help = "int size to divide teams into")

# read arguments from command line
args = parser.parse_args()

# assign output style arg to var
output_style = args.Output

# assign team size arg to var
team_size = int(args.TeamSize)

# read csv and return as list
def readCSV():
	# init team var
	team = []

	# read csv and load into team
	with open('names.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			team.append(f"{row['first_name']} {row['last_name']}")
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
	print(f"That's everyone!\n")

# greeting
print(f'howdy! Today it\'s:\n{"-"*10}')

# load list of participants
team = readCSV()

# create randomized list
rand_team = randomizeList(team)

# create groups and return list of
# defined group size
def createTeams(team, size):
    # take provided size and list of strings
    # break up into a list of lists
    num_groups = floor(len(team)/size)

    new_teams = []
    start = 0
    end = size

    for i in range(0, num_groups):
        new_team = team[start:end]
        new_teams.append(new_team)
        start = start + size
        end = end + size

    return new_teams

# define function to create groups
# and print to screen
def printTeams(output, team_size):
    # get list of lists
    new_team = createTeams(output, team_size)
    
    # initialize counter 
    num = 0
    # iterate through list and print each team
    # to console
    for t in new_team:
        # increment iteration count 
        num = num + 1
        # print team heading
        print(f"\nteam:{num}\n")
        
        # print each member
        for member in t:
            typePrint(member)
            print("\n")
        print('===================')

    print('\n')

# output new list
if(output_style == "one"):
	printOne(rand_team)
elif(output_style == "team"):
    printTeams(rand_team, team_size)
else:
	printAll(rand_team)



