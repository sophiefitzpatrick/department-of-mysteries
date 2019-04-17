import sys
from termcolor import colored, cprint
import time
from narratives import (
	welcome_narrative,
	brain_narrative,
	welcome_narrative,
	character_narrative,
	corridor_narrative,
	entrance_hall_narrative,
	atrium_narrative,
	love_narrative
	)
	

quit = {"quit", "exit", "q", "stop"}
yes = {"yes","y", "ye", "yep"}
no = {"no","n", "nope", "nah"}
back = {"flee", "run", "leave", "stop"}
forward = {"continue", "forward", "go", "move"}
unlock_incantation = "alohomora"

def welcome():
	print(colored(welcome_narrative.WELCOME_MESSAGE, "cyan"))
	time.sleep(3)
	print(colored(welcome_narrative.WELCOME_MESSAGE_2, "cyan"))
	time.sleep(3)
	print(colored(welcome_narrative.WELCOME_MESSAGE_3, "cyan"))
	continue_inputs = input(welcome_narrative.CONTINUE_INPUT).lower()
	for continue_input in continue_inputs:
		if continue_inputs in yes:
			continue
		elif continue_inputs in no:
			sys.exit(colored(welcome_welcome_narrative.EXIT_CHOICE, "yellow"))
		else:
			continue_inputs = input(welcome_narrative.CONTINUE_INPUT).lower()

def character():
	print(colored(character_narrative.LONDON_PHONEBOX, "cyan"))
	dial_code = input(character_narrative.DIAL_CODE_INPUT)
	if dial_code == "62442":
		print(colored(character_narrative.WELCOME_MINISTRY, "cyan"))
	elif dial_code in quit:
		sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
	else:
		dial_code = input(character_narrative.DIAL_CODE_INPUT)
	character_name = input(character_narrative.CHARACTER_NAME_INPUT)
	print(colored(character_narrative.MINISTRY_BADGE % (character_name), "cyan"))
	return character_name

