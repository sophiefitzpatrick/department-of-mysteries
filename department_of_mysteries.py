import sys
from termcolor import colored, cprint
import time
import constants as narrative

quit = {"quit", "exit", "q", "stop"}
yes = {"yes","y", "ye", "yep"}
no = {"no","n", "nope", "nah"}
back = {"flee", "run", "leave", "stop"}
forward = {"continue", "forward", "go", "move"}

def welcome():
	print(colored(narrative.WELCOME_MESSAGE, "cyan"))
	time.sleep(3)
	print(colored(narrative.WELCOME_MESSAGE_2, "cyan"))
	time.sleep(3)
	print(colored(narrative.WELCOME_MESSAGE_3, "cyan"))
	answer = input(narrative.CONTINUE).lower()
	for x in answer:
		if answer in yes:
			continue
		elif answer in no:
			sys.exit(colored(narrative.EXIT_CHOICE, "yellow"))
		else:
			answer = input(narrative.CONTINUE).lower()
	return answer

def character():
	print(colored(narrative.CHARACTER_NARRATIVE_1, "cyan"))
	code = input("Pick up the reciever and dial 62442: ")
	if code == "62442":
		print(colored(narrative.CHARACTER_NARRATIVE_2, "magenta"))
	elif code in quit:
		sys.exit(colored(narrative.EXIT_CHOICE, "yellow"))
	else:
		code = input("Pick up the reciever and dial 62442: ")
	character_name = input(narrative.CHARACTER_NARRATIVE_NAME)
	print(colored(narrative.CHARACTER_NARRATIVE_3 % (character_name), "magenta"))
	time.sleep(1)
	print(colored(narrative.CHARACTER_NARRATIVE_4, "cyan"))
	return character_name

def atrium():
	print(colored(narrative.ATRIUM_NARRATIVE_1, "cyan"))
	time.sleep(2)
	print(colored(narrative.ATRIUM_NARRATIVE_2, "magenta"))
	print(colored(narrative.ATRIUM_NARRATIVE_3, "cyan"))
	level = input(narrative.INPUT_LEVEL)
	for x in level:
		if "1" in level:
			print(colored(narrative.LEVEL_1, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "2" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "3" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "4" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "5" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "6" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "7" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "9" in level:
			print(colored(narrative.LEVEL_2, "magenta"))
			level = input(narrative.INPUT_LEVEL)
		elif "8" in level: 
			continue
		elif level in quit:
			sys.exit(colored(narrative.EXIT_CHOICE, "yellow"))
		else:
			level = input(narrative.INPUT_LEVEL)
	print(colored(narrative.LEVEL_8, "magenta"))
	return level

def corridor():
	print(colored(narrative.CORRIDOR_NARRATIVE_1, "cyan"))
	action = input(narrative.CORRIDOR_NARRATIVE_2).lower()
	for x in action:
		if action in back:
			answer = input(narrative.QUIT).lower()
			if answer in yes:
				sys.exit(colored(narrative.EXIT_CHOICE, "yellow"))
			elif answer in no:
				action = input(narrative.CORRIDOR_NARRATIVE_4).lower()
			else:
				action = input(narrative.CORRIDOR_NARRATIVE_4).lower()
		elif action in forward:
			continue
		else:
			action = input(narrative.CORRIDOR_NARRATIVE_4).lower()
	print(colored(narrative.CORRIDOR_NARRATIVE_3, "cyan"))
	return action

def entrance_hall():
	print(colored(narrative.ENTRANCE_HALL_1, "cyan"))
	doors = input(narrative.ENTRANCE_HALL_2)
	for door in doors:
		if "1" in doors:
			continue
		elif "2" in doors:
			continue
		elif "3" in doors:
			continue
		elif "4" in doors:
			continue
		elif "5" in doors:
			continue
		else:
			doors = input(narrative.ENTRANCE_HALL_2)
	return door
	





