import random
import csv

# greeting
print("howdy. let's get started")

# read list of participants
team = []

team = readCSV()

# store count participants
team_count = len(team)

#init random team container
rand_team = []

# load randomized data
for t in range(team_count):
	# pick one at random
	r = random.randrange(0, len(team))

	# add to randomized list
	rand_team.append(team[r])

	# remove from source list
	team.remove(team[r])

# output new list
print(rand_team)

def readCSV():
	team = []

	# read csv and load into team
	with open('names.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			team.append(row['first_name'])
	return team

# type name letter by letter

# ask user if theyd like
# to pick again

