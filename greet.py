from datetime import datetime, date
from colorama import Fore

def get_time():
	now = datetime.now()
	current_time = now.strftime("%H hours %M minutes")
	return current_time

def get_hours():
	now = datetime.now()
	return now.strftime("%H")

def get_date():
	return str(date.today())

def greeting_msg():
    hour = int(get_hours())
    if (hour >= 4 and hour <12 ):
        s = "Good Morning, "
    elif (hour >= 12 and hour <16 ):
        s = "Good Afternoon, "
    else:
        s = "Good Evening, "
    return s