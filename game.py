import time
from constants import TITLE_CREDITS
from department_of_mysteries import (
	welcome,
	character,
	atrium,
	corridor,
	entrance_hall
	)

print(TITLE_CREDITS)
time.sleep(2)

welcome()
time.sleep(2)

character = character()
time.sleep(2)

atrium()
time.sleep(2)

corridor()
time.sleep(2)

entrance_hall()
