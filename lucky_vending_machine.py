#importing randint from random module
from random import randint
#defining a variable new_player
new_player = None
 
class Player(object):
	"""Create a new player"""
 	def __init__(self, name, prize = "", worth = 0, spent = 0):
 		"""Initialize the Player class

 		Keyword arguments:
 		self -- instance reference
 		name -- user input for player name
 		prize -- prizes user have won(default "")
 		worth -- total prize worth(default 0)
 		spent -- total money spent by user(default 0)
 		"""
		self.name = name
		self.prize = prize
		self.worth = worth
		self.spent = spent
		print "\nHello", self.name, '\n'

class LuckyGuessGenerator(object):
	"""Create a random number and return it"""
	def rand_gen(self):
		"""Genrate a random number and return it

		Keyword arguments:
		self -- instance reference
		"""
		return randint(1, 5)

class Game(object):
	"""Display menu to user and react to the user response"""
	choice = 1
	while choice != 5:

		print 'Welcome to the Lucky Vending Machine'
		print '=' * 38
		print '(1) Set Up New Player'
		print '(2) Guess A Prize'
		print '(3) What Have I Won So Far?'
		print '(4) Display Game Help'
		print '(5) Exit Game\n'

		choice = int(raw_input('Choose an option: ')) #Take user input

		if choice == 1:
			user_name = raw_input("Please enter player's name: ")
			if user_name.strip(): #Handle blank name case
				new_player = Player(user_name) #Create a Player() class instance
			else:
				print '\n',"*" * 26 
				print "Player name can't be blank"
				print "*" * 26, '\n'
 		
 		elif choice == 2:
 			if new_player is not None: #Handle case if no player exist or have been created
	 			rand_num = LuckyGuessGenerator().rand_gen()  #Create a LuckyGuessGenerator() class instance
	 			prize_list = [['Pen ', 10, 1], ['Book ', 20, 2], ['DVD ', 30, 3], ['Mouse ', 40, 4], ['Keyboard ', 50, 5]]
	 			user_guess = int(raw_input("Please Guess a Number: ")) #Ask user to guess a number

	 			if user_guess == rand_num: 
	 				print '\n',"*" * 30
	 				print "Congrats! You Won a:", prize_list[rand_num - 1][0],'\n'
	 				print "*" * 30, '\n'
					new_player.prize += prize_list[rand_num - 1][0] #Update new_player's stats i.e Prizes won, Total worth, Money spent
					new_player.worth += prize_list[rand_num - 1][1]
					new_player.spent += prize_list[rand_num - 1][2]
	 			else:
	 				print "\nSorry! You Lost."
	 				print 'Game\'s random number was:',rand_num,'\n'
			else:
				print "\nFirst you need to set up a player !\n"

		elif choice == 3:
			if new_player is not None:
				print "*" * 50
				print 'You have won so far :-> ',new_player.prize  #Display player's stats i.e Prizes won, Total worth, Money spent
				print 'Total worth of prizes :-> ',new_player.worth,'$'
				print 'And you just spent :-> ',new_player.spent,'$'
				print "*" * 50, '\n'
			else:
				print "\nFirst you need to set up a player !\n"
		elif choice == 4: #Help 
			print 'Lucky Vending Machine is a place to try your luck!'
			print 'You just have to set up a player and play the game.'
			print 'Further,you just have to guess a number'
			print 'which should match with computer\'s random genrated number.'
			print 'if your guess is right you will win Prize, but if you loose your money is not yours anymore.'
			print 'so let\'s begin ... Have Fun!'
		elif choice == 5: #User Exit
			print '\nSee You Soon!'
			break
		else: #Handle invalid choice case
			print '\n',"*" * 26
			print "Your choice is not valid !"
			print "Look what you wish for :)"
			print "*" * 26, '\n'




if __name__ == '__main__':

	new_game = Game()