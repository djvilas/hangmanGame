import os, getpass
clear = lambda: os.system('clear')
clear()
playing = 1
tries = 0
multip = 0
ll = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while playing == 1:
	fin = 0
	print("Hangman™\n")
	# word = input("Enter a word: ")
	word = getpass.getpass("Enter a word: ")
	word = word.capitalize().strip()
	clear()
	print("Hangman™\n")
	
	lives = 6
	s = "-" * len(word)
	letters = []
	i = 0
	while i < len(word):
		if word[i].upper() == " ":
			multip = 1
			s = s[:i]+" "+s[(i+1):]
		i += 1
	a = s
	for x in a:
		if x == " ":
			a = a.replace(x,"")	
	print("A word consisting of {} letters has been chosen. Good luck!".format(len(a)))	
	#while lives != 0 and s != word:
	while lives != 0 and "-" in s:
		print("Word: {}".format(s))
		letter = input("Pick a letter: ")
		while letter.upper() in letters or len(letter) != 1 or letter.upper() not in ll:
			letter = input("Pick a new letter: ")
		letters.append(letter.upper())
		if letter.upper() in word.upper():
			i = 0
			print("You gussed a correct letter!")
			while i < len(word):
				if word[i].upper() == letter.upper():
					s = s[:i]+letter.upper()+s[(i+1):]
				i += 1	
		else:
			lives -= 1
			print("Uh oh, wrong letter...\nYou have {} lives left.".format(lives))

	if lives == 0:
		clear()
		print("Hangman™\n")
		print("You suck, pleb.\nThe word was {}".format(word))
	else:
		clear()
		print("Hangman™\n")
		if multip != 1:
			print("Whoever picked that word, congratulations you played yourself. GG.\nThe word was {}".format(word))
		else:
			print("Whoever picked those words, congratulations you played yourself. GG.\nThe words were {}".format(word))	

	while fin == 0:	
		playing = input("Play again? Yes|No : ")
		if playing.lower() == "yes":
			fin = 1
			playing = 1
		elif playing.lower() != "yes" and playing.lower() != "no" :
			print("{} is not a valid option, dummy.".format(playing.strip()))
			tries += 1
			if tries == 3:
				clear()
				print("Hangman™\n")
				print("Think you're being funny, do ya?")
				playing = 0
				fin = 1

		else:
			playing = 0
			fin = 1
			clear()
			print("Hangman™\n")
			print("Whatever, never liked you anyway.")

		#How do I get rid of whitespace to the left of a string?