def atrium():
	print(colored(atrium_narrative.ATRIUM_DESCRIPTION, "cyan"))
	time.sleep(2)
	level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
	for level_choice in level_choices:
		if "1" in level_choices:
			print(colored(atrium_narrative.LEVEL_1, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "2" in level_choices:
			print(colored(atrium_narrative.LEVEL_2, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "3" in level_choices:
			print(colored(atrium_narrative.LEVEL_3, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "4" in level_choices:
			print(colored(atrium_narrative.LEVEL_4, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "5" in level_choices:
			print(colored(atrium_narrative.LEVEL_5, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "6" in level_choices:
			print(colored(atrium_narrative.LEVEL_6, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "7" in level_choices:
			print(colored(atrium_narrative.LEVEL_7, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "9" in level_choices:
			print(colored(atrium_narrative.LEVEL_9, "cyan"))
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
		elif "8" in level_choices: 
			continue
		elif level_choices in quit:
			sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
		else:
			level_choices = input(atrium_narrative.MOM_LEVEL_INPUT)
	print(colored(atrium_narrative.LEVEL_8, "cyan"))
	return level_choices

def corridor():
	print(colored(corridor_narrative.CORRIDOR_VIBE, "cyan"))
	corridor_choices = input(corridor_narrative.CORRIDOR_CHOICE_INPUT).lower()
	for corridor_choice in corridor_choices:
		if corridor_choices in back:
			exit_question = input(corridor_narrative.QUIT).lower()
			if exit_question in yes:
				sys.exit(colored(corridor_welcome_narrative.EXIT_CHOICE, "yellow"))
			elif exit_question in no:
				corridor_choices = input(corridor_narrative.CORRIDOR_CHOICE_WRONG_INPUT).lower()
			else:
				corridor_choices = input(corridor_narrative.CORRIDOR_CHOICE_WRONG_INPUT).lower()
		elif corridor_choices in forward:
			continue
		else:
			corridor_choices = input(corridor_narrative.CORRIDOR_CHOICE_WRONG_INPUT).lower()
	print(colored(corridor_narrative.DOM_DOOR, "cyan"))

def entrance_hall_desc():
	print(colored(entrance_hall_narrative.ENTRANCE_HALL_DESCRIPTION, "cyan"))
	
def entrance_hall():
	entrance_hall_doors = input(entrance_hall_narrative.CHOOSE_DOOR_INPUT)
	for entrance_hall_door in entrance_hall_doors:
		if "1" in entrance_hall_doors:
			brains_room()
		elif "2" in entrance_hall_doors:
			love_room()
		elif "3" in entrance_hall_doors:
			continue
		elif "4" in entrance_hall_doors:
			continue
		elif "5" in entrance_hall_doors:
			continue
		else:
			entrance_hall_doors = input(entrance_hall_narrative.CHOOSE_DOOR_INPUT)

def entrance_hall_return():
	print(colored(entrance_hall_narrative.RETURN_MARK_DOOR, "cyan"))
	symbol = input(entrance_hall_narrative.SYMBOL_INPUT)
	if symbol != None:
		print(colored(entrance_hall_narrative.RETURN_ROTATING_ROOM, "cyan"))
		entrance_hall()
	else:
		symbol = input(entrance_hall_narrative.SYMBOL_INPUT)
	
def brains_room():
	print(colored(brain_narrative.ALOHOMORA_CANTATION, "cyan"))
	alohomora_incantations = input(brain_narrative.SPELL_INPUT).lower()
	for alohomora_incantation in alohomora_incantations:
		if alohomora_incantations == unlock_incantation:
			continue
		else:
			alohomora_incantations = input(brain_narrative.ALOHOMORA_WRONG_INPUT).lower()
	print(colored(brain_narrative.DESCRIPTION_BRAIN_ROOM, "cyan"))
	brain_explore_choices = input(brain_narrative.EXPLORE_CHOICE_INPUT).lower()
	move_forward = {"tank", "explore", "continue", "forwards"}
	move_backward = {"leave", "retreat", "run", "escape", "backwards"}
	for brain_explore_choice in brain_explore_choices:
		if brain_explore_choices in move_forward:
			continue
		elif brain_explore_choices in move_backward:
			entrance_hall_return()
		else:
			choices = input(brain_narrative.EXPLORE_CHOICE_WRONG_INPUT).lower()
	print(colored(brain_narrative.BRAINS_WINGARDIUM_LEVIOSA, "cyan"))
	wingardium_leviosa_incantations = input(brain_narrative.SPELL_INPUT).lower()
	for wingardium_leviosa_incantation in wingardium_leviosa_incantations:
		if "wingardium leviosa" in wingardium_leviosa_incantations:
			continue
		else:
			wingardium_leviosa_incantations = input(brain_narrative.WINGARDIUM_LEVIOSA_WRONG_INPUT).lower()
	print(colored(brain_narrative.BRAINS_ACCIO, "cyan"))
	accio_incantations = input(brain_narrative.ACCIO_INPUT).lower()
	accio = "accio"
	no_accio = {"lower", "drop", "sink"}
	for accio_incantation in accio_incantations:
		if accio_incantations in accio:
			continue
		elif accio_incantations in no_accio:
			print(colored(brain_narrative.NO_ACCIO, "cyan"))
			entrance_hall_return()
	print(colored(brain_narrative.BRAINS_DIFFINDO, "cyan"))
	diffindo_incantation = input(brain_narrative.SPELL_INPUT).lower()
	if "diffindo" in diffindo_incantation:
		print(colored(brain_narrative.BRAINS_SURVIVED, "cyan"))
		entrance_hall_return()
	else:
		print(colored(brain_narrative.BRAINS_DIED, "cyan"))
		time.sleep(5)
		sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))

def love_room():
	print(colored(brain_narrative.ALOHOMORA_CANTATION, "cyan"))
	alohomora_incantations = input(brain_narrative.SPELL_INPUT).lower()
	print(colored(love_narrative.LOVE_DESCRIPTION, "cyan"))
	symbol = input(entrance_hall_narrative.SYMBOL_INPUT)
	if symbol != None:
		print(colored(entrance_hall_narrative.RETURN_ROTATING_ROOM, "cyan"))
		entrance_hall()
	else:
		symbol = input(entrance_hall_narrative.SYMBOL_INPUT)





		









