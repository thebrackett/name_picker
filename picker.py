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

def randomizeList(source):

	# init destination list
	dest = []

	# store count participants
	team_count = len(source)
	
	for t in range(team_count):
		# pick one at random
		r = random.randrange(0, len(source))
	
		# add to destination randomized list
		dest.append(source[r])
	
		# remove from source list
		source.remove(source[r])
		
	# return both source and destination
	return dest

# greeting
print("howdy. let's get started")

# read list of participants
team = readCSV()

#randomize list
rand_team = randomizeList(team)

# output new list
print(rand_team)

# type name letter by letter

# ask user if theyd like
# to pick again

