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
	love_narrative,
	space_narrative,
	death_narrative,
	time_narrative,
	prophecy_narrative
	)


quit = {"quit", "exit", "q", "stop"}
yes = {"yes","y", "ye", "yep"}
no = {"no","n", "nope", "nah"}
back = {"flee", "run", "leave", "stop", "retreat", "back", "backwards", "b", "escape", "climb", "climb the stone steps"}
forward = {"continue", "forward", "go", "move", "explore", "forwards", "c", "walk", "walk through the veil", "walk through"}
unlock_incantation = "alohomora"
hello_answer = {"hello", "hi", "who\'s there?", "who\'s there"}

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
	character_name = input(character_narrative.CHARACTER_NAME_INPUT).upper()
	global character_age
	character_age = int(input(character_narrative.CHARACTER_AGE_INPUT))
	print(colored(character_narrative.MINISTRY_BADGE % (character_name), "cyan"))
	return character_age

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
			space_room()
		elif "4" in entrance_hall_doors:
			death_hall()
		elif "5" in entrance_hall_doors:
			time_room()
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
	alohomora()
	print(colored(brain_narrative.DESCRIPTION_BRAIN_ROOM, "cyan"))
	brain_explore_choices = input(brain_narrative.EXPLORE_CHOICE_INPUT).lower()
	for brain_explore_choice in brain_explore_choices:
		if brain_explore_choices in forward:
			continue
		elif brain_explore_choices in back:
			entrance_hall_return()
		else:
			brain_explore_choices = input(brain_narrative.EXPLORE_CHOICE_WRONG_INPUT).lower()
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

def alohomora():
	print(colored(brain_narrative.ALOHOMORA_CANTATION, "cyan"))
	alohomora_incantations = input(brain_narrative.SPELL_INPUT).lower()
	for alohomora_incantation in alohomora_incantations:
		if alohomora_incantations == unlock_incantation:
			continue
		else:
			alohomora_incantations = input(brain_narrative.ALOHOMORA_WRONG_INPUT).lower()

def space_room():
	alohomora()
	print(colored(space_narrative.DESCRIPTION_SPACE_ROOM, "cyan"))
	space_room_choices = input(space_narrative.FORWARD_BACK_INPUT).lower()
	for space_room_choice in space_room_choices:
		if space_room_choices in forward:
			continue
		elif space_room_choices in back:
			entrance_hall_return()
		else:
			choices = input(space_narrative.CHOICE_WRONG_PROMPT).lower()
	print(colored(space_narrative.PLANETS_DESCRIPTION, "cyan"))
	jupiter_moon_name = input(space_narrative.JUPITERS_MOONS_INPUT).lower()
	jupiter_moons = {"ganymede", "io", "europa", "callisto" }
	if jupiter_moon_name in jupiter_moons:
		print(colored(space_narrative.MOON_CORRECT, "cyan"))
	else:
		print(colored(space_narrative.MOON_INCORRECT, "cyan"))
	print(colored(space_narrative.PORTKEY_ESCAPE, "cyan"))
	portkey_choices = input(space_narrative.PORTKEY_CHOICE_INPUT).upper()
	planets = {"SATURN", "JUPITER", "EARTH", "MERCURY", "MARS", "VENUS", "URANUS", "NEPTUNE"}
	for portkey_choice in portkey_choices:
		if portkey_choices in planets:
			continue
		else:
			portkey_choices = input(space_narrative.PORTKEY_CHOICE_INPUT).upper()
	print(colored(space_narrative.PORTUS_CHARM % (portkey_choices), "cyan"))
	portus_spells = input(brain_narrative.SPELL_INPUT).lower()
	for portus_spell in portus_spells:
		if "portus" in portus_spells:
			continue
		else:
			portus_spells = input(brain_narrative.SPELL_INPUT).lower()
	print(colored(space_narrative.PORTKEY_TRAVEL % (portkey_choices), "cyan"))
	entrance_hall_return()

def death_hall():
	alohomora()
	print(colored(death_narrative.DEATH_HALL_DESCRIPTION, "cyan"))
	room_choices = input(death_narrative.ROOM_CHOICES).lower()
	for room_choice in room_choices:
		if room_choices in hello_answer:
			continue
		elif room_choices in back:
			entrance_hall_return()
		elif room_choices in quit:
			sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
		else:
			room_choices = input(death_narrative.ROOM_CHOICES).lower()
	print(colored(death_narrative.DAIS_WHISPERING, "cyan"))
	archway_choices = input(death_narrative.ARCHWAY_CHOICES).lower()
	if archway_choices in forward:
		print(colored(death_narrative.DEATH_DIED, "cyan"))
		time.sleep(5)
		sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
	elif archway_choices in back:
		print(colored(death_narrative.DEATH_SURVIVED, "cyan"))
		entrance_hall_return()
	else:
		archway_choices = input(death_narrative.ARCHWAY_CHOICES).lower()

def time_room():
	alohomora()
	print(colored(time_narrative.DESCRIPTION_TIME_ROOM, "cyan"))
	room_choices = input(time_narrative.FORWARD_BACK_INPUT).lower()
	for room_choice in room_choices:
		if room_choices in forward:
			continue
		elif room_choices in back:
			entrance_hall_return()
		elif room_choices in quit:
			sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
		else:
			room_choices = input(time_narrative.FORWARD_BACK_INPUT).lower()
	print(colored(time_narrative.BELLJAR_DESCRIPTION, "cyan"))
	belljar_choices = input(time_narrative.BELLJAR_CHOICE_INPUT).lower()
	belljar = {"belljar", "look", "explore", "edge closer to the belljar", "closer"}
	for belljar_choice in belljar_choices:
		if belljar_choices in forward:
			hall_of_prophecy_door()
			hall_of_prophecy()
			return
		elif belljar_choices in belljar:
			print(colored(time_narrative.BELLJAR_CHOSEN_DESCRIPTION,  "cyan"))
			mind_ages = int(input(time_narrative.WHAT_AGE_INPUT))
			if mind_ages == character_age:
				hall_of_prophecy_door()
				hall_of_prophecy()
				return
			elif mind_ages > character_age:
				print(colored(time_narrative.OLDER_AGE, "cyan"))
				hall_of_prophecy_door()
				hall_of_prophecy()
				return
			elif mind_ages < character_age:
				print(colored(time_narrative.YOUNGER_AGE, "cyan"))
				time.sleep(5)
				sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
			elif mind_ages in quit:
				sys.exit(colored(welcome_narrative.EXIT_CHOICE, "yellow"))
			else:
				mind_age = int(input(time_narrative.WHAT_AGE_INPUT))
		else:
			belljar_choices = input(time_narrative.BELLJAR_CHOICE_INPUT).lower()

def hall_of_prophecy_door():
	print(colored(prophecy_narrative.PROPHECY_DOOR, "cyan"))
	alohomora()
