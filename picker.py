import random

# greeting
print("howdy. let's get started")

# read list of participants
team = [ 'scott', 'jim', 'allison']

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

print(rand_team)



# type name letter by letter

# ask user if theyd like
# to pick again


