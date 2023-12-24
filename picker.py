import random
import csv

# define functions
def readCSV():
	team = []

	# read csv and load into team
	with open('names.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			team.append(row['first_name'])
	return team

def randomizeList(source,dest):
	# load randomized data
	for t in range(team_count):
		# pick one at random
		r = random.randrange(0, len(team))
	
		# add to randomized list
		rand_team.append(team[r])
	
		# remove from source list
		team.remove(team[r])
		
	# return both source and destination
	return source, dest

# greeting
print("howdy. let's get started")

# read list of participants
team = []

team = readCSV()

# store count participants
team_count = len(team)

#init random team container
rand_team = []

team, rand_team = randomizeList(team, rand_team)

# output new list
print(rand_team)

# type name letter by letter

# ask user if theyd like
# to pick again

