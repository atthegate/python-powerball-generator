import sys
import random

# Get arguments
args = sys.argv
 
# args[1] : lotteryType : "powerball" or "megamillions"
# args[2] : seed : "any-string"

# Lottery Number Generator
def getLotteryNumbers(lotteryType, seed):

	if lotteryType == "powerball":
		num_numbers = 5
		num_bonus = 1
		numbers_range = [1,69]
		bonus_range = [1,26]
	elif lotteryType == "megamillions":
		num_numbers = 5
		num_bonus = 1
		numbers_range = [1,70]
		bonus_range = [1,25]
	else:
		print "Lottery type not recognized!"
		return 

	random.seed(seed)

	# White Balls (WB)
	numbers = []

	# Generate Numbers
	while len(numbers) < num_numbers:
		r = random.randint(numbers_range[0],numbers_range[1])
		if r not in numbers:
			numbers.append(r)

		numbers.sort()

	# Generate Bonus
	while len(numbers) < (num_numbers + num_bonus):
		numbers.append(random.randint(bonus_range[0],bonus_range[1]))

	# Power Ball String Format >>> WB1-WB2-WB3-WB4-WB5:RPB
	o_numbers = '-'.join(map(str,numbers)[0:num_numbers]) + ' : ' + str(numbers[-1])

	output = {
		'seed': seed,
		'numbers': o_numbers
	}
	
	return output

#################################################

# Get Power Ball and print result
if len(args) == 3:
	lotteryType = args[1]
	seed = args[2]
	o_gpbn = getLotteryNumbers(lotteryType,seed)
	print "Numbers: " + o_gpbn['numbers']
	print "Seed: " + o_gpbn['seed']
else:
	print "Please provide two (2) arguments: a lottery type and a seed!"