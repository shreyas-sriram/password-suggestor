import itertools
import pyfiglet
import signal
import sys
from random import randint
from zxcvbn import zxcvbn


'''

---- References ----
https://medium.com/@mohammedijas/the-art-of-creating-a-strong-password-61d4c2feb14f
https://xato.net/the-worst-password-tips-3466ff964b45
https://www.passworddog.com/
https://suratiundhiyu.files.wordpress.com/2011/02/1000-english-proverbs.pdf
https://tools.fromdev.com/memorable-secure-password-generator.html
https://www.rempe.us/diceware/#eff
https://github.com/redacted/XKCD-password-generator
https://github.com/beala/xkcd-password
https://xkcd.com/936/
https://github.com/dropbox/zxcvbn
https://pypi.org/project/zxcvbn/
https://suratiundhiyu.files.wordpress.com/2011/02/1000-english-proverbs.pdf
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt


'''

'''

End-goal : [user word][separator][abbreviated proverb][separator][user word][separator][random word generated]

'''



separator = ['-','.']

substituition = {
				'not': '!',
				'why': 'Y',
				'a': '@',
				'e': '3',
				'i': '!',
				'o': '0',
				'at': '@',
				'to': '2',
				'l': '/',
				's': '$'
				}

header = [
			'Password with lower case characters',
			'Password with upper case and lower case characters',
			'Password with upper case, lower case and special characters'
		 ]


def handler(signum, frame):
    print('\n\033[33m Goodbye!\033[0m')
    sys.exit(0)


def getRandomWord() :
	f = open('wordlist.txt','r')
	wordlistLinesList = f.read().split('\n')

	randomIndex = randint(0,len(wordlistLinesList)-1)

	word = wordlistLinesList[randomIndex]

	f.close()
	
	return word


def abbreviatedProverbs() :
	print('-------------- List of proverbs --------------')
	print('\n')

	
	# Read and print the proverb list. Also get the user choice.
	f = open('proverbs3.txt','r')
	proverbsLinesList = f.read().split('\n')
	for index, proverb in enumerate(proverbsLinesList) :
		print('\033[32m [{}]\033[0m {}'.format(index+1,proverb))

	while (True):
		choice = int(input('\n\033[31m Choose a proverb from the above list : \033[0m'))
		if (choice > 0 and choice <= len(proverbsLinesList)) :
			break
		else :
			print('\033[31m Please enter a valid option!\033[0m')

	proverb = proverbsLinesList[choice-1]

	# print('\nThe option you chose is : {}'.format(proverb))

	f.close()

	# Find the abrreviated form.
	password = proverb[0].lower()
	for i in range(len(proverb)-1) :
		if(proverb[i] == ' ') :
			password += proverb[i+1]

	return password


def makeSubstitutions(password = None) :
	passwords = []
	allPositions = []

	# if not word :
	# 	word = input('Enter a password : ').lower()
	
	# passwords.append(password)

	for i in substituition.keys() :
		allPositions.clear() # reset list
		for j in range(len(password)) : # iterate through the password
			pos = password.find(i,j) # find occurances
			if (pos != -1) and (pos not in allPositions) : # add to list only if found and not already on the list
				allPositions.append(pos)
		
		if allPositions :
			if len(allPositions) > 1 :
				randomPosition = randint(0,len(allPositions)-1) # find random position to replace from all positions
			else :
				randomPosition = 0
			# print("All positions: ",allPositions)
			# print("Random position: ",randomPosition)
			# print(password[:allPositions[randomPosition]] + substituition[i] + password[allPositions[randomPosition]+len(i):])
			passwords.append(password[:allPositions[randomPosition]] + substituition[i] + password[allPositions[randomPosition]+len(i):]) # substituting the character/phrase

			break # stops when one trivial substitution is made

	return passwords[0] # send only one password


def makeUpperCase(password) :
	while(True) :
		randomIndex = randint(0,len(password)-1)
		if(password[randomIndex].islower()) :
			password = password[:randomIndex] + password[randomIndex].upper() + password[randomIndex+1:]
			break

	return password

def combineWords() :
	words = []
	wordsReplacedList = []
	passwords = []

	print('\033[32m Enter two words which you can remember easily \033[0m')
	print('-----------------------------------------------')
	
	# Get words from user
	for i in range(2):
		words.append(input('\033[31m Enter word {}: \033[0m'.format(i+1)))

	print('\n')


	# Get random word from worlist
	words.append(getRandomWord())

	# Get proverb
	words.append(abbreviatedProverbs())

	# Find all permutations of the 4 words and choose and random permutation
	permuteList = list(itertools.permutations(words))
	permuteIndex = randint(0,len(permuteList)-1)

	separatorIndex = randint(0,len(separator)-1)
	passwords.append(separator[separatorIndex].join(permuteList[permuteIndex]))

	# Include upper case
	for i in range(len(passwords)) :
		passwords.append(makeUpperCase(passwords[i]))

	# Include trivially substituted characters
	passwords.append(makeSubstitutions(passwords[1]))
	
	return passwords


if __name__ == '__main__' :

	# Handle KeyboardInterrupt
	signal.signal(signal.SIGINT, handler)

	print('\n')
	print('\033[36m-------------------------------------------------------\033[0m')
	# banner = pyfiglet.figlet_format("Password Suggestor")
	# print(banner)
	print('\033[36m                  Password Suggestor                   \033[0m')
	print('\033[36m-------------------------------------------------------\033[0m')
	print('\n')
	
	'''

	while (True) :

		print('Choose an option from below')
		print('---------------------------')
		print('\n')
		print('[1] Password based on 2 words (winner-winner-chicken-dinner)')
		print('[2] Password based on single word (hello -> h3ll0)')
		print('[3] Password based on a proverb (Experience is the mother of wisdom -> eitmow)')
		
		option = int(input('\nChoose a method from the above list : '))
		print('\n')
		
		if (option == 1) :
			passwords = combineWords()
			break
		
		elif (option == 2) :
			passwords = makeSubstitutions()
			break
		
		elif (option == 3) :
			passwords = abbreviatedProverbs()
			break
		
		else :
			print('Please enter a valid option!')
		
	'''

	passwords = combineWords()

	print('\n')
	print('\033[36m -------------- Password suggestions -------------- \033[0m')
	print('\n')
	
	# print(*passwords, sep='\n')
	for i in range(len(passwords)) :
		zxcvbnOutput = zxcvbn(passwords[i])
		print('\033[32m [{}] {}\033[0m'.format(i+1,header[i]))
		print('------------------------------------------------------------------')
		print('\n')
		print(' password : \033[32m {} \033[0m'.format(passwords[i]))
		print('\n')
		print(('\t Slow online cracking : {}'.format(zxcvbnOutput['crack_times_display']['online_throttling_100_per_hour'])))
		print(('\t Fast online cracking : {}'.format(zxcvbnOutput['crack_times_display']['online_no_throttling_10_per_second'])))
		print(('\t Slow offline cracking : {}'.format(zxcvbnOutput['crack_times_display']['offline_slow_hashing_1e4_per_second'])))
		print(('\t Fast offline cracking : {}'.format(zxcvbnOutput['crack_times_display']['offline_fast_hashing_1e10_per_second'])))
		print('\n')

	print('\n')
	print('--------------------------------------------------')
	print('\n')
