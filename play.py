import time
from narratives.welcome_narrative import TITLE_CREDITS
from game_code import (
	welcome,
	character,
	atrium,
	corridor,
	entrance_hall_desc,
	entrance_hall
	)

print(TITLE_CREDITS)
time.sleep(2)
welcome()
character()
atrium()
corridor()
entrance_hall_desc()
entrance_hall()
