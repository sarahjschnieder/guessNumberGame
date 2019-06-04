import random

random_number = random.randint(1,10)


# while guess != random_number:
# 	guess = input("Pick a number between 1 and 10: ")
# 	guess = int(guess)
# 	if guess < random_number:
# 		print("You're too low! ")	
# 	elif guess > random_number: 
# 		print("You're too high! ")	
# 	else:
# 		print("You won!!! ")	

# print(random_number)


while True:
	guess = input("Pick a number between 1 and 10: ")
	guess = int(guess)
	if guess < random_number:
		print("You're too low! ")	
	elif guess > random_number: 
		print("You're too high! ")	
	else:
		print("You won!!! ")
		play_again = input("Do you want to play again? (y/n) ")	
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing! ")
			break	


print(random_number)