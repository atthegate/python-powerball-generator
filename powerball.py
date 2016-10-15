import sys
import random

# Get arguments
args = sys.argv

# Power Ball Number Generator
def getPowerBallNumbers(seed):

	random.seed(seed)

	# White Balls (WB)
	numbers = []

	# Generate random white ball numbers
	while len(numbers) < 5:
		r = random.randrange(1,69)
		if r not in numbers:
			numbers.append(r)

		numbers.sort()

	# Red Power Ball (RPB)
	numbers.append(random.randrange(1,26))

	# Power Ball String Format >>> WB1-WB2-WB3-WB4-WB5:RPB
	o_numbers = '-'.join(map(str,numbers)[0:5]) + ' : ' + str(numbers[5])

	output = {
		'seed': seed,
		'numbers': o_numbers
	}
	
	return output

#################################################

# Get Power Ball and print result
if len(args) == 2:
	seed = args[1]
	o_gpbn = getPowerBallNumbers(seed)
	print "Powerball: " + o_gpbn['numbers']
	print "Seed: " + o_gpbn['seed']
else:
	print "Please provide only one (1) command line argument as a seed string!"