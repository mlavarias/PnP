#!/usr/bin/env python3

import creatures, random, sass, time, puzzles
from textFormat import print_s, input_s

# Shit I need for testing?
import user
#player = user.Prisoner(name = 'Jared', difficulty = 'easy') 

shark = creatures.Shark()

def shark_game(player):
	dice = random.randint(1,10)
	input_s("As you continue in your quest for the elusive Wizard and emerge onto the balcony, you encounter an escaped 'mythical' creature from the menagerie - the famous talking LandShark.", player)
	print(shark.art())
	time.sleep(2)
	input_s("The *clever* LandShark, having been on land for so long, has grown lungs and developed consumption (in addition to liver cirrhosis, for other reasons).", player)
	decision = input_s("Do you [jump over the shark] and risk infection or [go the long way] on your quest to the wizard?\n", user = player)

	while str(decision) not in ['jump over the shark', 'go the long way', 'riddle me']:
		decision = input_s(text=sass.sample_sass(), user = player, color="purple")

	if decision == "jump over the shark":
		if dice > 3:
			input_s("Damn, you just signed up for a lifetime of pain and suffering, lose 3 HP.", player)
			player.hp -= 3
		elif dice <= 3:
			input_s("You narrowly escaped, but why were you so foolish in the first place? Dumbass.", player)
			player.intelligence -= 2
			player.hp += 2
		
	elif decision == "go the long way":
		input_s("Someone knows what they're doing! Good job!", player)
		player.intelligence += 3
		input_s("Now you have to double back to the stairs to find an alternative route and encounter the legendary, award winning Milwaukee's Best (Monster).", player)
		print_s("To get past this monster, you must fight one of his (somewhat drunken) creatures.")
		time.sleep(2)
		animal = creatures.Animals()
		input_s("A wobbly " + animal.name + " stumbles down the stairs and attacks!\n", player)
		print(animal.art())
		player.combat(animal)
		if player.hp>0:
			input_s("I hope you're proud of your self, defeating a drunken " + animal.name + ". But you get to pass on to your greatest challenge yet. \n", player)
	elif decision == "riddle me":
		print_s("Congrats! *coughs violently* You have uncovered my hidden riddle!")
		my_puzzle = puzzles.Puzzles()
		puzzle_success = my_puzzle.do_puzzle(user = player)
	
		if puzzle_success == True:
			input_s("Great work! You completed my riddle and are richly rewarded.", player)
			player.intelligence += 3
			player.attack += 2
		
		elif puzzle_success == False:
			input_s("Drats, you failed. But (cough) have a free pass anyway.", player)
		
